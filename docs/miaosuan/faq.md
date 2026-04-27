# Frequently Asked Questions

> 来源: https://wargame.ia.ac.cn/docs/faq/

# Frequently Asked Questions

## **环境如何进入推演阶段**

当所有Agent都发出“结束部署动作后”，环境进入推演阶段

## **如何判断当前在部署阶段还是推演阶段**

检查态势中`observation["time"]["stage"]`，值为1说明在部署阶段，值为2说明在推演阶段

## **为什么SDK运行输出“did not pass authentication”，或没有输出“did pass authentication”?**

原因：SDK版本过时  
解决方法：

1. 删除land\_wargame\_train\_env python库
2. 重新安装land\_wargame\_train\_env-\*.whl
3. 如果~/.engin\_config文件存在，请删除