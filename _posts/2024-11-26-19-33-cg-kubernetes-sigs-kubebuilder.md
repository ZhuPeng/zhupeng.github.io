---
layout: post
title: GitHub 开源项目 kubernetes-sigs/kubebuilder 介绍，Kubebuilder - SDK for building Kubernetes APIs using CRDs
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 kubernetes-sigs/kubebuilder，该项目在 GitHub 有超过 8.0k Star。

![](https://stats.deeptrain.net/repo/kubernetes-sigs/kubebuilder/?theme=light)

一句话介绍该项目：Kubebuilder - SDK for building Kubernetes APIs using CRDs




![Quick Start](https://raw.githubusercontent.com/kubernetes-sigs/kubebuilder/master/docs/gif/kb-demo.v3.11.1.svg)


###### 项目介绍

### 背景介绍
在云原生时代，Kubernetes 已经成为了容器编排领域的事实标准。随着企业和开发者们越来越多地投入到 Kubernetes 生态中，他们发现需要定制化 Kubernetes 资源和操作来满足特定需求，这就涉及到了 Kubernetes API 的扩展。自定义资源定义（CRD）为扩展 Kubernetes API 提供了可能，但是创建和维护 CRDs 以及相应的控制器并非易事，开发者需要编写大量的模板代码，并理解 Kubernetes 内部的许多复杂机制。这个过程中的高复杂度以及维护成本，是云原生开发的一个核心痛点。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-10454bdff3e886d123ef9775a542d43d.png)

项目介绍
[Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) 是一个开源框架，旨在通过使用自定义资源定义（CRDs）简化 Kubernetes API 的构建过程。它的设计理念与 *Ruby on Rails* 和 *SpringBoot* 等 Web 开发框架类似，通过提供简单的抽象和工具来减少开发者管理的复杂性，从而提高开发速度。借助 Kubebuilder，开发者不需要从头开始，而是可以利用框架提供的库和工具，以及插件体系，来简化 Kubernetes API 的构建和发布过程。它基于广泛使用的 [controller-runtime](https://github.com/kubernetes-sigs/controller-runtime) 和 [controller-tools](https://github.com/kubernetes-sigs/controller-tools) 库开发，并提供了丰富的文档和社区支持资源来帮助开发者。

### 如何使用
安装 Kubebuilder 建议使用发布的版本，可以在其 [发布页面](https://github.com/kubernetes-sigs/kubebuilder/releases) 上找到相关的二进制文件。按照官方 [指南](https://book.kubebuilder.io/quick-start.html#installation) 完成安装后，开发者可以开始创建新的 Kubernetes API 项目：

```bash
kubebuilder init --domain mydomain.org
kubebuilder create api --group webapp --version v1 --kind Guestbook
```

这些命令将初始化一个新的项目，并创建一个名为 `Guestbook` 的自定义资源及其相应的控制器。更多的使用细节，可以参考 [Kubebuilder 书籍](https://book.kubebuilder.io)。

### 项目推介
Kubebuilder 是 Kubernetes 社区广泛认可的工具之一，其活跃的开发状态、丰富的文档资源和友好的社区支持使其成为开发 Kubernetes API 的首选框架。除此之外，它还被许多知名的开源项目采用，例如 Operator SDK 就是基于 Kubebuilder 作为库开发的。不论是 Kubernetes 新手还是有经验的开发者，Kubebuilder 都能大大降低构建和维护自定义 Kubernetes API 的难度，让开发者更加专注于业务逻辑本身。如果你正寻找一种高效、简化的方式来扩展 Kubernetes API，Kubebuilder 绝对值得尝试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubernetes-sigs/kubebuilder&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes-sigs/kubebuilder 

开源项目作者：kubernetes-sigs

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubernetes-sigs/kubebuilder)

关注我们，一起探索有意思的开源项目。

