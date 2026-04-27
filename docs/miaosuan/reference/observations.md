# 态势

> 来源: https://wargame.ia.ac.cn/docs/reference/observations/

# 态势

## **状态与态势**

**State and Observation**

`state`一般代表环境当前的所有状态。`observation`一般情况下代表对于某个智能体可观测的态势。`observation`是`state`的子集。

`TrainEnv`的`step`函数返回的`state`，表示当前环境的所有状态合集。状态合集有红方蓝方绿方态势组成：`state[0]`代表的是红方态势，`state[1]`代表的是蓝方态势,`state[-1]`代表的是绿方态势。
agent代码的`step`函数接受的参数是态势`observation`，它封装了当前时间，此agent能观测到的所有盘面信息，包括算子信息、裁决信息等。以下是态势最外层的数据结构以及他们代表的含义。

| Field | Type | Description |
| --- | --- | --- |
| `actions` | `list` | 上一步接收到的动作 |
| `cities` | `list` | 各个夺控点的信息 |
| `communication` | `list` | 通信相关信息 |
| `jm_points` | `list` | 间瞄点信息 |
| `judge_info` | `list` | 裁决信息 |
| `landmarks` | `dict` | 地标信息，雷场，路障 |
| `operators` | `list` | 算子信息 |
| `passengers` | `list` | 乘员信息 |
| `role_and_grouping_info` | `dict` | 玩家信息和编组信息 |
| `scenario_id` | `int` | 想定ID |
| `scores` | `dict` | 分数信息 |
| `terrain_id` | `int` | 地图 ID |
| `time` | `dict` | 时间信息 |
| `valid_actions` | `dict` | 当前态势下的可做动作信息 |
| `extra` | `dict` | 额外信息 |

### **算子属性**

**`observation["operators"]`和`observation["passengers"]`**

Note

注：`passengers`为车上乘员算子属性，其字段与`operators`字段完全一致

