---
layout: post
title: GitHub 开源项目 argoproj/argo-rollouts 介绍，Progressive Delivery for Kubernetes
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 argoproj/argo-rollouts，该项目在 GitHub 有超过 2.9k Star。

![](https://stats.deeptrain.net/repo/argoproj/argo-rollouts/?theme=light)

一句话介绍该项目：Progressive Delivery for Kubernetes




![Argo Rollotus Demo](https://img.youtube.com/vi/hIL0E2gLkf8/0.jpg)


###### 项目介绍

**Argo Rollouts：Kubernetes 中的渐进式发布解决方案**

在当今的软件开发生命周期中，持续集成和持续部署（CI/CD）已成为一个核心实践，特别是在使用 Kubernetes 这样的容器编排系统时。然而，尽管 Kubernetes 提供了原生的滚动更新策略以确保更新过程中的服务不中断，但这一策略很难满足现代应用快速迭代和高稳定性的需求。原生滚动更新策略的一些局限性包括：更新速度控制不精细、无法控制新旧版本之间的流量分配、对更新中潜在问题的感知及回滚能力不足等。这些问题在大规模、高容量的生产环境中尤为突出，因为任何一次更新失败的风险都可能导致重大损失。

**Argo Rollouts** 是一款专为 Kubernetes 设计的渐进式发布工具，它通过提供高级部署策略（如蓝绿部署、金丝雀部署）和深度集成服务网格及入口控制器来应对上述挑战。本项目通过一系列自定义资源定义（CRDs）和 Kubernetes 控制器，不仅能够精细控制流量分配，还能根据实时指标自动决策推进或回滚更新，极大地提升了更新的安全性和灵活性。

**如何使用 Argos Rollouts?**

开始使用 Argo Rollouts 十分简单。首先通过以下命令在 Kubernetes 中创建命名空间并部署 Argos Rollouts：

```bash
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
```

接下来，您可以遵循[入门指南](https://argo-rollouts.readthedocs.io/en/stable/)创建和更新 Rollout 对象。文档中有详细的指导，帮助您了解如何配置蓝绿或金丝雀发布策略、如何整合服务网格以及如何设置自动化指标检查等。

**为什么选择 Argo Rollouts?**

Argo Rollouts 提供了诸多 Kubernetes 原生滚动更新所不具备的高级功能，诸如：

- 蓝绿更新策略和金丝雀发布
- 精细的流量权重控制
- 自动回滚和推进支持
- 支持手动判断
- 自定义指标查询和业务 KPI 分析
- 与多种入口控制器和服务网格集成

此外，Argo Rollouts 支持与 **NGINX**、**ALB** 和 **Apache APISIX** 等多种入口控制器集成，还可以与 **Istio**、**Linkerd** 等服务网格，以及 **Prometheus**、**Datadog**、**New Relic** 等指标提供者集成，为您的 Kubernetes 部署提供全面的流量和指标管理能力。

**推荐 Argo Rollouts**

Argo Rollouts 已经被多家知名公司采用，并在社区中获得了极高的评价。无论您是正在寻找一种更安全的 Kubernetes 应用部署方式，还是希望在更新过程中获得更细粒度的流量控制和实时反馈，Argo Rollouts 都能为您提供可靠的解决方案。它的活跃开发社区、丰富的集成选项以及强大的功能使得它成为面向现代 Kubernetes 环境的理想

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=argoproj/argo-rollouts&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/argoproj/argo-rollouts 

开源项目作者：argoproj

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=argoproj/argo-rollouts)

关注我们，一起探索有意思的开源项目。

