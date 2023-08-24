---
layout: post
title: DevPod - 为你提供可定制的开发环境
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在开发过程中，我们经常会面临创建和管理可复现的开发环境的挑战。无论是在本地机器、Kubernetes 集群、远程服务器还是云上的虚拟机中，为了满足项目的需求，我们需要构建适合的开发环境。然而，这样的环境配置往往复杂，而且不同的后端环境需要不同的配置方式。为了解决这个问题，我们希望有一个开源的工具，能够根据统一的配置文件，在任何后端环境中创建可复现的开发环境。

今天要给大家推荐一个 GitHub 开源项目 loft-sh/devpod，该项目在 GitHub 有超过 2.6k Star，用一句话介绍该项目就是：“Codespaces but open-source, client-only and unopinionated: Works with any IDE and lets you use any cloud, kubernetes or just on localhost docker.”。

![](https://raw.githubusercontent.com/loft-sh/devpod/master/docs/static/media/devpod.png)

![](https://raw.githubusercontent.com/loft-sh/devpod/master/docs/static/media/codespaces-but.png)

###### 项目介绍

DevPod 是一个基于 devcontainer (https://containers.dev/) 的客户端工具，用于创建可复现的开发环境。每个开发环境都在容器中运行，并通过 devcontainer 文件进行配置。通过 DevPod，这些开发环境可以在任何后端环境中创建，例如本地计算机、Kubernetes 集群、可访问的远程机器或云中的虚拟机。你可以将 DevPod 视为将你的本地 IDE 与你想要开发的机器连接在一起的粘合剂。因此，根据项目的需求，你可以在本地计算机、配置强大的云计算机或其他远程计算机上创建工作区。在 DevPod 中，每个工作区都以相同的方式进行管理，这也使得在不同工作区之间切换变得非常容易。

![](https://raw.githubusercontent.com/loft-sh/devpod/master/docs/static/media/devpod-flow.gif)

DevPod 的主要特点包括：
- **灵活的配置**: DevPod 使用 devcontainer 文件进行配置，可以满足各种不同的项目需求。
- **跨平台支持**: DevPod 可在任何操作系统上运行，并与任何 IDE 兼容，为开发人员提供便捷的开发环境。
- **容器化开发**: 每个开发环境都在容器中运行，隔离和保护了开发环境，同时提供了一致的开发体验。

###### 如何使用

使用 DevPod 很简单。首先，你需要安装 DevPod Desktop，可以从以下方式下载适用于不同操作系统的安装包：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230812235844997.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=loft-sh/devpod&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/loft-sh/devpod 

开源项目作者：loft-sh

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=loft-sh/devpod)

关注我们，一起探索有意思的开源项目。

