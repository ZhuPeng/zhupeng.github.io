---
layout: post
title: S.A.T.U.R.D.A.Y - 构建优雅语音接口的工具箱
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代科幻电影中，我们经常看到能够与人类进行交流的智能语音助手。然而，在现实世界中，要构建一个功能强大、自定义的语音接口是一项具有挑战性的任务。S.A.T.U.R.D.A.Y 的目标就是解决这个问题，它为您提供了构建优雅语音接口的工具，以便与现代语言模型进行交互。该项目旨在建立一个志同道合的社区，共同实现电影中承诺给我们的技术。S.A.T.U.R.D.A.Y 设计高度模块化和灵活，同时与特定的 AI 模型解耦，以便在发布新的 AI 技术时无缝升级。

今天要给大家推荐一个 GitHub 开源项目 GRVYDEV/S.A.T.U.R.D.A.Y，该项目在 GitHub 有超过 433 Star，用一句话介绍该项目就是：“A toolbox for working with WebRTC, Audio and AI”。

![](https://raw.githubusercontent.com/GRVYDEV/S.A.T.U.R.D.A.Y/master/images/sat-logo.png)

###### 项目详情

S.A.T.U.R.D.A.Y 是一个用于处理 WebRTC、音频和人工智能的工具箱。通过使用 Pion、whisper.cpp 和 Coqui TTS，您可以构建自己的个人托管 J.A.R.V.I.S，为您的应用程序提供强大的语音计算功能。S.A.T.U.R.D.A.Y 由多个工具组成，每个工具都是语音计算栈中的一个特定部分。主要包括两种构造：

- **引擎**：引擎封装了工具的领域特定功能。不论使用哪种推理后端，该逻辑都保持不变。例如，在 STT（语音转文本）工具的情况下，引擎包含了语音活动检测算法以及一些自定义的缓冲逻辑。这样一来，在不需要重新编写代码的情况下，可以轻松更换后端。
- **后端**：后端实际上是运行 AI 推理的组件。通常是一个薄包装，但它提供了更大的灵活性和升级便利性。后端还可以编写为与 HTTP 服务器进行交互，以便轻松实现语言间的互操作性。

![](https://raw.githubusercontent.com/GRVYDEV/S.A.T.U.R.D.A.Y/master/images/demo-arch.png)

S.A.T.U.R.D.A.Y 包含三种主要类型的工具：STT（语音转文本）、TTT（文本转文本）和TTS（文本转语音）。

- **STT（Speech-to-Text）**：STT 工具是系统的听觉部分，对传入的音频进行语音转文本推理。
- **TTT（Text-to-Text）**：TTT 工具是系统的核心部分，一旦音频被转换为文本，就执行文本转文本推理。
- **TTS（Text-to-Speech）**：TTS 工具是系统的发声部分，对 TTT 工具提供的文本进行文本转语音推理。

###### 开始使用

要基于该项目搭建一个 DEMO，需要首先安装如下工具 Golang、Python、Make 和一个 C 编译器。另外基于项目的架构，需要搭建一个 RTC Server，以及对应的 Client，编译和安装流程参考如下图：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230814225136677.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230814225147408.png)

以下是该项目的 RoadMap，后续会支持本地推理（网络较差的情况下）、更易于使用、更多的项目功能迭代。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230814224945938.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=GRVYDEV/S.A.T.U.R.D.A.Y&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/GRVYDEV/S.A.T.U.R.D.A.Y 

开源项目作者：GRVYDEV

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=GRVYDEV/S.A.T.U.R.D.A.Y)

关注我们，一起探索有意思的开源项目。

