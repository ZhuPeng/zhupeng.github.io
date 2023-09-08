---
layout: post
title: GitHub 开源项目 HavocFramework/Havoc 介绍，The Havoc Framework.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 HavocFramework/Havoc，该项目在 GitHub 有超过 4.8k Star，用一句话介绍该项目就是：“The Havoc Framework.”。


![](https://raw.githubusercontent.com/HavocFramework/Havoc/master/assets/Havoc.png)
![](https://raw.githubusercontent.com/HavocFramework/Havoc/master/assets/Screenshots/FullSessionGraph.jpeg)
![](https://raw.githubusercontent.com/HavocFramework/Havoc/master/assets/Screenshots/MultiUserAgentControl.png)
![](https://raw.githubusercontent.com/HavocFramework/Havoc/master/assets/Screenshots/SessionConsoleHelp.png)







背景介绍：
在当今的网络安全环境中，我们常常会面临各种复杂的攻防挑战。其中，如何在攻击后的阶段进行有效的命令和控制，以及如何灵活地应对各种变化，是我们常常会遇到的问题。这就需要我们有一个现代化、易于改造的后攻击命令和控制框架，而这正是 Havoc 项目所能提供的。

项目介绍：
Havoc 是一个现代化且易于改造的后攻击命令和控制框架，由 @C5pider 创建。它具有以下特点：

1. 客户端：采用 C++ 和 Qt 编写的跨平台用户界面，基于 Dracula 的现代化、暗色主题。
2. Teamserver：采用 Golang 编写，支持多人协作、负载生成（exe/shellcode/dll）、HTTP/HTTPS 监听、可定制的 C2 配置文件以及外部 C2。
3. Demon：Havoc 的旗舰代理，采用 C 和 ASM 编写，支持 Sleep Obfuscation、x64 返回地址欺骗、间接 Syscalls for Nt* APIs、SMB 支持、Token vault、内置的后攻击命令、通过硬件断点修补 Amsi/Etw、代理库加载以及睡眠期间的堆栈复制等功能。
4. 扩展性：支持外部 C2、自定义代理支持（如 Talon）、Python API 以及模块。

如何使用：
Havoc 在 Debian 10/11，Ubuntu 20.04/22.04 和 Kali Linux 上运行良好。建议使用尽可能新的版本以避免问题，需要使用现代版本的 Qt 和 Python 3.10.x 来避免构建问题。具体的安装指南请参考 Wiki 中的 Installation guide。如果遇到问题，可以查看 Known Issues 页面以及 open/closed Issues 列表。

项目推介：
Havoc 项目目前处于早期发布状态，随着框架的成熟，可能会对 API/core 结构进行重大更改。如果你是一名对后攻击命令和控制框架有深入研究的开发者，或者你是一名对网络安全有深入理解的研究者，我强烈推荐你关注和参与到 Havoc 项目中来。你可以通过 Patreon/Github Sponsors 来支持 @C5pider，未来还计划为支持者提供额外的功能，如自定义代理/插件/命令等。同时，你也可以加入官方的 Havoc Discord 来与社区进行交流。





以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=HavocFramework/Havoc&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/HavocFramework/Havoc 

开源项目作者：HavocFramework

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=HavocFramework/Havoc)

关注我们，一起探索有意思的开源项目。

