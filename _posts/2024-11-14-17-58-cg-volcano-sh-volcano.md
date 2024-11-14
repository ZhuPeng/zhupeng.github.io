---
layout: post
title: GitHub 开源项目 volcano-sh/volcano 介绍，A Cloud Native Batch System (Project under CNCF)
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 volcano-sh/volcano，该项目在 GitHub 有超过 4.2k Star。

![](https://stats.deeptrain.net/repo/volcano-sh/volcano/?theme=light)

一句话介绍该项目：A Cloud Native Batch System (Project under CNCF)




![cncf_logo](https://raw.githubusercontent.com/volcano-sh/volcano/master/docs/images/cncf-logo.png)

![volcano](https://raw.githubusercontent.com/volcano-sh/volcano/master/docs/images/volcano-architecture.png)

![](https://raw.githubusercontent.com/volcano-sh/volcano/master/docs/images/volcano-horizontal-color.png)


###### 项目介绍

背景介绍：
在云原生时代，越来越多的企业和研究机构转向 Kubernetes 来管理他们的容器化应用。特别是在面对需要大量计算并且需求多变的批处理和弹性工作负载时，例如机器学习/深度学习、生物信息学/基因组学以及其他“大数据”应用，传统的 Kubernetes 调度系统可能无法满足其复杂性和灵活性上的需求。因此，寻找一个能够提高 Kubernetes 上这类工作负载运行效率和资源利用率的解决方案变得尤为重要。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-e81ba3acc30f73febc95e70544cd3dc5.png)

项目介绍：
[Volcano](https://github.com/volcano-sh/volcano) 是一个基于 Kubernetes 的批处理系统，它为批处理和弹性工作负载提供了一整套机制，适用于多种批处理类应用，包括但不限于机器学习/深度学习、生物信息学/基因组学和其他“大数据”应用。Volcano 整合了诸如 TensorFlow、Spark、Ray、PyTorch、MPI 等通用领域框架，构建于多年运行各类高性能工作负载的经验之上，融合了开源社区最佳的理念和实践。作为一个云原生计算基金会（CNCF）的孵化项目，Volcano 强调高性能、高效率和易用性，为 Kubernetes 环境下运行复杂工作负载提供了强力支持。

如何使用：
要在现有的 Kubernetes 集群上安装 Volcano，可以通过以下步骤执行：
```bash
kubectl apply -f https://raw.githubusercontent.com/volcano-sh/volcano/master/installer/volcano-development.yaml
```
安装完成后，Volcano 将在 `volcano-system` 命名空间下创建必要的资源，使用户能够开始调度自己的批处理和弹性工作负载。

项目推介：
截至 2021 年 6 月，Volcano 已经在全球多个行业得到广泛使用，包括互联网/云计算/金融/制造/医疗等领域。超过 20 家公司或机构不仅是其终端用户，还积极贡献于该项目。数百名贡献者积极参与代码提交、PR 审查、问题讨论、文档更新以及设计提供。包括华为在内的知名公司以及来自世界各地的技术会议也对 Volcano 给予了高度评价。此外，Volcano 作为 CNCF 的孵化项目，代表了其在云原生领域的重要地位和影响力。这些因素共同使得 Volcano 成为 Kubernetes 上运行批处理和弹性工作负载的首选解决方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=volcano-sh/volcano&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/volcano-sh/volcano 

开源项目作者：volcano-sh

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=volcano-sh/volcano)

关注我们，一起探索有意思的开源项目。

