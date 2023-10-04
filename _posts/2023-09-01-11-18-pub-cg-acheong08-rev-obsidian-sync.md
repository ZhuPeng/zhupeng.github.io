---
layout: post
title: 一个逆向工程的 Obsidian 同步和发布服务器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们日常的学习、工作中，经常会使用 Obsidian 这款知识管理工具来记录和整理信息，但是 Obsidian 的同步和发布服务并不是开源的，这就给我们带来了一些问题，比如我们无法自定义同步服务，无法在不同设备间实现实时同步，也无法进行文件历史记录的恢复和快照的获取。这些问题都需要我们去寻找一个解决方案。

今天要给大家推荐一个 GitHub 开源项目 acheong08/rev-obsidian-sync，该项目在 GitHub 有超过 708 Star，用一句话介绍该项目就是：“Reverse engineering of the native Obsidian sync and publish server”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230906232250053.png)

###### 项目介绍

Rev Obsidian Sync 是一个逆向工程的 Obsidian 同步和发布服务器，它并非官方版本，但是它能够解决我们上述提到的问题。该项目具有端到端的加密功能，可以在不同设备间实现实时同步，支持文件历史记录的恢复和快照的获取，同时还支持保险库分享和发布（目前只支持 markdown 格式，尚未支持渲染）。该项目可以在 IOS、Android、Linux、MacOS、Windows 等操作系统上运行。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230906232339819.png)

核心功能如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230906232402842.png)

###### 如何使用

首先，你需要在你的服务器上安装和运行这个项目，你可以通过 Docker 快速启动，也可以通过 git clone 这个项目然后运行主程序。在你完成安装和配置后，你可以通过运行一个命令或者发送一个 POST 请求来添加新用户。如果你需要，你还可以通过设置环境变量来自定义一些参数，比如服务器监听地址、注册 API 的访问权限等。

对应的 Docker Compose 的配置：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230906232539535.png)

添加新用户请求：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230906232609903.png)

###### 项目推介

Rev Obsidian Sync 目前正在活跃开发中，你可以随时关注到最新的开发进展。如果你是一个 Obsidian 的用户，那么这个项目将会是你的一个不错的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=acheong08/rev-obsidian-sync&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/acheong08/rev-obsidian-sync 

开源项目作者：acheong08

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=acheong08/rev-obsidian-sync)

关注我们，一起探索有意思的开源项目。

