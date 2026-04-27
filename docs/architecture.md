# 架构文档

## 模块结构

```
src/rl_scs/
├── SCS_Game.py          # 环境核心：setup / step / reset，回合裁决引擎
├── map.py               # HexMap：路径规划、通视、格距、邻格
├── weapons.py           # 武器 ID 具名常量
├── actions.py           # 动作构造辅助函数 + 动作验证器
├── render/
│   ├── SCS_Renderer.py  # pygame 渲染
│   ├── CounterCreator.py
│   ├── fonts.py         # FONT_SANS / FONT_MONO 跨平台选择
│   └── Color.py
├── example_configurations/  # YAML 场景配置（旧格式，逐步迁移）
└── assets/              # 单位和地形图片
data/                    # 不纳入 git
├── maps/<map_id>/
│   ├── basic.json       # 地形、高程、道路、河流、邻格
│   └── cost.json        # 各通行模式的格间通行代价
└── scenarios/
    └── <scenario_id>.json   # 想定：算子初始配置、夺控点、弹药
```

## 环境生命周期

```
setup(scenario, map_data)
    ↓
[部署阶段 stage=1]
    双方提交部署动作（type=303/304/314/315 等）
    双方均提交 type=333 → 进入推演阶段
    ↓
[推演阶段 stage=2]
    while not done:
        red_obs, blue_obs = env.observe()
        state, done = env.step(red_actions, blue_actions)
    ↓
reset()
```

## 回合裁决顺序

每次 `step` 内按以下顺序处理，确保结果确定性：

1. 验证动作合法性（非法动作静默丢弃，记录错误到 `judge_info`）
2. 处理**机动**（type=1/10，含堆叠、地形、坡度约束）
3. 处理**射击**（type=2/8/9，含通视、弹药、武器展开状态检查）
4. 处理**夺控**（type=5，含相邻格敌方检查）
5. 处理**状态切换**（type=6，含冷却回合计数）
6. 处理**上下车**（type=3/4）
7. 更新冷却计数、疲劳、压制倒计时
8. 生成新的 `state`（观察 + 合法动作 + 分数 + 裁决结果）

## HexMap

地图坐标为 4 位整数（行×100 + 列）。相邻六格从右侧起逆时针排列：
`[右, 右上, 左上, 左, 左下, 右下]`，越界格填 -1。

通行模式（`mode`）：0 车辆机动 / 1 车辆行军 / 2 步兵机动 / 3 空中机动

通视模式（`see_mode`）：0 地对地 / 1 低空对低空 / 2 低空对地 / 3 超低空对地
/ 4 超低空对超低空 / 5 低空对超低空 / 6 高空对地 / 7 高空对超低空
/ 8 高空对低空 / 9 高空对高空

## 地图格数据格式（basic.json）

```json
{
  "ele_grade": 5,
  "map_data": [[{
    "elev": 20,
    "cond": 0,
    "roads": [0, 1, 0, 0, 2, 0],
    "rivers": [0, 0, 1, 0, 0, 0],
    "neighbors": [1201, 1101, 1100, 1199, 1299, 1300]
  }]]
}
```

`cond`：0 开阔地 / 1 丛林 / 2 居民地 / 3 松软地 / 4 大河 / 5 路障
`roads`：0 无 / 1 乡村路(黑) / 2 一般公路(红) / 3 等级公路(黄)

## 奖励函数

| 奖励类型 | 来源 | 说明 |
|---------|------|------|
| 即时 | `judge_info[*].damage` | 对敌伤害为正，己方受损为负 |
| 中间 | `cities` 归属变化 | 夺控点从敌变我时 +`value` |
| 终局 | `scores["red_win"]` / `scores["blue_win"]` | `done=True` 时的净胜分 |

## 渲染

数据源从 `state["operators"]` 读取。`color=0` 红方，`color=1` 蓝方，`type` 决定图标。
血量条显示 `blood/max_blood`。额外渲染夺控点（`cities`）、雷场、路障（`landmarks`）。
