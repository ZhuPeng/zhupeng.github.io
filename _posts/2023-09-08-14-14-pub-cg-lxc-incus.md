---
layout: post
title: Incus - 一个现代化、安全且强大的 Linux 系统容器和虚拟机管理器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代的 IT 环境中，我们经常会遇到需要管理和运行全套 Linux 系统（比如官方和社区版本的 Ubuntu 镜像）的问题，这包括在容器或虚拟机中运行。同时，我们也需要一个能够在单机到数据中心集群之间进行扩展的解决方案，以便在开发和生产环境中运行工作负载。

今天要给大家推荐一个 GitHub 开源项目 lxc/incus，该项目在 GitHub 有超过 1.0k Star，用一句话介绍该项目就是：“Powerful system container and virtual machine manager ”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231004210241405.png)

###### 项目介绍

Incus 是一个现代化、安全且强大的系统容器和虚拟机管理器。它提供了一个统一的体验，用于在容器或虚拟机中运行和管理完整的 Linux 系统。Incus 支持大量 Linux 发行版的镜像（包括官方的 Ubuntu 镜像和社区提供的镜像），并围绕一个强大且简单的 REST API 构建。你可以轻松地设置一个感觉像小型私有云的系统，以高效的方式运行任何类型的工作负载，同时保持资源的优化。如果你想要容器化不同的环境或运行虚拟机，或者以一种成本效益的方式运行和管理你的基础设施，那么你应该考虑使用 Incus。

###### 如何使用

Incus 项目目前还处于早期阶段，尚未存在任何包或发布版本。对于生产环境，建议你暂时坚持使用 Canonical 的 LXD，直到 Incus 的稳定版本发布。

在保证 Incus 安装安全的方面，你需要考虑以下几点：

1、保持你的操作系统最新并安装所有可用的安全补丁；

2、只使用支持的 Incus 版本；

3、限制对 Incus 守护进程和远程 API 的访问；

4、除非需要，否则不要使用特权容器。如果你使用特权容器，需要采取适当的安全措施；

5、配置你的安全网络。

###### 项目推介

Incus 是 Canonical LXD 的社区分支，这个分支是为了回应 Canonical 从 Linux Containers 社区接管 LXD 项目而创建的。这个分支的主要目标是再次提供一个真正的社区项目，欢迎每个人的贡献，没有任何一个商业实体负责该项目。尽管 Incus 项目目前还处于早期阶段，但它的目标和设计理念值得我们关注和期待。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lxc/incus&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lxc/incus 

开源项目作者：lxc

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lxc/incus)

关注我们，一起探索有意思的开源项目。

