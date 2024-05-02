---
layout: post
title: 前沿探索，适用于 AI 设备的开源生态系统
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

我们身边的人工智能设备越来越多，如何围绕这种普遍存在的设备构建一个开源生态系统变得尤为重要。尤其是在维护设备功能、隐私保护以及实现设备之间的相互协作等方面，便需要一款能够为我们解决这些问题的开源产品。

今天要给大家推荐一个 GitHub 开源项目 OpenInterpreter/01，该项目在 GitHub 有超过 1.2k Star，一句话介绍该项目：The open-source language model computer


![OI-O1-BannerDemo-2](https://www.openinterpreter.com/OI-O1-BannerDemo-3.jpg)

![](https://github.com/OpenInterpreter/01/assets/63927363/52417006-a2ca-4379-b309-ffee3509f5d4)

###### 项目介绍

The 01 Project 是一个建设 AI 设备开源生态系统的项目。该项目目标是通过建设开放、模块化、免费的旗舰操作系统，如 Rabbit R1, Humane Pin 和 Star Trek computer 等对话设备，来成为旗舰操作系统领域的 GNU/Linux。

该项目主要包含两个部分：软件和硬件。软件部分主要由基于 Python 的代码构成，可以在 Mac OSX 和 Ubuntu 下运行。硬件部分，目前已经支持通过 ESP32 构建的 01 Light 声音接口设备，并且计划将支持能够本地运行所有程序的 01 Heavy 设备。

![](https://github.com/OpenInterpreter/01/assets/63927363/52417006-a2ca-4379-b309-ffee3509f5d4)

###### 如何使用

要使用该项目，我们首先需要从 GitHub 上克隆该项目的仓库，然后在相应的源代码目录下进行操作。在 Mac OSX 环境中，我们首先需要安装 portaudio、ffmpeg 和 cmake 这三个第三方依赖库，然后使用 poetry 安装 Python 的依赖。设置好环境变量后即可运行项目。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240418230331578.png)

对于硬件部分，我们需要参照硬件构建指南来进行硬件的构建。完成硬件构建后，我们还可以通过相应的指南来安装和运行 01 Server，以完成设备的互连。

###### 项目推介

该项目是由开放解释器团队持续开发和维护，该团队一直致力于为开发者和使用者提供优良的开源项目。虽然该项目目前还处于开发阶段，但项目的代码活跃度高，维护者对代码的更新及维护速度都相当快。如果你对人工智能设备感兴趣，或者想要参与到开源项目中，The 01 Project 将是一个不错的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenInterpreter/01&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenInterpreter/01 

开源项目作者：OpenInterpreter

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenInterpreter/01)

关注我们，一起探索有意思的开源项目。

