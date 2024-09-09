---
layout: post
title: 构建简单、高效协同的私有网络工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日益增长的数字化世界中，构建一个安全、高效的网络环境成为了每一个组织和个人的需求。随着远程工作和分布式团队的兴起，这一需求更加迫切。传统的 VPN 解决方案，虽然在一定程度上满足了这种需求，但在配置复杂度、安全性和易用性方面，往往不能完全满足用户的期待。尤其是当涉及到设备间的直接通信和多平台支持时，设置和维护变得异常复杂，影响了效率和用户体验。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-51c5c56ceaaf26aea0197540d9d0f312.png)

今天要给大家推荐一个 GitHub 开源项目 tailscale，该项目在 GitHub 有超过 18.2k Star，一句话介绍该项目：The easiest, most secure way to use WireGuard and 2FA.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240819230218882.png)

###### 项目介绍

Tailscale 基于 `WireGuard ®` 协议，提供了一个私有的网络构建方案，使得创建和管理一个安全、高效的网络变得异常简单。通过 `Tailscale` ，用户可以轻松地在各种设备上建立直接的网络连接，无论这些设备位于何处。不仅如此， `Tailscale` 还内置了两因素认证（2FA），为网络安全层面提供了额外的保障。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510224551789.png)

此外， `Tailscale` 支持各大主流操作系统，包括 Linux、Windows、macOS、iOS 和 Android 设备。这确保了无论是个人用户还是企业用户都能找到适用的解决方案。项目还开源了大部分代码，除了移动平台的 GUI 之外，核心的 `tailscaled` 守护进程和 `tailscale` CLI 工具都可供用户使用和修改。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510224648177.png)

###### 如何使用

首先，用户需在 [pkgs.tailscale.com](https://pkgs.tailscale.com/) 下载适合自己平台的安装包，然后安装即可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510224839037.png)

对于开发者，若希望从源码构建 `Tailscale` ，可以使用最新版本的 Go 语言进行构建：

```bash
go install tailscale.com/cmd/tailscale{,d}

./build_dist.sh tailscale.com/cmd/tailscale
./build_dist.sh tailscale.com/cmd/tailscaled
```

安装后，根据官方文档快速设置你的 `Tailscale` 网络，就可以开始安全、直接的设备间通信了。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510224908887.png)

###### 项目推介

`Tailscale` 团队不仅致力于提供一个高效的网络解决方案，同时也积极地与社区互动，不断地改进和更新项目。`Tailscale` 已经被众多知名公司和组织采用，这得益于其出色的性能、极简的配置以及超强的兼容性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240510225035662.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tailscale/tailscale&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tailscale/tailscale 

开源项目作者：tailscale

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tailscale/tailscale)

关注我们，一起探索有意思的开源项目。

