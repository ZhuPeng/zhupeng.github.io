---
layout: post
title: 书籍推荐：谷歌软件工程实践
tags: 书籍
---

大家好。

今天要推荐一本神书：Software Engineering at Google，我暂且翻译为谷歌软件工程实践。

说到 Google 不知道你想到的是什么，比如搜索、超高市值等等。但是对于软件从业者来说，或多或少会对 Google 内部使用的技术向往，毕竟很多的技术都是在 Google 内部得到了实践，最终通过开源被更多的公司使用，比如 Hadoop 是最开始 Google 内部使用的 MapReduce、Kubernetes 是基于谷歌内部的 Borg 重新设计等等。

本人有幸之前有同事在 Google 工作过，所以会从同事的交流中获得更多的关于 Google 内部的一些工程师文化和工具等。

比如 Google 内部所有的工程师都使用一个统一的代码仓库进行开发，你知道这意味着什么嘛？下图是从网上找到的 2015 年 Google 的代码量汇总信息。

![img](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_format,png.jpeg)

Google 当时所有的代码量只有 86T，为什么我说只有哈，因为如果一个和 Google 同体量的公司不是采用单一源码仓库管理，代码量肯定会远远超过 86T 的。虽然都在一个仓库会给管理带来一些困难，但是收益也是很多的，比如更好的对基础库的升级、要求工程师的代码有严格的测试等等，更多的信息大家可以往上搜索了解，文末的资料也收集了这部分信息。

不知道你是不是跟我一样，会从各个渠道获取到 Google 的部分技术信息，但是并不是很全面。而今天的推荐的书 Software Engineering at Google 比较完整的介绍了 Google 20 多年来，内部的一些技术、文化和工具的演变，会让你对 Google 技术有更全面的了解，满足你的好奇心。

不过，由于我也刚开始看这本书，还不能较完整的给大家介绍，接下来就简单介绍我看到的几个观点吧。

1. 编程和软件工程的区别，以及书中强调的 3 个基本原则

   本书开头就论述了什么是软件工程（Software Engineering），以及软件工程和编程（Programming）的区别。而整体的论述过程会从以下三个方面进行，而这三个方面会做为基本原则贯穿整本书。基本原则如下：

   Time and Change：代码的存活时间和是否能应对改变

   Scale and Growth：团队组织的扩张和效率

   Trade-offs and Costs：基于以上两点，一个组织应该如何权衡和取舍

   ![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_google_3_yuanze.png)

   以上对我来说理解比较深刻的就是 Trade-offs and Costs，我理解任何的方案或者技术都会基于要解决的问题的现状进行权衡和取舍，所以并不是任何的技术在任何公司都适用，最重要的是要理解为什么这样做决策，而这就体现了工程师的重要性。

   

2. 时间与软件项目的可维护性

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_google.time.matain.png)

一个项目可以工作和可维护是完全不同的两个概念，而项目的阶段不同，具体是应该先让其工作起来，还是让项目更好的维护，并没有完美统一的解决方案，这在你的工作中是永远需要思考的一个问题。

好了以上就是全部内容。

如果你对 Software Engineering at Google 感兴趣，可以微信扫描如下二维码关注公众号，后台回复：**谷歌**，获取以上书籍电子版。

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_google.jpeg)
