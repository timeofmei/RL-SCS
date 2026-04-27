# 想定

> 来源: https://wargame.ia.ac.cn/docs/reference/scenario/

# 想定

## 想定文件

想定文件是环境初始化时的必要文件，内部包含一个想定的所有初始条件。想定文件直接决定一场推演的初始态势。开发者可以自行修改想定文件的内容，达到修改想定的目的。

以下为想定文件json中，最外层的数据格式和内容含义：

```
{
    "operators": "此属性和态势中的'operators'完全一致",
    "time": {
        "cur_step": "初始步数，int",
        "max_time": "最大推演步数，int"
    },
    "cities": [
        {
            "coord": "位置，int",
            "value": "分值，int",
            "flag": "占领状态，-1-未占领，0-红方占领，1-蓝方占领",
            "name": "主要夺控点，次要夺控点"
        }
    ],
    "landmarks": {
        "roadblocks": ["路障位置，int"],
        "minefields": ["雷场位置，int"]
    },
    "blueprints": ["如果此想定会用到导演增加算子动作，需要在此处添加要增加的算子数据"],
    "config": {
        "electronic_jamming_config": {
            "global_jam_switch": "bool, 是否开启全局干扰规则",
        },
        "fire_support_config": {
            "red_X_switch": "bool，红方x火力支援开关",
            "red_X_num": "int，红方x火力次数",
            "red_X_wait": "int，红方x火力延迟",
            "red_X_duration": "int，红方x火力持续时间",
            "red_Y_switch": "bool，红方y火力支援开关",
            "red_Y_num": "int，红方y火力支援次数",
            "red_Y_wait": "int，红方y火力支援延迟时间",
            "red_Y_duration": "int，红方y火力支援持续时间",
            "blue_X_switch": "bool，蓝方x火力支援开关",
            "blue_X_num": "int，蓝方x火力支援次数",
            "blue_X_wait": "int，蓝方x火力支援延迟时间",
            "blue_X_duration": "int，蓝方x火力支援持续时间",
            "blue_Y_switch": "bool，蓝方y火力支援开关",
            "blue_Y_num": "int，蓝方y火力支援次数",
            "blue_Y_wait": "int，蓝方y火力支援延迟时间",
            "blue_Y_duration": "int，蓝方y火力支援持续时间"
        },
        "launch_mission_config": {
            "launch_mission_deadline": "int，发射任务最后期限",
            "undisguised_launch_point_reduction": "int，未伪装的发射任务的分数惩罚",
            "warhead_num": "int，弹头数量",
            "mission_score": "int，发射任务分",
            "exposure_consecutive_min_time_lv1": "int，一级暴露触发惩罚最小连续时间",
            "exposure_consecutive_min_time_lv2": "int，二级暴露触发惩罚最小连续时间",
            "exposure_consecutive_min_time_lv3": "int，三级暴露触发惩罚最小连续时间",
            "exposure_score_deduction_lv2": "int，二级暴露分数惩罚",
            "exposure_score_deduction_lv3": "int，三级暴露分数惩罚"
        },
        "satellite_support_switch_red": "bool，卫星凌空规则开关",
        "satellite_support_switch_blue": "bool，卫星凌空规则开关",
        "satellite_support_delay_time_red": "int，卫星凌空效果延迟时间",
        "satellite_support_delay_time_blue": "int，卫星凌空效果延迟时间",
        "satellite_support_duration_time_red": "int，卫星凌空效果持续时间",
        "satellite_support_duration_time_blue": "int，卫星凌空效果持续时间",
        "satellite_support_cooldown_time_red": "int，卫星凌空冷却时间",
        "satellite_support_cooldown_time_blue": "int，卫星凌空冷却时间"
    },
    "launch_sites": "此属性与态势中的'launch_sites'完全一致",
    "com_graph": "此属性与态势中的'com_graph'完全一致"
}
```