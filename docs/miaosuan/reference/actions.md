# 动作

> 来源: https://wargame.ia.ac.cn/docs/reference/actions/

# 动作

agent的`step`函数必须返回一个动作列表。
列表中的每个元素`action`表示的是该agent当前帧要进行的动作的确切信息，需要遵守正确的数据结构。
而后此动作列表将作为`TrainEnv.step`的参数传入环境。

每个动作的正确结构见下文。

## **机动**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 1,
    "move_path": "机动路径 list(int)"
}
```

## **打击**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "攻击算子ID int",
    "type": 2,
    "target_obj_id": "目标算子ID",
    "weapon_id": "武器ID int"
}
```

## **上车**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "乘员算子ID int",
    "type": 3,
    "target_obj_id": "车辆算子ID"
}
```

## **下车**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "车辆算子ID int",
    "type": 4,
    "target_obj_id": "乘员算子ID"
}
```

## **夺控**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 5
}
```

## **切换状态**

Note

状态之间互斥，算子在某一时刻只能处于一种状态。

```
 {
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 6,
    "target_state": "目标状态 0-正常机动 1-行军 2-一级冲锋 3-二级冲锋, 4-掩蔽 5-半速"
}
```

## **移除压制**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 7
}
```

## **间瞄射击**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "攻击算子ID int",
    "type": 8,
    "jm_pos": "目标位置",
    "weapon_id": "武器ID int"
}
```

## **引导射击**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "引导算子ID int",
    "type": 9,
    "target_obj_id": "目标算子ID",
    "weapon_id": "武器ID int",
    "guided_obj_id": "射击算子ID"
}
```

## **停止机动**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 10
}
```

## **武器锁定**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 11
}
```

## **武器展开**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 12
}
```

## **取消间瞄计划**

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "算子ID int",
    "type": 13
}
```

## **配置编组信息**

Note

此动作为营长专属动作，作用是分配算子给到指定玩家。

```
{
    "actor": "int 动作发出者席位",
    "type": 100,
    "info": {
        "int 席位数": {
            "operators": [
                "int 算子id",
                "int 算子id"
            ]
        }
    }
}
```

## **下达作战任务**

Note

此动作为营长专属动作。作用是向一个玩家下达一种战斗任务。目前支持四种任务，“进攻”，“防御”，“侦察”，“集结”。

进攻任务

```
{
    "actor": "int 动作发出者席位",
    "type": 207,
    "seat": "命令接收人id",
    "hex": "任务目标位置",
    "start_time": "起始时间",
    "end_time": "结束时间",
    "unit_ids": "执行任务的单位ID列表",
    "route": "执行此任务的途径点列表"
}
```

防御任务

```
{
    "actor": "int 动作发出者席位",
    "type": 208,
    "seat": "命令接收人id",
    "hex": "任务目标位置",
    "start_time": "起始时间",
    "end_time": "结束时间",
    "unit_ids": "执行任务的单位ID列表",
    "route": "执行此任务的途径点列表"
}
```

侦察任务

```
{
    "actor": "int 动作发出者席位",
    "type": 209,
    "seat": "命令接收人id",
    "hex": "任务目标位置",
    "radius": "侦察半径"
    "start_time": "起始时间",
    "end_time": "结束时间",
    "unit_ids": "执行任务的单位ID列表",
    "route": "执行此任务的途径点列表"
}
```

集结任务

```
{
    "actor": "int 动作发出者席位",
    "type": 210,
    "seat": "命令接收人id",
    "hex": "任务目标位置",
    "start_time": "起始时间",
    "end_time": "结束时间",
    "unit_ids": "执行任务的单位ID列表",
    "route": "执行此任务的途径点列表"
}
```

## **删除作战任务**

Note

此动作为营长专属动作。删除某个战斗任务

```
{
    "actor": "int 动作发出者席位",
    "type": 202,
    "msg_id": "int 要删除的作战指令的id"
}
```

## **部署上车**

Note

