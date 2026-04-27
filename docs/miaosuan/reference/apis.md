# 环境接口

> 来源: https://wargame.ia.ac.cn/docs/reference/apis/

# 环境接口

## **AI本地开发**

AI开发需要自行编写名为`Agent`的类，继承`BaseAgent`类并重载一些方法:

- [setup](#baseagentsetup)
- [step](#baseagentstep)
- [reset](#baseagentreset)

这些方法均来自BaseAgent类

## **BaseAgent类接口**

`BaseAgent`类包含3个抽象方法，[setup](#baseagentsetup)、[step](#baseagentstep)，[reset](#baseagentreset)。这些方法为AI必须编写的方法，未实现这些方法的agent将无法使用本SDK进行开发和线上接入。

### **`BaseAgent.setup`**

**功能：**在推演开始之前，向agent提供此次推演的相关配置信息，agent应在此函数中进行一些初始化等操作。此方法只接收一个参数`setup_info`；此参数为一个字典，字典内包含关于当前推演的一些开局信息。以下字典内参数均为在正式网络对抗时，在线对抗引擎一定会向此接口提供的参数，单机离线时完全由开发者自行决定是否提供。

**参数说明：**

| 参数名 | 数据类型 | 说明 |
| --- | --- | --- |
| setup\_info | dict | 此场对局相关的详细配置信息 |
| setup\_info["scenario"] | dict | [想定数据](../scenario/) |
| setup\_info["basic\_data"] | dict | [地图基础数据](../map/#basicdata) |
| setup\_info["cost\_data"] | dict | [地图通行成本数据](../map/#costdata) |
| setup\_info["see\_data"] | dict | [地图通视数据](../map/#seedata) |
| setup\_info["seat"] | int | 本场对局的席位数，用来区分智能体的唯一值 |
| setup\_info["faction"] | int | 阵营id，0为红，1为蓝 |
| setup\_info["role"] | int | 角色，0为连长，1为营长 |
| setup\_info["user\_name"] | string | 用户名 |
| setup\_info["user\_id"] | int | 用户id |
| setup\_info["state"] | dict | 完整初始态势（第一帧），包括红蓝绿三方的完整观测数据 |

**返回值：**无

**示例：（来自DemoAI）**
在agent实例化时，通过setup告诉agent关于此场特定的推演的一些信息。setup在每场推演前都要调用一次。agent在此时可以主动加载，处理这场对局将要用的数据，保存一些参数等必要操作。

```
def setup(self, setup_info: dict):
    self.scenario = setup_info["scenario"]
    self.color = setup_info["faction"]
    self.faction = setup_info["faction"]
    self.seat = setup_info["seat"]
    self.role = setup_info["role"]
    self.user_name = setup_info["user_name"]
    self.user_id = setup_info["user_id"]
    self.priority = {
        ActionType.Occupy: self.gen_occupy,
        ActionType.Shoot: self.gen_shoot,
        ActionType.GuideShoot: self.gen_guide_shoot,
        ActionType.JMPlan: self.gen_jm_plan,
        ActionType.LayMine: self.gen_lay_mine,
        ActionType.ActivateRadar: self.gen_activate_radar,
        ActionType.ChangeAltitude: self.gen_change_altitude,
        ActionType.GetOn: self.gen_get_on,
        ActionType.GetOff: self.gen_get_off,
        ActionType.Fork: self.gen_fork,
        ActionType.Union: self.gen_union,
        ActionType.EnterFort: self.gen_enter_fort,
        ActionType.ExitFort: self.gen_exit_fort,
        ActionType.Move: self.gen_move,
        ActionType.RemoveKeep: self.gen_remove_keep,
        ActionType.ChangeState: self.gen_change_state,
        ActionType.StopMove: self.gen_stop_move,
        ActionType.WeaponLock: self.gen_WeaponLock,
        ActionType.WeaponUnFold: self.gen_WeaponUnFold,
        ActionType.CancelJMPlan: self.gen_cancel_JM_plan
    }  # choose action by priority
    self.observation = None
    self.map = Map(
        setup_info["basic_data"],
        setup_info["cost_data"],
        setup_info["see_data"]
    )  # use 'Map' class as a tool
    self.map_data = self.map.get_map_data()
```

### **`BaseAgent.step`**

**功能：**agent在对局过程中需要调用`step`接收态势以及输出agent动作列表。以下参数均为在正式网络对抗时，引擎一定会向此接口提供的参数，单机离线时完全由开发者自行决定是否提供。

**参数说明：**

| 参数名 | 数据类型 | 说明 |
| --- | --- | --- |
| observation | dict | [态势数据](../observations/) |

**返回值：**

| 数据类型 | 说明 |
| --- | --- |
| List[dict] | agent返回生成的符合格式要求的动作列表。详见[动作数据](../actions/) |

**示例：（来自DemoAI）**
在`BaseAgent.step`中开发者需要体现AI的策略。`BaseAgent.step`函数传入的参数是态势信息,输出的则是agent的动作列表。因为agent所作出的一切动作都必须要通过step函数来返回，所以开发者需要在`BaseAgent.step`函数中完成接受态势以及生成动作的功能。态势数据和动作数据见[态势数据](../observations/)以及[动作数据](../actions/)。

```
def step(self, observation: dict):
    self.observation = observation  # save observation for later use
    self.team_info = observation["role_and_grouping_info"]
    self.controllable_ops = observation["role_and_grouping_info"][self.seat][
        "operators"
    ]
    communications = observation["communication"]
    for command in communications:
        if command["type"] in [200, 201] and command["info"]["company_id"] == self.seat:
            if command["type"] == 200:
                self.my_mission = command
            elif command["type"] == 201:
                self.my_direction = command
    total_actions = []

    if observation["time"]["stage"] == 1:
        actions = []
        for item in observation["operators"]:
            if item["obj_id"] in self.controllable_ops:
                operator = item
                if operator["sub_type"] == 2 or operator["sub_type"] == 4:
                    actions.append(
                        {
                            "actor": self.seat,
                            "obj_id": operator["obj_id"],
                            "type": 303,
                            "target_obj_id": operator["launcher"],
                        }
                    )
        actions.append({
            "actor": self.seat,
            "type": 333
        })
        return actions

    # loop all bops and their valid actions
    for obj_id, valid_actions in observation["valid_actions"].items():
        if obj_id not in self.controllable_ops:
            continue
        for (
            action_type
        ) in self.priority:  # 'dict' is order-preserving since Python 3.6
            if action_type not in valid_actions:
                continue
            # find the action generation method based on type
            gen_action = self.priority[action_type]
            action = gen_action(obj_id, valid_actions[action_type])
            if action:
                total_actions.append(action)
                break  # one action per bop at a time
    return total_actions
```

### **`BaseAgent.reset`**

**功能：**在一场推演结束后，agent需要调用`reset`清空AI在对局中调用的数据、模型、资源等。

**参数说明：**无

**返回值：**无

**示例：（来自DemoAI）**
agent每场对局结束后执行一次`reset`函数。`reset`函数没有参数和返回值，仅用于赛后释放agent在策略中用到的数据、模型等外部信息。选手需要在`reset`函数中清空自己在对局中生成的数据等外部信息，以避免数据未清空的情况下导致这些数据对接下来的对局过程中agent的决策产生意外的影响。

```
def reset(self):
    self.scenario = None
    self.color = None
    self.priority = None
    self.observation = None
    self.map = None
    self.scenario_info = None
    self.map_data = None
    self.seat = None
    self.faction = None
    self.role = None
    self.controllable_ops = None
    self.team_info = None
    self.my_direction = None
    self.my_mission = None
    self.user_name = None
    self.user_id = None
    self.history = None
```

## **TrainEnv类接口**

### **`TrainEnv.__init__`**

**功能：**构建环境实例

**参数说明**：无

**返回值**：环境实例

### **`TrainEnv.setup`**

**功能：**配置环境，输入此次推演环境所需的所有配置信息，并初始化环境后返回第一帧的完整红蓝绿态势。

**参数说明：**

| 参数名 | 数据类型 | 说明 |
| --- | --- | --- |
| `setup_info` | `dict` | 整个方法的参数`dict`合集 |
| `setup_info['scenario_data']` | `dict` | [想定数据](../scenario/) |
| `setup_info['basic_data']` | `dict` | [地图基础数据](../map/#basicdata) |
| `setup_info['cost_data']` | `dict` | [地图通行成本数据](../map/#costdata) |
| `setup_info['see_data']` | `dict` or `none` | [地图通视数据](../map/#seedata)，SDK自5.0.0版本起，see\_data可为None |
| `setup_info['player_info']` | `list` | 推演席位信息。`player_info`是一个`list[dict]`，结构如下 |
| `setup_info['player_info'][*]['seat']` | `int` | 代表player的席位 |
| `setup_info['player_info'][*]['faction']` | `int` | 代表player阵营 |
| `setup_info['player_info'][*]['role']` | `int` | 代表player的角色 |
| `setup_info['player_info'][*]['user_name']` | `int` | 用户名 |
| `setup_info['player_info'][*]['user_id']` | `int` | 用户id |

**返回值：**返回游戏完整第一帧完整红蓝绿态势字典,详见[态势数据](../observations/)

### **`TrainEnv.step`**

**功能：**接受各类动作，包括机动，打击，部署上车，兵力部署等，处理所有动作后返回新的一帧完整态势，以及是否达到游戏结束条件的flag。详见[动作数据](../actions/)和[态势数据](../observations/)。

**参数说明：**

| 参数名 | 数据类型 | 说明 |
| --- | --- | --- |
| action\_msgs | list[dict] | 动作列表, 详见[动作数据](../actions/) |

**返回值：**返回游戏完整态势字典，返回游戏是否结束的boolean

| 返回变量名 | 数据类型 | 说明 |
| --- | --- | --- |
| state | list[dict] | 态势列表，其中state[0]代表红方态势，state[1]代表蓝方态势， state[-1]代表绿方态势，详见[态势数据](../observations/) |
| done | bool | 推演是否到达结束条件 |

### **`TrainEnv.reset`**

**功能**：重置环境，重置子模块，清空环境中的变量，释放环境占用的资源

**参数说明**：无

**返回值**：无