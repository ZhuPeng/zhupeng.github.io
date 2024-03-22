---
layout: post
title: GitHub 开源项目 dockur/windows 介绍，Windows in a Docker container.
tags: All
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 dockur/windows，该项目在 GitHub 有超过 5.8k Star，一句话介绍该项目：Windows in a Docker container.




![](https://github.com/dockur/windows/raw/master/.github/logo.png)



在我们的开发过程中，我们可能需要为应用程序在不同的 Windows 系统环境中进行测试，又或者我们可能需要在 Linux 系统上运行一些 Windows 应用。这时，我们常常需要通过虚拟机来实现这个需求，但是这种方法往往设置复杂，占用大量的硬件资源。为了解决这个问题，我们可以使用 dockur/windows（https://github.com/dockur/windows）。 

dockur/windows 项目是一个功能强大的开源项目，它可以让你在 Docker 容器中运行 Windows。这个项目解决了我们在不同操作系统环境中运行和测试应用的问题，其主要的设计要点包括了 ISO 下载器、KVM 加速以及基于 Web 的视图器。 

dockur/windows 的使用方法也非常简单，你只需要通过 docker-compose.yml 或者运行 docker run 命令就可以方便的启动它。启动后，只需要连接到 8006 端口，就可以通过你的网页浏览器查看到完全自动进行的 Windows 安装进程，一旦你看到桌面，你的 Windows 安装就已经准备好了。

同时，dockur/windows 也支持自定义安装的 Windows 版本，你只需要在 compose 文件中添加 VERSION 环境变量就可以选择你想要安装的 Windows 版本，它支持从 Windows XP 到 Windows 11 的各种版本，以及从 Windows Server 2008 到 Windows Server 2022 的各种版本。

总的来说，dockur/windows 是一个非常活跃的开源项目，它已经获得了大量的关注和好评。如果你需要在 Docker 上运行 Windows，而且你希望这个过程简单、快速，而不用担心复杂的设置和硬件资源的问题，那么我强烈推荐你试试 dockur/windows。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dockur/windows&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dockur/windows 

开源项目作者：dockur

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dockur/windows)

关注我们，一起探索有意思的开源项目。

