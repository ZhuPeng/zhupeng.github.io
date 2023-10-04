---
layout: post
title: Capslock - Google 开源 Go 语言软件供应链安全评估工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在开源软件供应链攻击日益增多的背景下，第三方依赖包的安全性备受关注。Capslock 是一个针对 Go 语言包的能力分析命令行工具，通过跟踪调用特权标准库操作来分类 Go 包的能力，告知用户给定包可以访问哪些特权操作。通过 Capslock，用户可以更全面地了解依赖包的权限，从而更好地进行安全评估。


![](https://raw.githubusercontent.com/google/capslock/master/docs/capslock-banner.png)

###### 项目介绍

Capslock 是由 Google 开源，是一个能力分析命令行（CLI）工具，主要用于 Go 语言包的能力分析。Capslock 通过跟踪调用特权标准库操作来分类 Go 包的能力，告知用户给定包可以访问哪些特权操作。Capslock 的主要功能包括：能力分析、权限告警、权限变更告警等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230902200039328.png)

###### 如何使用

用户可以通过以下步骤安装 Capslock：

1、命令行 shell 中运行命令：go install github.com/google/capslock/cmd/capslock@latest

2、在需要分析的包路径下运行命令：capslock

###### 项目推介

Capslock 是由 Google 开发的开源项目，虽然在 GitHub 开源还处于初期阶段，但有大厂背书质量和后续的迭代肯定没有问题。从功能的角度来看，Capslock 可以帮助用户更全面地了解依赖包的权限，从而更好地进行安全评估，是保障软件安全的重要工具，每一个公司都应该重点关注自身软件的安全。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=google/capslock&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/google/capslock 

开源项目作者：google

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=google/capslock)

关注我们，一起探索有意思的开源项目。

