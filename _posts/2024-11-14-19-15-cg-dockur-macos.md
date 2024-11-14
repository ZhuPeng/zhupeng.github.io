---
layout: post
title: GitHub 开源项目 dockur/macos 介绍，OSX (macOS) inside a Docker container.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 dockur/macos，该项目在 GitHub 有超过 5.3k Star。

![](https://stats.deeptrain.net/repo/dockur/macos/?theme=light)

一句话介绍该项目：OSX (macOS) inside a Docker container.




![](https://github.com/dockur/macos/raw/master/.github/logo.png)


###### 项目介绍

背景介绍：
如今，软件开发和测试环境的构建越来越多样化和复杂化。尤其对于 macOS 开发者而言，他们常常面临着需要在多个版本的 macOS 上测试和开发应用的需求。然而，苹果的硬件并非每个人都能轻易承担，而且在非苹果硬件上安装 macOS 往往伴随着许多限制和困难。团队协作时，保持环境一致性也是一大挑战。这些问题不仅耗费时间，还可能影响到开发效率和软件的质量。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-bf11a00d73ad5e2dc4ebbe2ff464efaa.png)

项目介绍：
为了解决以上问题，《dockur/macos》项目应运而生。这个项目使得在 Docker 容器内运行 macOS 成为可能。它提供了如 KVM 加速、基于 Web 的查看器和自动下载 macOS 的功能。通过这些特性，它提供了一个轻量级、可灵活配置的 macOS 虚拟环境，极大地简化了在多个 macOS 版本上的开发和测试过程。该项目的主要设计要点包括利用 KVM (基于内核的虚拟机) 以提高性能，以及提供 Web 界面访问虚拟机，让用户无需繁琐设置即可开始其 macOS 体验。

如何使用：
《dockur/macos》项目支持 Docker Compose、Docker CLI 和 Kubernetes 多种部署方式，为不同用户的需求提供便捷。例如，通过 Docker Compose 启动 macOS 容器的代码如下：

```yaml
services:
  macos:
    image: dockurr/macos
    container_name: macos
    environment:
      VERSION: "13"
    devices:
      - /dev/kvm
    cap_add:
      - NET_ADMIN
    ports:
      - 8006:8006
      - 5900:5900/tcp
      - 5900:5900/udp
    stop_grace_period: 2m
```

此外，还能通过环境变量定制 macOS 版本、磁盘大小以及 CPU 和内存资源等，使其更贴合个人需求。

项目推介：
《dockur/macos》是开源社区中的一颗新星。其能在 Docker 容器中运行 macOS 这一创新点，已经吸引了许多开发者的关注和使用。该项目以其活跃的开发态势、实用的功能设计，以及对开源社区的积极贡献，被视为一种高效解决多版本 macOS 测试和开发环境构建问题的方案。虽然目前该项目可能还在早期阶段，但其潜力无限，值得每一位 macOS 开发者或爱好者关注。此外，项目的合法性说明和详尽的 FAQ 部分为用户提供了实用的指南和安心的保障。专业人士和业内评论者对该项目的前景持积极态度，认为它能够为 macOS 应用开发的便利性和可访问性带来新的突破。

通过结合现代化的容器技术和用户友好的设计，《dockur/macos》无疑是向所有寻求高效、灵活 macOS 应用开发和测试解决方案的个人和团队发出的一份诚挚邀请。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dockur/macos&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dockur/macos 

开源项目作者：dockur

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dockur/macos)

关注我们，一起探索有意思的开源项目。

