# API 规范

## 观察结构（`state` / `observation`）

每次 `step` 返回的 `state` 为嵌套字典，红蓝双方各获得己方视角的子集。

| 字段 | 类型 | 说明 |
|------|------|------|
| `operators` | `list` | 可见算子列表（己方全部 + 通视范围内的敌方） |
| `valid_actions` | `dict` | `{obj_id: {action_type: [参数列表]}}` |
| `cities` | `list` | 夺控点：`coord`, `value`, `flag`(0红/1蓝), `name` |
| `scores` | `dict` | 红蓝双方各维度得分（见下） |
| `judge_info` | `list` | 本回合裁决结果（见下） |
| `landmarks` | `dict` | `roadblocks: list[int]`, `minefields: list[dict]` |
| `time` | `dict` | `cur_step`, `max_step`, `stage`(1部署/2推演) |

### 算子字段（`operators[*]`）

核心字段（完整列表见 `docs/miaosuan/reference/observations.md`）：

| 字段 | 类型 | 说明 |
|------|------|------|
| `obj_id` | int | 算子 ID |
| `color` | int | 0 红 / 1 蓝 |
| `type` | int | 1 步兵 / 2 车辆 / 3 飞机 / 4 工事 / 5 战略支援 |
| `sub_type` | int | 细分类型 |
| `cur_hex` | int | 当前坐标（4 位整数） |
| `blood` | int | 当前血量 |
| `max_blood` | int | 最大血量 |
| `move_state` | int | 0 正常 / 1 行军 / 2 一冲 / 3 二冲 / 4 掩蔽 / 5 半速 |
| `stop` | int | 是否静止 |
| `weapon_unfold_state` | int | 0 锁定 / 1 展开 |
| `carry_weapon_ids` | list[int] | 携带武器 ID 列表 |
| `remain_bullet_nums` | dict[int,int] | 弹药余量（武器 ID → 数量） |
| `keep` | int | 是否被压制 |
| `tire` | int | 疲劳等级 0/1/2 |
| `on_board` | int | 是否在车上 |
| `see_enemy_bop_ids` | list[int] | 可见敌方算子 ID |
| `owner` | int | 所属席位 ID |

### 分数字段（`scores`）

`red_attack`, `red_occupy`, `red_remain`, `red_mission`, `red_total`, `red_win`
`blue_attack`, `blue_occupy`, `blue_remain`, `blue_mission`, `blue_total`, `blue_win`

### 裁决字段（`judge_info[*]`）

四种类型：直瞄射击 / 间瞄射击 / 引导射击 / 雷场裁决。
共有字段：`type`(str), `att_obj_id`, `target_obj_id`, `damage`, `cur_step`

---

## 动作结构

每个动作为一个字典，`actor` 为席位 ID，`type` 区分动作种类。

### 核心动作类型

| type | 动作 | 必填字段 |
|------|------|---------|
| 1 | 机动 | `obj_id`, `move_path: list[int]` |
| 2 | 打击（直瞄） | `obj_id`, `target_obj_id`, `weapon_id` |
| 3 | 上车 | `obj_id`(乘员), `target_obj_id`(车辆) |
| 4 | 下车 | `obj_id`(车辆), `target_obj_id`(乘员) |
| 5 | 夺控 | `obj_id` |
| 6 | 切换状态 | `obj_id`, `target_state` |
| 7 | 移除压制 | `obj_id` |
| 8 | 间瞄射击 | `obj_id`, `jm_pos`, `weapon_id` |
| 9 | 引导射击 | `obj_id`, `target_obj_id`, `weapon_id`, `guided_obj_id` |
| 10 | 停止机动 | `obj_id` |
| 11 | 武器锁定 | `obj_id` |
| 12 | 武器展开 | `obj_id` |
| 333 | 结束部署 | — |

`target_state` 取值：0 正常机动 / 1 行军 / 2 一级冲锋 / 3 二级冲锋 / 4 掩蔽 / 5 半速

### 动作构造辅助函数（`src/rl_scs/actions.py`）

