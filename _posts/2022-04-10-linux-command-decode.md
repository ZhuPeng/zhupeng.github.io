---
layout: post
title: Linux 系统常用命令行工具详细讲解
tags: Linux
---

大家好。

今天，Linux 为互联网上超过一半的服务器、大多数智能手机（通过建立在 Linux 之上的 Android 系统）以及世界上所有最强大的超级计算机提供支持。

![image-20220410232545795](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220410232545795.png)

Linux 的设计原则有一条是这样介绍的，让每一个程序只做好一件事情。Linux 中有很多只做好一件事情的小程序，通过集中精力应对单一任务，程序可以减少冗余代码，从而避免过高的开销、不必要的复杂性和缺乏灵活性。

其中 Linux 基本的命令行工具（ls、cp、rm 等等）都是 GNU coreutils 工具包提供的，而这里面的很多工具都是在践行只做好一件事情的原则，通过组合这些工具可以做非常多的事情。如果你能够仔细去研究上述这些工具，一定能够发现很多有趣的设计和知识。

![coreutils brought to you by the GNU project](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_gnu.decode.linux.cmd.png)

今天要推荐一个网站，这个网站是对 GNU coreutils 工具包的详细介绍，逐一分析其中近 100 个工具的内部实现。

该网站并不是一个用户手册，如果你想知道具体命令怎么使用，使用 man 命令就可以很轻松的知道。这个网站是你想去了解某个工具的源码实现过程中的辅助手册，能够帮助你更好的了解对应工具的设计背景。

比如大部分工具的基础设计如下：

![General CLI procedure](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_general_cli_utility.png)

对应具体的命令 kill 来说，它的设计是这样的：

![l](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_kill_cli_utility.png)

以上都是该网站中包含的内容，非常详尽的介绍超过 100 个工具的内部实现。目录如下图，有没有你想了解的命令呢？

![image-20220410233410371](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220410233410371.png)

更多项目详情请查看如下链接。

网站地址：http://www.maizure.org/projects/decoded-gnu-coreutils/index.html
