---
layout: post
title: 兼容 Docker 的强大容器管理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当前的开发环境中，容器化技术已经成为了软件开发和部署的标准之一。Docker，作为最广泛使用的容器技术之一，大大简化了容器的创建、部署和管理过程。然而，随着容器生态系统的不断成熟，用户和开发人员面临着更多高级功能的需求，如容器的即时拉取、根目录模式运行、P2P 图像分发等，这些在 Docker 中暂时无法实现，或者实现起来极为复杂。但是对于开发者来说，迫切需要更加先进的容器管理解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6433d57f3cc8ef6a99cbf75593956d01.png)

今天要给大家推荐一个 GitHub 开源项目 nerdctl，该项目在 GitHub 有超过 8.2k Star。

![](https://stats.deeptrain.net/repo/containerd/nerdctl/?theme=light)

一句话介绍该项目：contaiNERD CTL - Docker-compatible CLI for containerd, with support for Compose, Rootless, eStargz, OCIcrypt, IPFS

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241124233947108.png)


###### 项目介绍

`nerdctl` 是一个完全兼容 Docker 的命令行接口（CLI），它基于强大的容器运行时 `containerd` 构建，并旨在填补 Docker 在某些高级特性上的空白。`nerdctl` 兼容 Docker 的 UI/UX，让用户无需额外的学习成本就能切换使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241124234101650.png)

除了提供 Docker 的基本功能外，`nerdctl` 还支持 Docker Compose、无根模式运行（rootless mode）、懒拉取镜像（如 Stargz）、加密镜像（ocicrypt）、P2P 镜像分发（IPFS）、以及容器图像签名和验证（cosign）等高级特性。这使 `nerdctl` 成为了一个非常强大的工具，尤其适合寻求在容器管理上实现更高效率和安全性的开发者和企业。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241124234117547.png)

###### 如何使用

通过以下步骤，可以安装和使用 `nerdctl`：

1、安装：用户可以从官方 [GitHub Releases](https://github.com/containerd/nerdctl/releases)下载适用于自己系统的二进制文件。

2、基本使用示例：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241124234222498.png)

###### 项目推介

`nerdctl` 作为 containerd 的官方非核心子项目之一，自发布以来，它就以其丰富的特性和可靠性，吸引了大量的开发者社区的关注和参与。此项目的开发活跃，不仅拥有 containerd 这样强大背书，其功能也在持续地扩张和完善中。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=containerd/nerdctl&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/containerd/nerdctl 

开源项目作者：containerd

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=containerd/nerdctl)

关注我们，一起探索有意思的开源项目。

