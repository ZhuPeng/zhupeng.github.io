---
layout: post
title: AWS 开源的 Kubernetes 节点自动扩缩容项目
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在多云和自动化技术日益成熟的当下，Kubernetes 作为容器编排的事实标准，其在企业级部署中的地位日益重要。然而，随着集群规模的扩大和应用负载的波动，如何高效、成本友好地管理节点资源成为了运维团队面临的一个重大挑战。传统的节点扩缩容策略往往不能完美适应复杂多变的业务需求，既需保证业务的高可用性，又要避免资源的浪费，这就需要一个更加智能、灵活的解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-a04bc6fad94372db10161ac8279b8e28.png)

今天要给大家推荐一个 GitHub 开源项目 karpenter-provider-aws，该项目在 GitHub 有超过 6.1k Star。

![](https://stats.deeptrain.net/repo/aws/karpenter-provider-aws/?theme=light)

一句话介绍该项目：Karpenter is a Kubernetes Node Autoscaler built for flexibility, performance, and simplicity.


![](https://raw.githubusercontent.com/aws/karpenter-provider-aws/master/website/static/banner.png)


###### 项目介绍

**Karpenter** 是 AWS 开源的一个针对 Kubernetes 的节点自动扩缩容项目，旨在以灵活性、性能和简洁性为核心，提供一个高效且成本优化的节点管理方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618224440839.png)

Karpenter 的工作原理包含如下几个关键步骤：

**1、监控** Kubernetes 调度器标记为不可调度的 Pod。

**2、评估** Pod 请求的调度约束（资源请求、节点选择器、亲和性、容忍度和拓扑扩散约束）。

**3、供应** 满足 Pod 要求的节点。

**4、移除** 不再需要的节点。

通过这种方式，Karpenter 能够优化工作负载在 Kubernetes 集群上的效率和成本。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618224530057.png)

###### 如何使用

安装步骤相对比较繁琐，参考如下文档按步骤操作即可：

```shell
https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618224854609.png)

###### 项目推介

Karpenter 已经成为 Kubernetes 集群管理不可或缺的工具之一，它不仅得到了 AWS 的强力推动，还拥有活跃的开发社区，持续的特性更新和问题解决保障了其前沿性和稳定性。此外，Karpenter 在过去的一些技术会议和社区活动中有着亮眼的表现，如 Kubecon、AWS 容器日等，其实用性、高效性和节省成本的优势得到了业界的广泛认可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618224943804.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=aws/karpenter-provider-aws&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/aws/karpenter-provider-aws 

开源项目作者：aws

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=aws/karpenter-provider-aws)

关注我们，一起探索有意思的开源项目。

