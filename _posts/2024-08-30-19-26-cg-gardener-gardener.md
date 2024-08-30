---
layout: post
title: GitHub 开源项目 gardener/gardener 介绍，Homogeneous Kubernetes clusters at scale on any infrastructure using hosted control planes.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 gardener/gardener，该项目在 GitHub 有超过 2.8k Star。

![](https://stats.deeptrain.net/repo/gardener/gardener/?theme=light)

一句话介绍该项目：Homogeneous Kubernetes clusters at scale on any infrastructure using hosted control planes.




![Gardener Logo](https://raw.githubusercontent.com/gardener/gardener/master/logo/gardener-large.png)

![Gardener v1.30 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.30%20AWS/tests_status?style=svg)

![Gardener v1.29 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.29%20AWS/tests_status?style=svg)

![Gardener v1.28 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.28%20AWS/tests_status?style=svg)

![Gardener v1.27 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.27%20AWS/tests_status?style=svg)

![Gardener v1.26 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.27%20AWS/tests_status?style=svg)

![Gardener v1.25 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.25%20AWS/tests_status?style=svg)

![Gardener v1.30 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.30%20Azure/tests_status?style=svg)

![Gardener v1.29 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.29%20Azure/tests_status?style=svg)

![Gardener v1.28 Conformance Tests](https://testgrid.k8s.io/q/summary/conformance-gardener/Gardener,%20v1.28%20Azure/tests_status?style=svg)


###### 项目介绍

### 背景介绍

在快速演进的云计算时代，容器技术和 Kubernetes 已经成为了微服务架构的核心。然而，在多种云服务商或自建设施上部署和管理统一且规模化的 Kubernetes 集群仍然是一个充满挑战的任务。企业和开发者面临的核心痛点包括如何确保集群在不同环境中的一致性、如何高效管理集群的日常维护任务（如升级、扩缩容、备份恢复等），以及如何最大程度地减少运营成本。这些问题需要一个全面且易于扩展的解决方案来应对。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-468ab34adcfa0a64a866f25da40c06b4.png)

项目介绍

[Gardener](https://github.com/gardener/gardener) 是一个开源项目，旨在通过托管控制平面来实现在任何基础设施上规模化部署同质化 Kubernetes 集群。Gardener 实现了 Kubernetes 集群作为服务的自动化管理和操作，并提供了一个完全验证的扩展性框架，可以调整以适应任何程序化的云或基础设施提供商。

项目的关键设计理念是充分利用 Kubernetes 概念完成所有任务，包括通过 K8s 原生 API 创建在所有支持的基础设施上同质化的集群。与 [SIG Cluster Lifecycle](https://github.com/kubernetes/community/tree/master/sig-cluster-lifecycle) 的 [Cluster API](https://github.com/kubernetes-sigs/cluster-api#cluster-api) 不同，Gardener 的 Cluster API 不仅统一了集群的获取方式，还统一了集群本身的构成，确保了在所有支持的基础设施上提供完全相同配置和行为的集群。

### 如何使用

安装和使用 Gardener 的过程主要包括在现有的 Kubernetes 集群中引入 Gardener 扩展 API 服务器及其定制控制器。用户需要准备一个 Kubernetes 集群用作**园区（Garden）**集群，并在此基础上通过 Gardener 的 [declarative cluster specifications](https://github.com/gardener/gardener/blob/master/example/90-shoot.yaml) 描述和管理最终用户的 Kubernetes 集群（即**射击（Shoot）**集群）。以下是一个快速开始的示例：

1. 克隆 Gardener GitHub 仓库：
   ```bash
   git clone https://github.com/gardener/gardener.git
   ```

2. 遵循仓库中的安装指南和示例配置准备你的园区（Garden）集群和种子（Seed）集群。

3. 使用示例射击（Shoot）集群的 YAML 文件来部署你的 Kubernetes 集群。

### 项目推介

Gardener 不仅通过其创新的架构设计（如托管控制平面）在社区中获得了广泛的认可，也通过持续参与 [Certified Kubernetes Conformance Program](https://www.cncf.io/certification/software-conformance/) 确保了与 Kubernetes 标准的一致性。当前，Gardener 已经通过了 Kubernetes v1.30 版本的认证，彰显了其在兼容性和稳定性方面的承诺。

项目由一个活跃的开源社区支持，并且得到了包括自主云和多家知名公司在内的广泛应用。资源丰富的 [Gardener Wiki](https://github.com/gardener/gardener/blob/master/docs/concepts/architecture.md) 和 [kubernetes.io](https://kubernetes.io/blog/2018/05/17/gardener) 的博文深入介绍了 Gardener 的架构和

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gardener/gardener&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/gardener/gardener 

开源项目作者：gardener

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gardener/gardener)

关注我们，一起探索有意思的开源项目。