| Field | Type | Description |
| --- | --- | --- |
| `obj_id` | `int` | 算子ID |
| `color` | `int` | 算子阵营 0-红 1-蓝 |
| `type` | `int` | 算子类型 1-步兵 2-车辆 3-飞机 4-工事 5-战略支援算子 |
| `name` | `str` | 名称 |
| `sub_type` | `int` | 细分类型（如坦克、无人机等，详见枚举说明） |
| `basic_speed` | `int` | 基础速度 km/h |
| `armor` | `int` | 装甲类型 0-无 1-轻型 2-中型 3-重型 4-复合装甲 |
| `A1` | `int` | 是否有行进间射击能力 |
| `stack` | `int` | 是否堆叠 |
| `carry_weapon_ids` | `list[int]` | 携带武器ID |
| `remain_bullet_nums` | `dict[int, int]` | 剩余弹药数（按类型分类） |
| `remain_bullet_nums_bk` | `dict[int, int]` | 敌方看到的弹药数 |
| `guide_ability` | `int` | 是否有引导射击能力 |
| `value` | `int` | 分值 |
| `valid_passenger_types` | `list[int]` | 可承载的乘员 sub\_type |
| `max_passenger_nums` | `dict[int, int]` | 最大承载数 |
| `loading_capacity` | `int` | 最大承载车班数 |
| `observe_distance` | `list[int]` | 对不同 sub\_type 的观察距离 |
| `move_state` | `int` | 机动状态（0-正常 1-行军 等） |
| `cur_hex` | `int` | 当前坐标（四位数） |
| `cur_pos` | `float` | 当前格到下一格的百分比进度 |
| `speed` | `int` | 当前机动速度 格/s |
| `move_to_stop_remain_time` | `int` | 机动转停止的剩余时间 |
| `can_to_move` | `int` | 是否可继续机动（停止转换中） |
| `flag_force_stop` | `int` | 是否被强制停止 |
| `stop` | `int` | 是否静止 |
| `move_path` | `list[int]` | 计划机动路径 |
| `blood` | `int` | 当前血量 |
| `max_blood` | `int` | 最大血量 |
| `tire` | `int` | 疲劳等级（0-不疲劳，1-一级，2-二级） |
| `tire_accumulate_time` | `int` | 累积疲劳时间 |
| `keep` | `int` | 是否被压制 |
| `keep_remain_time` | `int` | 压制剩余时间 |
| `on_board` | `int` | 是否在车上 |
| `car` | `int` | 所属车辆ID |
| `launcher` | `int` | 所属发射器ID（下车/发射后） |
| `passenger_ids` | `list[int]` | 乘客ID列表 |
| `launch_ids` | `list[int]` | 发射单元ID列表 |
| `lose_control` | `int` | 是否失去控制（如无人车） |
| `alive_remain_time` | `int` | 巡飞弹剩余存活时间 |
| `get_on_remain_time` | `float` | 上车剩余时间 |
| `get_on_partner_id` | `list[int]` | 上车相关ID（车与乘员） |
| `get_off_remain_time` | `int` | 下车剩余时间 |
| `get_off_partner_id` | `list[int]` | 下车相关ID |
| `change_state_remain_time` | `int` | 状态切换剩余时间 |
| `target_state` | `int` | 状态转换目标状态 |
| `weapon_cool_time` | `int` | 武器冷却剩余时间 |
| `weapon_unfold_time` | `int` | 武器展开/锁定剩余时间 |
| `weapon_unfold_state` | `int` | 武器状态（0-锁定，1-展开） |
| `see_enemy_bop_ids` | `list[int]` | 可见敌方算子ID列表 |
| `owner` | `int / str` | 所属玩家席位ID |
| `close_combat` | `int` | 是否在同格交战中 |
| `stationary_count` | `int` | 静止步长 |
| `forking` | `int` | 是否在解聚 |
| `forking_remain_time` | `int` | 解聚剩余时间 |
| `unioning` | `int` | 是否在聚合 |
| `unioning_remain_time` | `int` | 聚合剩余时间 |
| `unioning_partner` | `int` | 聚合对象ID |
| `unioining_role` | `int` | 聚合角色（1-发起者，2-被动者） |
| `altitude` | `int` | 当前高度 |
| `changing_altitude` | `int` | 是否在改变高度 |
| `changing_altitude_remain_time` | `int` | 改变高度剩余时间 |
| `target_altitude` | `int` | 目标高度 |
| `activating_radar` | `int` | 是否开启雷达 |
| `activating_radar_remain_time` | `int` | 开启雷达剩余时间 |
| `radar_activated` | `int` | 雷达是否开启 |
| `in_fort` | `int` | 是否在工事中 |
| `fort` | `int` | 所在工事ID |
| `entering_fort` | `int` | 是否正在进入工事 |
| `entering_fort_remain_time` | `int` | 进入工事剩余时间 |
| `entering_fort_partner` | `list[int]` | 进入工事相关对象ID |
| `exiting_fort` | `int` | 是否在离开工事 |
| `exiting_fort_remain_time` | `int` | 离开工事剩余时间 |
| `exiting_fort_partner` | `list[int]` | 离开工事相关对象ID |
| `fort_passengers` | `list[int]` | 工事中的算子ID |
| `laying_mine` | `int` | 是否正在布雷 |
| `laying_mine_remain_time` | `int` | 布雷剩余时间 |
| `remaining_mine_count` | `int` | 剩余雷场数 |
| `laying_mine_target_pos` | `int` | 当前布雷目标格 |
| `observalbe_distance` | `int` | 可被观察的基础距离 |
| `disrupt_cooldown` | `int` | 干扰冷却时间 |
| `disrupt_duration` | `int` | 干扰持续时间 |
| `disrupt_direction` | `int` | 干扰方向（六个方向之一） |
| `disrupt_ongoing` | `boolean` | 是否正在进行电子干扰 |
| `disrupted` | `boolean` | 是否被电子干扰 |
| `disrupted__globally` | `boolean` | 是否被全局电子干扰 |
| `warhead_loaded` | `boolean` | 是否装弹 |
| `disguised` | `boolean` | 是否伪装下 |
| `disguising` | `boolean` | 是否正在伪装 |
| `disguising_remain_time` | `int` | 伪装剩余时间 |
| `launching` | `boolean` | 是否正在发射 |
| `launching_remain_time` | `boolean` | 发射剩余时间 |
| `launched` | `boolean` | 是否完成发射 |
| `jam_counter_cooldown_remain_time` | `boolean` | 抗干扰剩余时间 |
| `roadblock_building_capability` | `boolean` | 设障能力指示 |
| `roadblock_building` | `boolean` | 是否正在设障 |
| `roadblock_building_remain_time` | `int` | 设障剩余时间 |
| `roadblock_building_remain_number` | `int` | 设障剩余次数 |
| `roadblock_clearing_capability` | `boolean` | 清障能力指示 |
| `roadblock_clearing` | `boolean` | 是否正在清障 |
| `roadblock_clearing_remain_time` | `int` | 清障剩余时间 |
| `comnode_sabotaging_capability` | `boolean` | 破坏通信节点能力指示 |
| `comnode_sabotaging_remain_number` | `int` | 破坏通信节点剩余次数 |
| `comnode_repairing_capability` | `boolean` | 维修破坏节点能力指示 |

