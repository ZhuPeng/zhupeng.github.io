---
layout: post
title: 可定制的音频控制面板，让你的电脑使用体验更酷
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### **背景介绍**

在我们的日常电脑工作和娱乐时间里，经常可能会同时运行着音乐播放器、游戏和语音聊天等多个应用程序。这就可能会导致一个问题：正在玩游戏或者进行其他工作时，你可能听到音乐或者聊天音量太大或太小。然而，调整每个应用程序的音量通常需要切换到该应用程序，这可能会打断我们正在做的事情，使体验变得不那么顺畅。

今天要给大家推荐一个 GitHub 开源项目 omriharel/deej，该项目在 GitHub 有超过 4.1k Star，一句话介绍该项目：Set app volumes with real sliders! deej is an Arduino & Go project to let you build your own hardware mixer for Windows and Linux

![](https://raw.githubusercontent.com/omriharel/deej/master/assets/build-3d-annotated.png)

###### 项目介绍

`deej` 是一个开源的硬件音量混频器项目，支持 Windows 和 Linux 操作系统。它可以让你像 DJ 一样使用现实中的滑块无缝控制不同应用的音量。这样，你就可以在不中断当前操作的情况下，轻松调整不同应用程序的音量了。

你可以将应用程序绑定到不同的滑动器上，并且可以绑定多个应用程序到同一个滑动器上，比如，你可以将所有的游戏都绑定到同一个滑动器上。此外，你甚至还可以控制你的麦克风输入级别。

![](https://raw.githubusercontent.com/omriharel/deej/master/assets/schematic.png)

`deej` 由两部分组成：一部分是在 Go 语言中编写的轻量级桌面客户端；另一部分是一个基于 Arduino 的硬件设备，设备上有 5 个（当然也可以更多）根据你的需求连接到 Arduino 的模拟引脚上的滑动器。

###### 如何使用

对于硬件部分，你只需按照提供的原理图连接滑动器和 Arduino 板。
软件部分包括在 Arduino 板上运行的 C 程序，以及在电脑后台运行的 Go 客户端。C 程序会不断通过串行接口写入当前滑动器的值，Go客户端会读取串行流并根据给定的配置文件调整应用音量。 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240418225837191.png)

###### 项目推介

`deej` 项目在 Github 上已经获得了 4000 多个 star，说明了它的热度和用户认可度。该项目的作者 Omri Harel 是一位有经验和热情的开发者，提交代码的频率保持在一个较高的水平，说明这个项目正在积极更新和维护。因此，这就值得你一试，定制你自己的混音面板，用更酷的方式来控制你的电脑声音。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=omriharel/deej&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/omriharel/deej 

开源项目作者：omriharel

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=omriharel/deej)

关注我们，一起探索有意思的开源项目。

