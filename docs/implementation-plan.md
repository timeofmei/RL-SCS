# 实现计划

庙算规则适配的具体开发任务，按推荐顺序排列。每项可独立开发和单测。

## 1. HexMap（`src/rl_scs/map.py`）

- [ ] 从 `basic.json` 加载地图（高程、地形、道路、河流、邻格）
- [ ] `get_neighbors(coord) -> list[int]` — 六邻格，越界填 -1，从右侧起逆时针
- [ ] `get_distance(coord1, coord2) -> int` — hex 格距
- [ ] `is_valid(pos) -> bool` — 坐标合法性
- [ ] `gen_move_route(coord1, coord2, mode) -> list[int]` — Dijkstra 路径规划
  - mode: 0 车辆机动 / 1 车辆行军 / 2 步兵机动 / 3 空中机动
  - 行军模式只走道路格
  - 从 `cost.json` 读取各模式通行代价
- [ ] `can_see(coord1, coord2, see_mode) -> bool` — 高程线性插值通视判断
  - 10 种 see_mode（地对地 0 … 高空对高空 9）
  - 居民地/丛林格高程 +1 修正（端点格不修正）
- [ ] `get_grid_at_distance(center, d_min, d_max) -> set[int]` — 范围格集合

## 2. 武器库（`src/rl_scs/weapons.py`）

- [ ] 定义全部武器 ID 具名常量（见 `docs/api-spec.md` 武器表）
- [ ] 无其他逻辑；射击合法性检查在动作验证器中完成

## 3. 场景加载（`SCS_Game.py`）

- [ ] `setup(scenario_path, map_path)` 从 JSON 初始化：
  - 算子列表（id、阵营、类型、初始坐标、血量、武器配置）
  - 夺控点列表（坐标、初始归属、分值）
  - 雷场、路障初始位置
  - 回合上限（`max_step`）
- [ ] 生成初始 `state`（stage=1 部署阶段）

## 4. 动作层（`src/rl_scs/actions.py`）

- [ ] 动作构造辅助函数（`make_move`, `make_fire`, `make_capture` 等，见 `docs/api-spec.md`）
- [ ] 动作验证器：对照 `valid_actions` 检查合法性
  - 非法动作静默丢弃，写入本回合 `judge_info` 错误记录
  - 常见非法情形：弹药耗尽、武器未展开、目标不可见、单位被压制、堆叠超限

## 5. 回合裁决引擎（`SCS_Game.py`）

- [ ] `step(red_actions, blue_actions) -> (state, done)` 实现裁决流程：
  1. 验证动作
  2. 机动（含地形/坡度/堆叠约束）
  3. 射击裁决（直瞄/间瞄/引导，查裁决表计算伤害）
  4. 夺控（检查夺控点及相邻 6 格）
  5. 状态切换
  6. 上下车
  7. 冷却/疲劳/压制计数更新
  8. 算子死亡处理（blood ≤ 0 移出 operators）
  9. 生成新 `state`
- [ ] 部署阶段：仅接受 `type` 在 303/304/314/315 的部署动作，双方均提交 333 后切换 stage=2
- [ ] 终局判断：`cur_step >= max_step` 或一方算子全灭

## 6. 合法动作生成（`SCS_Game.py`）

每次生成 `state` 时同步计算 `valid_actions`：

- [ ] 机动（type=1）：未被压制 + 非行军状态
- [ ] 打击（type=2）：武器已展开 + 目标可见 + 弹药 > 0 + 通视
- [ ] 夺控（type=5）：在夺控点格 + 相邻格无敌方地面单位
- [ ] 切换状态（type=6）：排除当前状态 + 行军需在道路格
- [ ] 上车（type=3）：同格有可乘车辆 + 双方均停止
- [ ] 下车（type=4）：在车上 + 车辆停止
- [ ] 武器锁定/展开（type=11/12）：车辆类型 + 停止状态

## 7. 奖励函数（`SCS_Game.py`）

- [ ] 即时奖励：`sum(j["damage"] for j in judge_info if j["attack_color"] == my_color)` - 己方受损
- [ ] 夺控奖励：夺控点归属从敌变我时 +`city.value`
- [ ] 终局奖励：`scores["red_win"]` / `scores["blue_win"]`

## 8. 渲染适配（`src/rl_scs/render/SCS_Renderer.py`）

- [ ] 数据源切换为 `state["operators"]`（`color`, `type`, `cur_hex`, `blood/max_blood`）
- [ ] 渲染夺控点（`cities`，按归属上色）
- [ ] 渲染雷场、路障（`landmarks`）
- [ ] 本回合裁决高亮（`judge_info`，显示 1 回合后消失）

## 开发说明

- 各模块可独立单测：`HexMap` 不依赖游戏状态，动作验证器不依赖渲染
- 裁决表数值参见 `docs/miaosuan/rules/tables.md`
- 完整观察/动作字段定义见 `docs/api-spec.md`
- 架构概览见 `docs/architecture.md`