### **时间**

**`observation["time"]`**

```
{
    "cur_step": "int, 当前步长",
    "tick": "int, 每次step会前进多少帧",
    "max_time": "int, 最大帧数",
    "max_step": "int, 最大步数，等于max_time/tick",
    "stage": "int, 当前处于的阶段，0-环境配置阶段，1-部署阶段，2-正常推进阶段"
}
```

### **间瞄点信息**

**`observation["jm_points"]`**

态势信息中包含己方的正在飞行的和正在爆炸的间瞄点信息，以及敌方正在爆炸的间瞄点信息，敌方正在飞行的间瞄点信息无法得到。

| Field Name | Description | Data Type |
| --- | --- | --- |
| `obj_id` | 攻击算子ID | int |
| `color` | 炮弹所属方 | int |
| `weapon_id` | 攻击武器ID | int |
| `pos` | 位置 | int |
| `status` | 当前状态  0-正在飞行 (Flying) 1-正在爆炸 (Exploding) 2-无效 (Invalid) | int |
| `fly_time` | 已飞行时间 | int |
| `boom_time` | 已爆炸时间 | int |
| `align_status` | 校射状态 | int |
| `flag_offset` | 是否偏移 | bool |
| `off_field` | 是否为场外火力支援 | bool |
| `x_or_y` | 火力支援类型 | str |

### **夺控点信息**

**`observation["cities"]`**

```
[
    {
        "coord": "int, 坐标",
        "value": "int, 分值",
        "flag": "int, 阵营 0-红 1-蓝",
        "name": "str, 名称 str"
    }
]
```

### **对局分数信息**

**`observation["scores"]`**

| Field Name | Description | Data Type |
| --- | --- | --- |
| `red_attack` | 红方战斗得分 | int |
| `red_occupy` | 红方夺控分 | int |
| `red_remain` | 红方剩余算子分 | int |
| `red_reamin_max` | 红方最大剩余得分 | int |
| `red_mission` | 红方任务分 | int |
| `red_total` | 红方总分 | int |
| `red_win` | 红方净胜分 | int |
| `blue_attack` | 蓝方攻击得分 | int |
| `blue_occupy` | 蓝方夺控分 | int |
| `blue_remain` | 蓝方剩余得分 | int |
| `blue_reamin_max` | 蓝方最大剩余得分 | int |
| `blue_mission` | 蓝方任务分 | int |
| `blue_total` | 蓝方总分 | int |
| `blue_win` | 蓝方净胜分 | int |

### **裁决信息**

