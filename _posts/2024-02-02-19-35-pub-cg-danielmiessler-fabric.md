---
layout: post
title: 使用 AI 不是能力问题，而是一个集成问题
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在 2023 年以来，人们已经看到了大量的 AI 应用程序用于完成各种任务。然而要将这些 AI 应用系统地整合到我们的生活中并不容易。AI 面临的最大问题并不是功能问题，而是集成问题。诸如：管理各种 AI 提示，发现新的 AI 提示等问题

今天要给大家推荐一个 GitHub 开源项目 danielmiessler/fabric，该项目在 GitHub 有超过 2.8k Star，用一句话介绍该项目就是：fabric is an open-source framework for augmenting humans using AI.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311230901767.png)

###### 项目介绍

`fabric` 是一个开源框架，使用 AI 提升人类的能力，它的主要目标是帮助人们收集并将模块化的 AI 功能（此处为提示）集成到日常生活的各个环节中。Fabric 为生活和工作的各种活动准备了模式（提示），包括但不限于从 YouTube 视频和播客中提取最有趣的部分、仅用一个想法就可以用你自己的声音写一篇文章、总结晦涩的学术论文、为写作创作完美匹配的 AI 艺术提示等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311231022435.png)

###### 如何使用

Fabric 提供了三种主要的使用方式。

一是直接使用模式（提示），只需要导航到 `/patterns`目录并开始探索！你可以在任何你有的 AI 应用中使用它们。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311231230730.png)

二是创建你自己的 Fabric Mill（服务器），如果你想拥有自己的 Fabric 服务器，可以参照 `/server/` 目录并用你自己运行的模式设置你自己的 Fabric Mill！然后你可以使用 `/client/standalone_client_examples` 来连接。

![](https://github.com/danielmiessler/fabric/assets/50654/ec3bd9b5-d285-483d-9003-7a8e6d842584)

三是独立客户端（CLI），你可以直接调用模式而无需连接到 Fabric 服务器，使用流模式获得即时的动态结果等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240311231321805.png)

###### 项目推介

作为一款开源人工智能框架，`Fabric` 提供了一个共享和派生的提示的透明、可扩展、可靠的生态系统。它可以让开发人员建立自己的人工智能生态系统，运行自己特定的模式组合，满足特定的使用案例。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=danielmiessler/fabric&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/danielmiessler/fabric 

开源项目作者：danielmiessler

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=danielmiessler/fabric)

关注我们，一起探索有意思的开源项目。

