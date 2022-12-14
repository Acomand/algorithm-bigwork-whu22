参考资料

1. 装箱问题简介

https://blog.51cto.com/u_15324424/4555733#:~:text=%E4%B8%89%E7%BB%B4%E8%A3%85%E7%AE%B1%E9%97%AE%E9%A2%98%EF%BC%88Three%20Dimensional,Container%20Loading%20Poblem%EF%BC%89%E6%8C%87%E5%9C%A8%E6%BB%A1%E8%B6%B3%E5%AE%B9%E7%A7%AF%E9%99%90%E5%88%B6%E3%80%81%E5%A4%96%E5%BD%A2%E5%87%A0%E4%BD%95%E9%99%90%E5%88%B6%E5%92%8C%E7%A8%B3%E5%AE%9A%E6%80%A7%E9%99%90%E5%88%B6%E7%AD%89%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%83%85%E5%86%B5%E4%B8%8B%EF%BC%8C%E6%8A%8A%E4%B8%80%E5%AE%9A%E6%95%B0%E9%87%8F%E4%BD%93%E7%A7%AF%E8%BE%83%E5%B0%8F%E7%9A%84%E7%89%A9%E5%93%81%E6%94%BE%E5%85%A5%E5%85%B7%E6%9C%89%E8%BE%83%E5%A4%A7%E5%AE%B9%E9%87%8F%E7%9A%84%E4%B8%80%E4%B8%AA%E6%88%96%E5%A4%9A%E4%B8%AA%E7%AE%B1%E5%AD%90%EF%BC%8C%E8%BE%BE%E5%88%B0%E6%89%80%E7%94%A8%E7%AE%B1%E5%AD%90%E6%95%B0%E9%87%8F%E6%9C%80%E5%B0%91%E3%80%81%E7%A9%BA%E9%97%B4%E5%88%A9%E7%94%A8%E7%8E%87%E6%9C%80%E9%AB%98%E3%80%81%E7%A8%B3%E5%AE%9A%E6%80%A7%E6%9C%80%E5%A5%BD%E3%80%81%E8%A3%85%E8%BD%BD%E4%BB%B7%E5%80%BC%E6%9C%80%E9%AB%98%E3%80%81%E5%AE%B9%E9%87%8D%E6%AF%94%E6%9C%80%E9%AB%98%E7%AD%89%E7%9B%AE%E7%9A%84%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96%E7%9A%84%E9%97%AE%E9%A2%98%E3%80%82

2. 一个基于启发式搜索的静态算法

[Janet-19/3d-bin-packing-problem: A python model of 3D Bin Packing problem (github.com)](https://github.com/Janet-19/3d-bin-packing-problem)

3. 禁忌搜索与遗传算法

https://github.com/mahdims/3D-bin-packing

4. 遗传算法

https://github.com/sinunfan/3DBinPacking

5. 一个基于搜索树的方法

https://www.jianshu.com/p/cf1c91472da4

问题分析

1. 在线算法

在我看来，在线算法和装箱问题是两个相对独立的问题。只要实现了静态装箱，就一定能出现在线算法，这里有几个解决在线算法的思路

问题描述：由于每个物品都要装载，因此这个问题就被转化为了：装在哪里，怎么进行物品翻转的问题

I. 补充法。随机假设之后的几个物品，判断该物品应该装在何处。

II. 贪心法。进行物品的状态枚举，3*6种，看什么样的操作使得剩余空间最大。


算法思路

1. Greedy

静态算法：优先装大的、或者小的、或者其他规则

动态算法：随机旋转进行装载