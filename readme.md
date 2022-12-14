
算法实践题
物流公司在流通过程中，需要将打包完毕的箱子装入到一个货车的车厢中，为了提高物流效率，需要将车厢尽量填满，显然，车厢如果能被100%填满是最优的，但通常认为，车厢能够填满85%，可认为装箱是比较优化的。
设车厢为长方形，其长宽高分别为L，W，H；共有n个箱子，箱子也为长方形，第i个箱子的长宽高为li，wi，hi（n个箱子的体积总和是要远远大于车厢的体积），做以下假设和要求：
1. 长方形的车厢共有8个角，并设靠近驾驶室并位于下端的一个角的坐标为（0,0,0），车厢共6个面，其中长的4个面，以及靠近驾驶室的面是封闭的，只有一个面是开着的，用于工人搬运箱子；
2. 需要计算出每个箱子在车厢中的坐标，即每个箱子摆放后，其和车厢坐标为（0,0,0）的角相对应的角在车厢中的坐标，并计算车厢的填充率。

问题分解为基础和高级部分，完成基础部分可得78分以上，完成高级部分可得85分以上。
基础部分：
1. 所有的参数为整数；2. 静态装箱，即从n个箱子中选取m个箱子，并实现m个箱子在车厢中的摆放（无需考虑装箱的顺序，即不需要考虑箱子从内向外，从下向上这种在车厢中的装箱顺序）；3. 所有的箱子全部平放，即箱子的最大面朝下摆放；4. 算法时间不做严格要求，只要1天内得出结果都可。

高级部分：
1. 参数考虑小数点后两位；2. 实现在线算法，也就是箱子是按照随机顺序到达，先到达先摆放；3. 需要考虑箱子的摆放顺序，即箱子是从内到外，从下向上的摆放顺序；4. 因箱子共有3个不同的面，所有每个箱子有3种不同的摆放状态；5. 算法需要实时得出结果，即算法时间小于等于2秒。

群里同学问了的：
1. 避免悬空，可以部分悬空(大物体在小物体上面)；
2. 箱子共三种不同的面，每种面可以横着摆或者竖着摆，所以总共有6种摆放方式；
3. 高级部分可以部分完成；
4. 在线算法禁止移动已摆放的箱子

装箱问题：<br/>
箱柜装载问题(three-dimensional bin packing problem，简称3D-BPP)：给定一些不同类型的方型箱子和一些规格统一的方型容器，问题是要把所有箱子装入最少数量的容器中；<br/>
（这个算法我感觉也是通用的，我室友就是用这个算法来解决问题的）<br/>
容器装载问题(three-dimensional container-packing problems，简称3D-CPP)：在该问题中，所有箱子要装入一个不限尺寸的容器中，目标是要找一个装填，使得容器体积最小；<br/>
√ 背包装载问题(three-dimensional knapsack loading problems，简称**3D-KLP**)：每个箱子有一定的价值，背包装载是选择一部分箱子装入容器中，使得装入容器中的箱子总价值最大。如果把箱子的体积作为价值，则目标转化为**使容器浪费的体积最小**。

参考：
1.https://blog.csdn.net/TIQCmatlab/article/details/112131351?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-112131351-blog-125376144.pc_relevant_recovery_v2&spm=1001.2101.3001.4242.2&utm_relevant_index=4
2.https://blog.csdn.net/weixin_37522117/article/details/125376144
3.http://www.jos.org.cn/1000-9825/18/2083.pdf
4.https://blog.csdn.net/weixin_37522117/article/details/125376144

5.装箱问题简介

https://blog.51cto.com/u_15324424/4555733#:~:text=%E4%B8%89%E7%BB%B4%E8%A3%85%E7%AE%B1%E9%97%AE%E9%A2%98%EF%BC%88Three%20Dimensional,Container%20Loading%20Poblem%EF%BC%89%E6%8C%87%E5%9C%A8%E6%BB%A1%E8%B6%B3%E5%AE%B9%E7%A7%AF%E9%99%90%E5%88%B6%E3%80%81%E5%A4%96%E5%BD%A2%E5%87%A0%E4%BD%95%E9%99%90%E5%88%B6%E5%92%8C%E7%A8%B3%E5%AE%9A%E6%80%A7%E9%99%90%E5%88%B6%E7%AD%89%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%83%85%E5%86%B5%E4%B8%8B%EF%BC%8C%E6%8A%8A%E4%B8%80%E5%AE%9A%E6%95%B0%E9%87%8F%E4%BD%93%E7%A7%AF%E8%BE%83%E5%B0%8F%E7%9A%84%E7%89%A9%E5%93%81%E6%94%BE%E5%85%A5%E5%85%B7%E6%9C%89%E8%BE%83%E5%A4%A7%E5%AE%B9%E9%87%8F%E7%9A%84%E4%B8%80%E4%B8%AA%E6%88%96%E5%A4%9A%E4%B8%AA%E7%AE%B1%E5%AD%90%EF%BC%8C%E8%BE%BE%E5%88%B0%E6%89%80%E7%94%A8%E7%AE%B1%E5%AD%90%E6%95%B0%E9%87%8F%E6%9C%80%E5%B0%91%E3%80%81%E7%A9%BA%E9%97%B4%E5%88%A9%E7%94%A8%E7%8E%87%E6%9C%80%E9%AB%98%E3%80%81%E7%A8%B3%E5%AE%9A%E6%80%A7%E6%9C%80%E5%A5%BD%E3%80%81%E8%A3%85%E8%BD%BD%E4%BB%B7%E5%80%BC%E6%9C%80%E9%AB%98%E3%80%81%E5%AE%B9%E9%87%8D%E6%AF%94%E6%9C%80%E9%AB%98%E7%AD%89%E7%9B%AE%E7%9A%84%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96%E7%9A%84%E9%97%AE%E9%A2%98%E3%80%82

6.一个基于启发式搜索的静态算法

[Janet-19/3d-bin-packing-problem: A python model of 3D Bin Packing problem (github.com)](https://github.com/Janet-19/3d-bin-packing-problem)

7.禁忌搜索与遗传算法

https://github.com/mahdims/3D-bin-packing

8.遗传算法

https://github.com/sinunfan/3DBinPacking

9.一个基于搜索树的方法

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