**`observation["judge_info"]`**

共有四种裁决信息：直瞄射击，间瞄射击，引导射击，雷场裁决

```
[
  # 直瞄射击类型
  {
    "att_level": "int, 攻击等级  ",
    "att_obj_blood": "int, 攻击算子血量",
    "att_obj_id": "int, 攻击算子ID",
    "attack_color": "int, 攻击算子颜色",
    "attack_sub_type": "int, 攻击算子类型",
    "cur_step": "int, 当前步长",
    "damage": "int, 最终战损",
    "distance": "int, 距离",
    "ele_diff": "int, 高差等级",
    "ori_damage": "int, 原始战损",
    "random1": "int, 随机数1",
    "random2": "int, 随机数2",
    "random2_rect": "int, 随机数2修正值",
    "rect_damage": "int, 战损修正值",
    "target_color": "int, 目标颜色",
    "target_obj_id": "int, 目标id",
    "target_sub_type": "int, 目标类型",
    "type": "str, 直瞄射击",
    "wp_id": "int, 武器ID int"
    },
  # 间瞄射击类型
  {
    "align_status": "int, 较射类型 0-无较射 1-格内较射 2-目标较射",
    "att_obj_blood": "int, 攻击算子血量",
    "att_obj_id": "int, 攻击算子ID",
    "attack_color": "int, 攻击算子颜色",
    "attack_sub_type": "int, 攻击算子类型",
    "cur_step": "int, 当前步长",
    "damage": "int, 最终战损",
    "distance": "int, 距离",
    "ori_damage": "int, 原始战损",
    "ori_random2": "int, ",
    "offset": "bool, 偏移 bool",
    "random1": "int, 随机数1",
    "random2": "int, 随机数2",
    "random2_rect": "int, 随机数2修正值",
    "rect_damage": "int, 战损修正值",
    "target_color": "int, 目标颜色",
    "target_obj_id": "int, 目标id",
    "target_sub_type": "int, 目标类型",
    "type": "str, 间瞄射击",
        "wp_id": "int, 武器ID"
  },
  # 引导射击类型
    {
    "att_level": "int, 攻击等级",
    "att_obj_blood": "int, 攻击算子血量",
    "att_obj_id": "int, 攻击算子ID",
    "attack_color": "int, 攻击算子颜色",
    "attack_sub_type": "int, 攻击算子类型",
    "cur_step": "int, 当前步长",
    "damage": "int, 最终战损",
    "distance": "int, 距离",
    "ele_diff": "int, 高差等级",
    "guide_obj_id": "int, 引导算子ID",
    "ori_damage": "int, 原始战损",
    "random1": "int, 随机数1",
    "random2": "int, 随机数2",
    "random2_rect": "int, 随机数2修正值",
    "rect_damage": "int, 战损修正值",
    "target_color": "int, 目标颜色",
    "target_obj_id": "int, 目标id",
    "target_sub_type": "int, 目标类型",
    "type": "str, 引导射击",
    "wp_id": "int, 武器ID",
  },
  # 雷场射击类型
  {
    "target_obj_id": "int, 目标算子id",
    "target_color": "int, 目标颜色",
    "target_type": "int, 目标类型",
    "target_armor": "int, 目标护甲",
    "original_damage_random_number": "int, 原始战损随机数",
    "calibration_random_number": "int, 修正随机数",
    "calibration_value": "int, 修正值",
    "final_damage": "int, 最终战损",
    "cur_step": "int, 当前步数",
    "minefield_id": "int, 雷场id",
    "minefield_hex": "int, 雷场位置",
    "minefield_color": "int, 雷场颜色",
    "type": "str, 雷场裁决"
  }
]
```

### **编组角色信息**

**`observation["role_and_grouping_info"]`**

`key`为席位`value`为席位对应的玩家的角色和编组信息

