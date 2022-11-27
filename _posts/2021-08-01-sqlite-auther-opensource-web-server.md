---
layout: post
title: SQLite 作者最新开源力作
tags: 其他
---

大家好。

SQLite 大家应该都知道吧，SQLite 是一款轻型的数据库，是遵守 ACID 的关系型数据库管理系统，它包含在一个相对小的C库中。它的设计目标是嵌入式的，而且已经在很多嵌入式产品中使用了它，它占用资源非常的低。

SQLite 的作者是 D. Richard Hipp（理查德希普），作者非常的有个性，用到的软件工具都是自己写，他写了不少工具，比如 SQLite、Bug 追踪系统 CVSTrac、版本管理系统 Fossil。

今天要推荐的就是理查德希普最新开源的 Web 服务器 althttpd，我们可以先来看下这个项目的时间线。

![image-20210801224314018](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210801224314018.png)

可以看出来开源工作是最近才开始的，但是实际上 althttpd 从 2004 年开始就在支撑 https://sqlite.org/ 网站的运行，althttpd 的设计目标就是为了简单、安全同时低资源消耗。在 2018 年，sqlite.org 每天要响应 50 万的 HTTP 请求，而只用了价值 40 美金的服务器，而且服务器处于很低的负载（0.1 或者 0.2），可以看出其性能还是不错的。

我们来看下 althttpd 的代码，项目实际只有一个 c 文件，整体行数也不多，是一个非常不错的学习项目。

![image-20210801224817788](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210801224817788.png)

而且项目中有一个介绍文件 althttpd.md，详细介绍了 althttpd 的设计哲学、项目使用说明等。

![image-20210801225159587](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210801225159587.png)

从 althttpd 的设计哲学可以看出来，作者是一个很克制的人，并不是希望去做一个功能非常丰富的 Web 服务器，而是希望 althttpd 在满足功能要求的前提下，能够尽量保持代码的简洁，这是非常值得我们学习的。

更多项目详情请查看如下链接。

开源项目地址：https://sqlite.org/althttpd/doc/trunk/althttpd.md
