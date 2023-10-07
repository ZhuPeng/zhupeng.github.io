---
layout: post
title: GitHub 开源项目 charmbracelet/log 介绍，A minimal, colorful Go logging library 🪵
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/log，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“A minimal, colorful Go logging library 🪵”。


![](https://user-images.githubusercontent.com/25087/219742757-c8afe0d9-608a-4845-a555-ef59c0af9ebc.png)
![](https://vhs.charm.sh/vhs-1wBImk2iSIuiiD7Ib9rufi.gif)
![](https://vhs.charm.sh/vhs-4AeLaEuO3tDbECR1qe9Jvp.gif)
![](https://vhs.charm.sh/vhs-65KIpGw4FTESK0IzkDB9VQ.gif)
![](https://vhs.charm.sh/vhs-3QQdzOW4Zc0bN2tOhAest9.gif)
![](https://vhs.charm.sh/vhs-6oSCJcQ5EmFKKELcskJhLo.gif)
![](https://vhs.charm.sh/vhs-4LXsGvzyH4RdjJaTF4a9MG.gif)
![](https://vhs.charm.sh/vhs-1JgP5ZRL0oXVspeg50CczR.gif)
![](https://vhs.charm.sh/vhs-4nX5I7qHT09aJ2gU7OaGV5.gif)
![](https://vhs.charm.sh/vhs-79YvXcDOsqgHte3bv42UTr.gif)





背景介绍：
在日常的开发工作中，我们经常需要记录程序运行过程中的各种信息，以便于我们了解程序的运行状态，发现并解决问题。然而，标准的日志库通常功能单一，输出格式单调，缺乏人性化的设计，使得我们在查看日志时需要花费大量的时间和精力。因此，我们需要一个功能强大，易于使用，输出格式丰富多彩的日志库，来提高我们的开发效率。

项目介绍：
" Log " 是一个简洁且多彩的 Go 语言日志库。它提供了一个具有多级别、结构化、人类可读的日志记录器，并且 API 使用简单。与标准日志库不同，" Log " 提供了可定制的多彩人类可读日志记录，包括以下特点：
- 使用 Lip Gloss 来样式化和色彩化输出。
- 多彩的、人类可读的格式。
- 能够定制时间戳格式。
- 跳过调用者框架并将函数标记为助手。
- 多级别日志记录。
- 文本、JSON 和 Logfmt 格式化器。
- 在上下文中存储和检索日志记录器。
- 标准日志适配器。

如何使用：
首先，使用 go get 命令下载依赖：
```
go get github.com/charmbracelet/log@latest
```
然后，在你的 Go 文件中导入它：
```
import "github.com/charmbracelet/log"
```
你可以使用 log.Print() 来打印没有级别前缀的消息，或者使用 New() 来创建新的日志记录器。此外，" Log " 提供了多个级别来过滤你的日志，你可以使用 log.SetLevel() 来设置日志级别，或者使用 log.Options{Level: } 来创建具有特定日志级别的新日志记录器。

项目推介：
" Log " 是一个活跃的开源项目，由 Charmbracelet 团队开发和维护。Charmbracelet 是一个知名的开源团队，他们开发的项目广受开发者喜爱。" Log " 项目的设计理念和实现方式都非常出色，无论是对于日志记录的需求，还是对于学习 Go 语言的开发者来说，都是一个非常好的选择。



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=charmbracelet/log&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/log 

开源项目作者：charmbracelet

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=charmbracelet/log)

关注我们，一起探索有意思的开源项目。