```
{
    0: {
        "faction": "int 红为0，蓝为1",
        "role": "int 分队为0，群队为1",
        "operators": "list[int],拥有的算子id",
        "user_id": "int",
        "user_name": "str"
    },
    1: {
        "faction": "int, 红为0，蓝为1",
        "role": "int, 分队为0，群队为1",
        "operators": "list[int], 拥有的算子id",
        "user_id": "int",
        "user_name": "str"
    },
    ...
}
```

### **通信信息**

**`observation["communication"]`**

包含了本方阵营当前的战斗任务信息等通信信息,由队长发出

```
[
    # 进攻任务信息
    {
        "actor": "int 动作发出者席位",
        "type": 207,
        "seat": "命令接收人id",
        "hex": "任务目标位置",
        "start_time": "起始时间",
        "end_time": "结束时间",
        "unit_ids": "执行任务的单位ID列表",
        "route": "执行此任务的途径点列表"
    },
    # 防御任务
    {
        "actor": "int 动作发出者席位",
        "type": 208,
        "seat": "命令接收人id",
        "hex": "任务目标位置",
        "start_time": "起始时间",
        "end_time": "结束时间",
        "unit_ids": "执行任务的单位ID列表",
        "route": "执行此任务的途径点列表"
    },
    # 侦察任务
    {
        "actor": "int 动作发出者席位",
        "type": 209,
        "seat": "命令接收人id",
        "hex": "任务目标位置",
        "radius": "侦察半径",
        "start_time": "起始时间",
        "end_time": "结束时间",
        "unit_ids": "执行任务的单位ID列表",
        "route": "执行此任务的途径点列表"
    },
    # 集结任务
    {
        "actor": "int 动作发出者席位",
        "type": 210,
        "seat": "命令接收人id",
        "hex": "任务目标位置",
        "start_time": "起始时间",
        "end_time": "结束时间",
        "unit_ids": "执行任务的单位ID列表",
        "route": "执行此任务的途径点列表"
    },
    # 聊天信息
    {
        "actor": "int, 本方营长的席位id",
        "type": "int, 204",
        "receive_step": "int, 接收时的步数",
        "to_all": "int, 0-对队友发出，1-对所有人发出",
        "msg_body": "str",
        "msg_id": "int, 此消息的id"
    },
    # 渲染信息
    {
        "actor": "int 动作放出者",
        "type": "int, 205",
        "msg_id": "int, 此消息的id",
        "receive_step": "int, 接收时的步数",
        "to_all": "int, 0-对队友发出，1-对所有人发出",
        "msg_body": {
            "hexs": "list[int], 要渲染的六角格坐标", 
            "graphic_type": "str, 渲染类型",
            "word": "str, 渲染字符",
            "color": "str, 颜色",
            "description": "str, 对于此命令的其他描述"
        } 
    },
    # 发射任务
    {
        "actor": "int 动作放出者",
        "type": "int, 334",
        "msg_id": "int, 此消息的id",
        "receive_step": "int, 接收时的步数",
        "start_time": "int, 任务起始时间",
        "end_time": "int， 任务结束时间",
        "launch_sites": "list[int] 发射地点列表"
    },
]
```

### **地标信息**

**`observation["landmarks"]`**

包含一局推演中的地标信息，比如路障，雷场的信息

```
"landmarks": {
    "roadblocks": "list[int], 六角格坐标",
    "minefields": [
        {
            "id": "int, 雷场id",
            "name": "str, 雷场",
            "hex": "int, 位置",
            "color": "int, 颜色",
            "creator": "int/None, 雷场创造者，None-想定自带雷场，int-算子创造雷场",
            "roads": [
            {
                "id": "int, 通路id",
                "creator": "int, 通路制造者，int-制造通路的算子id",
                "direction": "int, 通路方向，0~5，0是正右侧，按逆时针递进",
                "color": "int, 通路颜色",
                "hex": "int, 通路位置"
            }
            ]
        }
    ]
}
```

### **地图id**

**`observation["terrain_id"]`**

包含此次推演使用的地图id