此动作为赛前部署动作，使agent可以在部署阶段瞬时完成一些动作。此动作是算子瞬时上车。可做此动作的算子类型有，步兵和无人车。

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "乘员算子ID int",
    "type": 303,
    "target_obj_id": "车辆算子ID"
}
```

## **部署下车**

Note

此动作为赛前部署动作，使agent可以在赛前瞬时完成一些动作。此动作是算子瞬时下车。可做此动作的算子类型有，步兵和无人车。

```
{
    "actor": "int 动作发出者席位",
    "obj_id": "车辆算子ID int",
    "type": 304,
    "target_obj_id": "乘员算子ID"
}
```

## **解聚**

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 14
}
```

## **聚合**

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "target_obj_id": "算子ID int",
    "type": 15
}
```

## **部署解聚**

Note

此动作为赛前部署动作，使agent可以在赛前瞬时完成一些动作。

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 314
}
```

## **部署聚合**

Note

此动作为赛前部署动作，使agent可以在赛前瞬时完成一些动作。

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "target_obj_id": "算子ID int",
    "type": 315
}
```

## **改变高程**

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 16,
    "target_altitude": "目标高程，20超低空，200低空 500高空"
}
```

## **部署改变高程**

Note

此动作为赛前部署动作，使agent可以在赛前瞬时完成一些动作。

Warning

此动作正在开发中

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 316,
    "target_altitude": "目标高程，20超低空，200低空 500高空"
}
```

## **开启校射雷达**

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 17
}
```

## **进入工事**

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 18,
    "target_obj_id": "工事算子ID"
}
```

## **退出工事**

```
{
    "actor": "int 动作发出者",
    "obj_id": "算子ID int",
    "type": 19,
    "target_obj_id": "工事算子ID"
}
```

## **布雷**

```
{
    "actor": "int 动作发出者",
    "obj_id": "布雷车算子ID int",
    "type": 20,
    "target_pos": "布雷坐标 int"
}
```

## **导演击杀算子**

Note

此动作为导演动作，只有导演可以下达此动作。

```
{
    "actor": "int",
    "type": 401,
    "target_obj_id": "击杀算子id"
}
```

## **导演布雷**

Note

此动作为导演动作，只有导演可以下达此动作。

```
{
    "actor": "int",
    "type": 402,
    "target_pos": "布雷坐标"
}
```

## **导演建造路障**

Note

此动作为导演动作，只有导演可以下达此动作。

```
{
    "actor": "int",
    "type": 403,
    "target_pos": "路障坐标"
}
```

## **导演增加算子**

Note

此动作为导演动作，只有导演可以下达此动作。为了使用此动作，必须在环境初始化阶段注册导演信息；同时要在想定文件中加入"blueprints"属性来声明新增算子的模板。

```
{
    "actor": "int",
    "type": 404,
    "sub_type": "算子sub_type",
    "color": "0红, 1蓝",
    "hex": "空降位置"
}
```

## **结束部署**

Note

此动作为赛前部署动作。当环境收到所有Agent发出的此动作之后，结束部署阶段并进入正常推演阶段。

```
{
    "actor": "int，动作发出者",
    "type": 333
}
```

## **发送聊天信息**

```
{
    "actor": "int 动作发出者",
    "type": 204,
    "to_all": "0-发给队友，1-发给全部",
    "msg_body": "custoum strings, up to 100 characters in Chinese and 50 words in English"
}
```

## **发送辅助渲染信息**

发送辅助渲染信息，前端页面收到此动作之后将在人类界面中进行相应渲染。agent可通过此动作向人类发送有用的的视觉信息

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
      "hexs": ["六角格坐标"], 
      "graphic_type": "渲染模式，见下文",
      "word": "渲染字符",
      "color": "颜色，hex各式，#ffffff",
      "description": "对于此命令的其他描述，字符串"
    }  
}
```

Info

不同的渲染模式拥有不同的渲染效果

渲染模式

