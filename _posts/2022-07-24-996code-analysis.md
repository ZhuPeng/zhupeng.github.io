---
layout: post
title: 牛逼真的强，996 代码分析工具推荐
tags: 代码分析
---

大家好。

程序员是一个创作型的职业，频繁的加班并不能增加产出，而国内 996 的公司文化，真的一言难尽。但是如果你进到一家公司，你能从哪些观察来判断这家公司的工作强度（加班文化）？是看大家走得早不早吗？有一定的参考意义，但是如果走得晚呢，可能是大家不敢提前走而在公司耗时间。

今天要推荐一个代码分析工具 code996，它可以统计 Git 项目的 commit 时间分布，进而推导出这个项目的编码工作强度。这算是一种对项目更了解的方式，杜绝 996 从了解数据开始。

我们先来看 code996 分析出来的结果示例，以下是分析项目的基本情况：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_code996.1.png)

通过图表查看 commit 提交分布：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_code996.2.png)

对比项目工作时间类型：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_code996.3.png)

如果你对 code996 是如何工作的，以下是作者的说明：

![image-20220724211802252](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220724211802252.png)

因为代码是公司的很重要的资产，泄露是肯定不行的，为了解决大家的后顾之忧，该项目是完全安全的。

![image-20220724211908612](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220724211908612.png)

code996 除了能够分析项目的实际工作强度，也能用来分析我们代码编写的情况，对自身了解自己代码编写效率的时段、最近的工作强度等都是非常好的一个输入。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/hellodigua/code996

开源项目作者：[hellodigua](https://github.com/hellodigua)