```
"terrain_id": "int"
```

### **想定id**

**`observation["想定id“scenario_id”"]`**

包含此次推演使用的想定的id

```
"scenario_id": "int"
```

### **合法动作**

**`observation["valid_actions"]`**

此项包含在当前态势下，所有算子的所有可做动作的合集，以及与动作相关的额外信息，比如攻击动作会提供此攻击的攻击等级，使用的武器等。比如上下车动作的目标算子。同一算子可在同一时刻有多个可以做的valid actions，AI可以根据自己的策略选择最优的动作。

Info

valid\_actions中不包含队长动作（配置兵力编组信息，下达作战任务等），不包含部署动作（部署上车，部署下车，部署解聚，部署聚合，结束部署等）

```
{
    "算子ID": {
        "1-机动": null,
        "2-射击": [
            {
                "target_obj_id": "目标ID int",
                "weapon_id": "武器ID int",
                "attack_level": "攻击等级 int"
            }
        ],
        "3-上车": [
            {
                "target_obj_id": "车辆ID int"
            }
        ],
        "4-下车": [
            {
                "target_obj_id": "乘客ID int"
            }
        ],
        "5-夺控": null,
        "6-切换状态": [
            {
                "target_state": "目标状态 0-正常机动 1-行军 2-一级冲锋 3-二级冲锋 4-掩蔽"
            }
        ],
        "7-移除压制": null,
        "8-间瞄": [
            {
                "weapon_id": "武器ID"
            }
        ],
        "9-引导射击": [
            {
                "guided_obj_id": "被引导算子ID int",
                "target_obj_id": "目标算子ID",
                "weapon_id": "武器ID int",
                "attack_level": "攻击等级 int"
            }
        ],
        "10-停止机动": null,
        "11-武器锁定": null,
        "12-武器展开": null,
        "13-取消间瞄计划": null,
        "14-解聚": null,
        "15-聚合": [{"target_obj_id": "聚合对象ID int"}],
        "16-改变高程": [{"target_altitude": "目标高程 int"}],
        "17-开启炮兵校射雷达": null,
        "18-进入工事": [{"target_obj_id": "工事ID int"}],
        "19-退出工事": [{"target_obj_id": "工事ID int"}],
        "20-布雷": null,
    }
}
```

如果是绿方态势中，会有绿方专属的valid\_actions

```
{
    "401-导演击杀算子": null,
    "402-导演布雷": null,
    "403-导演建造路障": null,
    "404-导演增加算子": null
}
```

### **历史动作**

**`observation["actions"]`**

此项包含了上一帧态势中传入了的动作列表，以及动作的详细参数。如果动作有错误，会提供错误码以及错误信息。

```
"actions": [
    {
        "cur_step": "int, 当前步长",
        "message": "dict, 动作信息",
        "error": {
            "code": "int, 错误码 int",
            "message": "str, 错误原因"
        }
    }
]
```

### 通信图

**`observation["com_graph"]`**

| Field Name | Description | Data Type |
| --- | --- | --- |
| `nodes` | 节点列表 | list |
| `edges` | 边列表 | list |

**`observation["com_graph"]["nodes"][*]`**

| Field Name | Description | Data Type |
| --- | --- | --- |
| `com_node_id` | 节点id | int |
| `position` | 位置 | int |
| `functional` | 是否具备功能 | bool |

**`observation["com_graph"]["edges"][*]`**

| Field Name | Description | Data Type |
| --- | --- | --- |
| `node1_id` | 节点1id | int |
| `node2-id` | 节点2id | int |

### 发射地点

**`observation["launch_sites"][*]`**

| Field Name | Description | Data Type |
| --- | --- | --- |
| `site_positon` | 位置 | int |

### 额外信息

**`observation["extra"]`**

