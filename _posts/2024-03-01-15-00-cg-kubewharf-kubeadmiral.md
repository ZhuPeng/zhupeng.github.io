---
layout: post
title: GitHub 开源项目 kubewharf/kubeadmiral 介绍，Multi-Cluster Kubernetes Orchestration
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 kubewharf/kubeadmiral，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Multi-Cluster Kubernetes Orchestration”。



![](https://raw.githubusercontent.com/kubewharf/kubeadmiral/master/./docs/images/arch.png)



作为一名工程师，我们经常会遇到跨多个 Kubernetes 集群进行资源管理的问题。这是一个常见而又困扰许多工程师的问题。传统的 Kubernetes Federation v2 让我们可以通过联合类型像 FederatedDeployment、FederatedReplicaSet、FederatedSecret 等来管理多集群的 K8s 资源。但是，这其中仍然存在诸多局限性，例如 API 的不兼容性、资源管理能力有限等问题。

针对这些问题，我为您推荐一个 kubewharf 的开源项目： KubeAdmiral。

这是一个适用于 Kubernetes 的多集群管理系统。它在 Kubernetes Federation v2 的基础上进行了发展，还扩展了 Kubernetes Federation v2 的 API，并提供了与 Kubernetes 原生 API 的兼容性以及更强大的资源管理能力。

KubeAdmiral 不仅增加了以下新功能：
- 具有丰富的调度插件的新调度框架
- 覆盖策略
- 伴随调度的依赖自动传播
- 成员集群资源的状态汇总
- 可扩展性、稳定性和用户体验的增强

想了解如何使用 KubeAdmiral 吗？你可以参考 [Quickstart](https://github.com/kubewharf/kubeadmiral/blob/main/docs/quickstart.md) 快速入门文档来进行安装与初始化的操作。对于代码示例，你可以直接在项目的 Github 页面找到。 

如今，KubeAdmiral 的活跃状态良好，持续受到来自社区的更新和维护。它的许可证是 Apache 2.0，你可以放心使用。KubeAdmiral 是 Kubernetes Federation v2 的继承者，某些功能依赖于来自 Kubernetes 的原有代码——所有的荣誉都归原始 Kubernetes 作者所有。

如果你有任何问题，欢迎通过 GitHub 问题或 pull 请求进行交流，大家在这里形成一个活跃的开发社区。同时，也欢迎你成为 KubeAdmiral 项目的贡献者。如果有心人士希望参与到这个项目的开发中，可以查阅我们的 [CONTRIBUTING](https://github.com/kubewharf/kubeadmiral/blob/main/CONTRIBUTING.md) 文档。

相信 KubeAdmiral 能解决你在多集群 Kubernetes 管理上的困扰！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubewharf/kubeadmiral&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubewharf/kubeadmiral 

开源项目作者：kubewharf

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubewharf/kubeadmiral)

关注我们，一起探索有意思的开源项目。

