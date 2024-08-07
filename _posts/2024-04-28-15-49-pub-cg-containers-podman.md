---
layout: post
title: 非 Docker 无守护进程的容器管理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着容器化技术的兴起，开发和运维人员越来越依赖容器来简化部署流程和实现快速、一致的环境配置。然而，容器管理工具的选择多样且复杂，我们常常面临着容器生命周期管理的挑战、容器网络配置问题以及构建和分享容器镜像的需求。特别是在支持多平台（如 Linux、Mac 和 Windows）和非 root 用户运行容器时，这些问题和需求变得尤为突出。安全性、资源占用以及易用性成为评估容器管理工具时最重要的指标。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240627221837577.png)

今天要给大家推荐一个 GitHub 开源项目 podman，该项目在 GitHub 有超过 22.3k Star，一句话介绍该项目：Podman: A tool for managing OCI containers and pods.


![](https://raw.githubusercontent.com/containers/common/main/logos/podman-logo-full-vert.png)

###### 项目介绍

Podman 是一个全面的容器管理工具，旨在解决 OCI（开放容器倡议）标准容器和容器组的管理问题。作为一个无守护进程、支持多平台的工具，Podman 提供了完整的容器生命周期管理，包括容器的创建、运行、停止以及移除。它还支持容器镜像的全面管理，如拉取、构建、提交和推送到各种存储后端。此外，Podman 在支持无 root 运行容器方面做了特别的优化，提供了用户级别的命名空间隔离，增强了容器的安全性和隔离性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502220309695.png)

Podman 继承了 `libpod` 库，这是一个提供容器生命周期管理 API 的库，包含了容器、容器组、容器镜像和卷的管理。与 Docker 不同，Podman 不依赖于守护进程，这减少了在空闲时的资源消耗并增强了系统的安全性。Podman 之间可以互相通信，提供了 Docker 兼容的 CLI 和 REST API，支持跨平台运行，并且可以在无 root 权限下运行。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502220342201.png)

###### 如何使用

首先，需要从官方页面或 GitHub 获取 Podman 的安装包，并根据操作系统进行安装。安装完成后，可以通过命令行界面开始使用 Podman。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502220442297.png)

以下是一些基本的命令示例：

1、拉取一个容器镜像：`podman pull [image_name]`

2、运行一个容器：`podman run -dt [image_name]`

3、列出正在运行的容器：`podman ps`

4、停止一个容器：`podman stop [container_id]`

5、构建一个容器镜像：`podman build -t [tag_name] .`

这些命令提供了日常容器管理工作所需的基本功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240627222131205.png)

###### 项目推介

Podman 自问世以来，因其无守护进程架构、跨平台支持以及高度兼容 Docker 的特性，获得了开发者社区的广泛关注。项目处于活跃开发状态，拥有一个积极的社区，不断有新功能和改进被提交。同时，Podman 因在安全性和易用性方面的努力获得了很高的评价，诸如无需 root 权限运行容器的能力，对开发者和系统管理员来说是巨大的价值。

###### ![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240502220556214.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=containers/podman&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/containers/podman 

开源项目作者：containers

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=containers/podman)

关注我们，一起探索有意思的开源项目。

