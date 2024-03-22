---
layout: post
title: GitHub 开源项目 glasskube/glasskube 介绍，🧊 The missing Package Manager for Kubernetes 📦 Featuring a GUI and a CLI. Glasskube packages are dependency aware, GitOps ready and can get automatic updates via a central public package repository.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 glasskube/glasskube，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“🧊 The missing Package Manager for Kubernetes 📦 Featuring a GUI and a CLI. Glasskube packages are dependency aware, GitOps ready and can get automatic updates via a central public package repository.”。



![Glasskube GUI Mockup](https://github.com/glasskube/operator/assets/3041752/71d0da0c-34ac-40b7-8740-bd2a81ca9f07)
![cast](https://github.com/glasskube/glasskube/assets/16959694/f8b936ca-7b58-4e2b-8845-17da089f2384)
![](https://raw.githubusercontent.com/glasskube/.github/main/images/glasskube-logo.png)
![](https://static.scarf.sh/a.png?x-pxid=899d5aee-625c-4345-bad0-713d29caf929)



背景介绍：
在 Kubernetes 的生态环境中，传统的包管理或直接应用 manifest 可能会非常复杂，并不能很好地进行扩展。这种复杂性可能导致安装和升级 Kubernetes 包变得困难，并且难以管理包的依赖关系。此外，对于希望将 GitOps 方法引入其集群的用户，找到能够支持 GitOps 的 Kubernetes 包管理器是一个挑战。

项目介绍：
Glasskube 是 Kubernetes 缺失的包管理器，特色是具有 GUI 和 CLI。Glasskube包括以下几个主要特性：
- 用户友好的 UI和CLI体验：我们剥去了不必要的复杂性，提供了一个简单但强大的用户界面和命令行界面，便于进行包管理。
- 自动化更新：Glasskube 确保您的 Kubernetes 包和应用始终是最新的，最小化了维护的手动努力。
- 依赖关系的认识：我们理解 Kubernetes 包的相互关联性。Glasskube 智能地管理依赖关系。
- 与 ArgoCD 或 Flux 的 GitOps 准备就绪：可无缝地将 Glasskube 集成到您的 GitOps 工作流中，支持像 ArgoCD 或 Flux 这样的流行工具。
- 中央包存储库：在一个中央存储库中跟踪您的所有包，计划支持自定义存储库的功能。

如何使用：
您可以通过 Homebrew 安装 Glasskube：

```bash
brew install glasskube/tap/glasskube
```

安装了 CLI 后，首先需要在集群中安装必要的组件。为此，请运行
```sh
glasskube bootstrap
```

成功启动集群后，您可以启动包管理器UI：

```bash
glasskube serve
```

此命令将在默认浏览器中打开 [`http://localhost:8580`](http://localhost:8580)。恭喜您，现在您可以浏览和安装我们所有可用的包! 🎉

项目推介：
Glasskube 是一个开放源码项目，由一群积极热心的开发者驱动。虽然这个项目依然是年轻的，但它已经被越来越多的企业和个人开发者所接受并使用，包括一些知名的公司。既可以作为生产环境中的包管理器，也可以作为开发或学习 Kubernetes 的良好工具。所以，无论你是 Kubernetes 的初学者，还是经验丰富的开发者，我们都强烈推荐你试试 Glasskube！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=glasskube/glasskube&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/glasskube/glasskube 

开源项目作者：glasskube

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=glasskube/glasskube)

关注我们，一起探索有意思的开源项目。

