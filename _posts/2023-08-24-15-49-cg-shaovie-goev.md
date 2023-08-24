---
layout: post
title: GitHub 开源项目 shaovie/goev 介绍，goev is a lightweight, concise i/o event demultiplexer implementation in Go
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 shaovie/goev，该项目在 GitHub 有超过 94 Star，用一句话介绍该项目就是：“goev is a lightweight, concise i/o event demultiplexer implementation in Go”。


![](https://raw.githubusercontent.com/shaovie/goev/master/images/goev.png)
![](https://raw.githubusercontent.com/shaovie/goev/master/images/bench-32v-64g.png)





背景介绍：
在进行Go语言的TCP网络编程时，我们通常使用标准库（go net），但是标准库的协程压力较大，因此我们需要一种更轻量级、高性能的非阻塞I/O事件驱动网络框架。goev就是为此而生的。

项目介绍：
goev是一款基于Go语言的高性能、轻量级、非阻塞、I/O事件驱动的网络框架。它从ACE的设计模式中汲取灵感，为TCP网络编程项目提供了优雅而简洁的解决方案。使用goev，您可以无缝集成您的项目，而不必担心标准库（go net）引入的协程压力。与go net库相比，goev可以在同步I/O方面至少提高20%的性能。此外，与框架内的无锁处理相结合，它提供了更好的优化机会，从而实现更高的整体性能增益。

goev的主要特点包括：
* I/O事件驱动架构
* 轻量级和简约的反应器模式实现，允许多个反应器的灵活组合
* 面向对象的实现，更易于封装业务逻辑
* 支持异步发送，允许高级应用程序执行同步I/O操作，同时异步处理业务处理
* 轮询堆栈中的无锁操作，实现同步I/O的零拷贝数据传输
* 完美支持REUSEPORT多轮询器模式
* 内置四堆计时器实现，实现I/O和计时器事件的无锁/同步处理
* 完全本地实现的接受器/连接器，提供最大的可定制性
* 可控的底层线程数。每个连接每个协程的方法通常会导致线程数激增，但使用轮询器可以保持一致的线程数，将其保持在初始水平
* 垃圾回收（GC）友好，最小化运行时的额外堆内存使用
* 支持应用层与轮询器之间的交互，例如在轮询器协程中创建缓存，实现无锁使用（类似于runtime.mcache）
* API较少，学习成本低

如何使用：
您可以通过以下步骤安装goev：
```
go get github.com/shaovie/goev
```
如果您需要使用goev，可以参考项目中的示例代码。

项目推介：
goev在GitHub上获得了广泛的关注和使用。它的开发活跃度高，已经被许多知名用户和公司使用。此外，它也得到了业内知名人士的推荐。根据我们的测试，goev在同步I/O方面的性能比go net库提高了至少20%，这使得它成为一款非常值得推荐的网络框架。

如果您正在寻找一款高性能、轻量级、非阻塞、I/O事件驱动的网络框架，那么goev绝对是您的不二选择。快来尝试一下吧！

项目链接：https://github.com/shaovie/goev




以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=shaovie/goev&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/shaovie/goev 

开源项目作者：shaovie

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=shaovie/goev)

关注我们，一起探索有意思的开源项目。