| Field Name | Description | Data Type |
| --- | --- | --- |
| `global_jam_switch` | 是否开启全局干扰规则 | bool |
| `global_jam_duration_red` | 全局干扰的剩余时间红方 | int |
| `global_jam_duration_blue` | 全局干扰的剩余时间蓝方 | int |
| `global_jam_cooldown_red` | 全局干扰的冷却时间红方 | int |
| `global_jam_cooldown_blue` | 全局干扰的冷却时间蓝方 | int |
| `warhead_remain_num` | 剩余的弹头数量 | int |
| `x_fire_support_switch_red` | x火力支援红方开关 | bool |
| `x_fire_support_switch_blue` | x火力支援蓝方开关 | bool |
| `x_fire_support_remain_num_red` | x火力支援剩余次数红方 | int |
| `x_fire_support_remain_num_blue` | x火力支援剩余次数蓝方 | int |
| `y_fire_support_switch_red` | y火力支援红方开关 | bool |
| `y_fire_support_switch_blue` | y火力支援蓝方开关 | bool |
| `y_fire_support_remain_num_red` | y火力支援剩余次数红方 | int |
| `y_fire_support_remain_num_blue` | y火力支援剩余次数蓝方 | int |
| `satellite_support_switch_red` | 卫星凌空规则开关 | bool |
| `satellite_support_switch_blue` | 卫星凌空规则开关 | bool |
| `satellite_support_delay_remain_time_red` | 卫星凌空效果延迟时间剩余 | int |
| `satellite_support_delay_remain_time_blue` | 卫星凌空效果延迟时间剩余 | int |
| `satellite_support_duration_remain_time_red` | 卫星凌空效果持续剩余时间 | int |
| `satellite_support_duration_remain_time_blue` | 卫星凌空效果持续剩余时间 | int |
| `satellite_support_cooldown_remain_time_red` | 卫星凌空冷却剩余时间 | int |
| `satellite_support_cooldown_remain_time_blue` | 卫星凌空冷却剩余时间 | int |

## **敌方阵营的不可见信息或部分可见的信息**

Warning

以下信息为在我方视角下的敌方算子信息和间瞄点信息中不可见或部分可见的属性，请谨慎使用以下属性

敌方算子信息 observation['operators']

```
[
    {
        "remain_bullet_nums": "剩余弹药数 dict{弹药类型 int 0-非导弹, 100-重型导弹, 101-中型导弹, 102-小型导弹: 剩余弹药数 int}",
        "move_to_stop_remain_time": "机动转停止剩余时间 >0表示",
        "can_to_move": "是否可机动标志位.只在停止转换过程中用来判断是否可以继续机动.强制停止不能继续机动,正常停止可以继续机动. 0-否 1-是",
        "move_path": "计划机动路径 [int] 首个元素代表下一目标格，只能观察到敌方机动的下一格，不能观察到全部路径",
        "tire_accumulate_time": "疲劳状态剩余时间 int",
        "keep_remain_time": "压制状态剩余时间 int",
        "launcher": "算子下车/发射后,记录所属发射器 int",
        "passenger_ids": "乘客列表 [int]",
        "launch_ids": "记录车辆发射单元列表 [int]",
        "alive_remain_time": "巡飞弹剩余存活时间",
        "get_on_remain_time": "上车剩余时间 float",
        "get_off_remain_time": "下车剩余时间 float",
        "weapon_unfold_time": "武器锁定状态表示展开剩余时间, 武器展开状态下表示锁定剩余时间 float",
        "see_enemy_bop_ids": "观察敌方算子列表 list(int)",
        "C2": "普通弹药数",
        "C3": "剩余导弹数",
        "target_state": "状态转换过程中记录目标状态 int 0-正常机动 1-行军 2-一级冲锋 3-二级冲锋 4-掩蔽",
    }
]
```

敌方间瞄点信息 observation['jm\_points']

```
[
    {
        "obj_id": "攻击算子ID int",
        "weapon_id": "攻击武器ID int",
        "fly_time": "剩余飞行时间 float",
        "boom_time": "剩余爆炸时间 float"
    }
]
```