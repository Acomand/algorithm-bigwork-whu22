问题描述请参考 [实验思考与参考文献.md](./实验思考与参考文献.md) 

项目运行方法

```
python main_int.py --method brickwork_annealing --time_limit 1400
```

&emsp;method 可选为：[brickwork, random_place, ourmethod, brickwork_annealing, ourmethod_annealing]

&emsp;time_limit：表示模拟退火算法中，模拟退火的时间限制

整个项目的代码结构如下

```
├─dataset
|   *.csv （经过处理后的数据）
|   process.py （数据处理脚本）
|
├─result
|   *.txt
|
├─solve_method
|   *.py （表示每一种方法）
|
├─box.py （基类）
|
├─main_int.py （整数条件下的主函数）
|
├─main_float.py （浮点条件下的主函数）
|
├─plot.py (绘图工具)
```

下面对几个方法进行说明

&emsp;brickwork：参考文章http://www.jos.org.cn/1000-9825/18/2083.pdf实现；

&emsp;random_place：该策略为每次随机选择一个可放置点进行放置，主要用于与其他方法进行对比；

&emsp;ourmethod：brickwork方法中存在参考线，但我们认为参考线并无实际价值，因此直接去掉了参考线。