```
{
  "attention": "hexs中的六角格上放置感叹号",
  "sub_type": "在hexs中的六角格上放置一个算子模型",
  "target": "在hexs中的六角格上放置一个旗子",
  "see_range": "在hexs中的六角格渲染成绿色",
  "fire_range": "在hexs中的六角格渲染成红色",
  "custom": "在hexs中的六角格上渲染'color'颜色和'word'文字"
}
```

渲染示例

警示信息

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
    "hexs": [1111,2222,3333], 
    "graphic_type": "attention",
    "description": "注意这些点"
    }
}
```

敌方位置预测

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
    "hexs": [1111,2222,3333], 
    "graphic_type": "sub_type",
    "word": "1"
    "description": "这些地点可能有敌方坦克"
    }
}
```

目标点

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
    "hexs": [1111,2222,3333], 
    "graphic_type": "target",
    "description": "我们去攻击这几个点"
    }
}
```

通视范围

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
    "hexs": [1111,2222,3333], 
    "graphic_type": "see_range",
    "description": "敌方坦克能看到以下六角格"
    }  
}
```

火力范围

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
    "hexs": [1111,2222,3333], 
    "graphic_type": "fire_range",
    "word": "5",
    "description": "敌方坦克可以对以下六角格进行打击，攻击等级5"
    }  
}
```

自定义渲染

```
{
    "actor": "int 动作发出者",
    "type": 205,
    "msg_body": {
    "hexs": [1111,2222,3333], 
    "graphic_type": "custom",
    "word": "你好",
    "color": "#ffffff",
    "description": "在以上六角格渲染‘你好’字符,用#ffffff颜色盖住六角格"
    }  
}
```

## **电子干扰**

```
{
    "actor": "int 动作发出者",
    "type": 21,
    "obj_id": "算子ID int",
    "direction": "干扰方向"
}
```

Note

被干扰的无人单位（无人车，无人机）无法接受指令，但可以继续执行已有的指令，效果持续75秒，动作冷却时间为75秒。

## **全局电子干扰**

```
{
    "actor": "int 动作发出者",
    "type": 22,
}
```

Note

全局干扰动作使战场上所有能进行引导射击的单位失去能力，效果持续75秒，动作冷却时间为75秒。

## **X火力支援**

场外目标校射火力支援

```
{
    "actor": "int 动作发出者",
    "type": 23,
}
```

## **Y火力支援**

场外无校射火力支援

```
{
    "actor": "int 动作发出者",
    "type": 24,
}
```

## **全局干扰**

队长可以启动全局干扰动作并在特定时间内影响全场所有的无人装备

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 22 | 动作类型 |

## **局部干扰**

具有电子干扰的单位可以开启干扰，并影响场上无人装备

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 21 | 动作类型 |
| `direction` | int | 干扰方向, 必须是0~5 |

## **伪装**

一号车实施伪装行动

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 25 | 动作类型 |
| `obj_id` | int | 算子id |

## **发射**

一号车实施发射行动

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 27 | 动作类型 |
| `obj_id` | int | 算子id |

## **设路障**

放置路障

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 28 | 动作类型 |
| `obj_id` | int | 算子id |

## **清路障**

清理路障

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 29 | 动作类型 |
| `obj_id` | int | 算子id |

## **破坏通信节点**

破坏通信节点

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 30 | 动作类型 |
| `obj_id` | int | 算子id |

## **维修通信节点**

维修通信节点

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 31 | 动作类型 |
| `obj_id` | int | 算子id |

## **抗干扰**

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 32 | 动作类型 |
| `obj_id` | int | 算子id |

## **卫星过境侦察**

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 33 | 动作类型 |

## **派发发射任务**

| Field Name | Data Type | Description |
| --- | --- | --- |
| `actor` | int | 席位 |
| `type` | 334 | 动作类型 |
| `obj_id` | int | 算子id |
| `start_time` | int | 任务开始时间 |
| `end_time` | int | 任务结束时间 |
| `launch_sites` | list[int] | 发射位置 |