```python
make_move(actor, obj_id, move_path)
make_fire(actor, obj_id, target_obj_id, weapon_id)
make_indirect_fire(actor, obj_id, jm_pos, weapon_id)
make_guided_fire(actor, obj_id, target_obj_id, weapon_id, guided_obj_id)
make_capture(actor, obj_id)
make_state_change(actor, obj_id, target_state)
make_stop(actor, obj_id)
make_board(actor, obj_id, vehicle_id)
make_disembark(actor, vehicle_id, passenger_id)
make_weapon_lock(actor, obj_id)
make_weapon_deploy(actor, obj_id)
make_end_deploy(actor)
```

---

## 武器 ID 常量（`src/rl_scs/weapons.py`）

| 常量名 | ID | 武器名称 |
|--------|----|---------|
| `WEAPON_AA_GUN` | 1 | 防空高炮 |
| `WEAPON_AA_MISSILE_PORTABLE` | 2 | 便携防空导弹 |
| `WEAPON_AA_MISSILE_VEHICLE` | 3 | 车载防空导弹 |
| `WEAPON_SPEED_GUN_ANTI_GROUND` | 4 | 速射炮（对地） |
| `WEAPON_MISSILE_PORTABLE_ANTI_GROUND` | 5 | 便携导弹（对地） |
| `WEAPON_INFANTRY_LIGHT` | 29 | 步兵轻武器 |
| `WEAPON_ROCKET` | 35 | 火箭筒 |
| `WEAPON_CANNON_LARGE` | 36 | 大号直瞄炮 |
| `WEAPON_CANNON_MEDIUM` | 37 | 中号直瞄炮 |
| `WEAPON_VEHICLE_LIGHT` | 43 | 车载轻武器 |
| `WEAPON_CANNON_SMALL` | 54 | 小号直瞄炮 |
| `WEAPON_SPEED_GUN` | 56 | 速射炮 |
| `WEAPON_MISSILE_VEHICLE` | 69 | 车载导弹 |
| `WEAPON_MISSILE_PORTABLE` | 71 | 便携导弹 |
| `WEAPON_CANNON_HEAVY` | 72 | 重型炮 |
| `WEAPON_MISSILE_HEAVY` | 73 | 重型导弹 |
| `WEAPON_MISSILE_MEDIUM_PORTABLE` | 74 | 中型导弹（便携） |
| `WEAPON_MISSILE_SMALL` | 75 | 小型导弹 |
| `WEAPON_MISSILE_LOITERING` | 76 | 巡飞导弹 |
| `WEAPON_MISSILE_MEDIUM_STD` | 83 | 中型导弹（标准） |
| `WEAPON_MISSILE_GUN_LAUNCHED` | 84 | 炮射导弹 |
| `WEAPON_CANNON_MEDIUM_ART` | 88 | 中型炮 |
| `WEAPON_CANNON_LIGHT_ART` | 89 | 轻型炮 |

---

## 游戏规则约束摘要

完整规则见 `docs/miaosuan/rules/rules.md`，以下为实现时的关键约束。

### 机动

- 同方地面单位同格 ≤ 4（堆叠限制）
- 路障不可通过（步兵可通过）
- 车辆地形速度修正：丛林 ×½，居民地 ×⅓，大河/松软地 ×¼
- 坡度 > 5 级车辆不可进入
- 行军只能沿道路，需先锁定武器（1 回合冷却）

### 状态冷却（回合制：实时制 75 秒 → 等待 1 回合）

| 操作 | 冷却 |
|------|------|
| 机动→停止 | 1 回合后可射击/上下车 |
| 武器锁定/展开 | 1 回合 |
| 上车/下车 | 1 回合 |
| 掩蔽切换 | 1 回合 |

### 射击前提

- 车辆：`weapon_unfold_state=1`（展开）才可射击
- 行军状态不可射击
- 射击前检查 `carry_weapon_ids` 和 `remain_bullet_nums`，弹药 0 不合法

### 步兵疲劳

- 一冲：+1 级/格；二冲：+1 级/格
- 二级疲劳不能机动；静止 1 回合 -1 级

### 压制

- 被压制单位当回合跳过所有动作
- 压制持续 1 回合后自动解除
