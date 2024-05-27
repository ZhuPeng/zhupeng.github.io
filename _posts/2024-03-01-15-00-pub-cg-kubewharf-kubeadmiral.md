---
layout: post
title: 适用于 Kubernetes 的多集群管理系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

作为一名使用 Kubernetes 的工程师，我们经常会遇到跨多个 Kubernetes 集群进行资源管理的问题。这是一个常见而又困扰许多工程师的问题。传统的 Kubernetes Federation v2 让我们可以通过联合类资源 FederatedDeployment、FederatedReplicaSet、FederatedSecret 等来管理多集群的 K8s 资源。但是，这其中仍然存在诸多局限性，例如 API 的不兼容性、资源管理能力有限等问题。

今天要给大家推荐一个 GitHub 开源项目 kubeadmiral，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目：Multi-Cluster Kubernetes Orchestration.

![](https://raw.githubusercontent.com/kubewharf/kubeadmiral/master/./docs/images/arch.png)

###### 项目介绍

KubeAdmiral 是一个适用于 Kubernetes 的多集群管理系统。它在 Kubernetes Federation v2 的基础上进行了扩展，同时还扩展了 Kubernetes Federation v2 的 API，并提供了与 Kubernetes 原生 API 的兼容性以及更强大的资源管理能力。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240515221320574.png)

KubeAdmiral 增加了以下新功能：

1、具有丰富的调度插件的新调度框架

2、覆盖策略

3、伴随调度的依赖自动传播

4、成员集群资源的状态汇总

5、可扩展性、稳定性和用户体验的增强

###### 如何使用

想了解如何使用 KubeAdmiral 可以参考快速入门文档来进行安装与初始化的操作。对于代码示例，你可以直接在项目的 GitHub 页面找到。 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406175758244.png)

###### 项目推介

KubeAdmiral 的开源许可证是 Apache 2.0，你可以放心使用。KubeAdmiral 是 Kubernetes Federation v2 的继承者，相信 能解决你在多集群 Kubernetes 管理上的困扰！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubewharf/kubeadmiral&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubewharf/kubeadmiral 

开源项目作者：kubewharf

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubewharf/kubeadmiral)

关注我们，一起探索有意思的开源项目。

