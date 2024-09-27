---
layout: post
title: GitHub 开源项目 thanos-io/thanos 介绍，Highly available Prometheus setup with long term storage capabilities. A CNCF Incubating project.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 thanos-io/thanos，该项目在 GitHub 有超过 13.0k Star。

![](https://stats.deeptrain.net/repo/thanos-io/thanos/?theme=light)

一句话介绍该项目：Highly available Prometheus setup with long term storage capabilities. A CNCF Incubating project.




![Sidecar](https://docs.google.com/drawings/d/e/2PACX-1vSJd32gPh8-MC5Ko0-P-v1KQ0Xnxa0qmsVXowtkwVGlczGfVW-Vd415Y6F129zvh3y0vHLBZcJeZEoz/pub?w=960&h=720)

![Receive](https://docs.google.com/drawings/d/e/2PACX-1vRdYP__uDuygGR5ym1dxBzU6LEx5v7Rs1cAUKPsl5BZrRGVl5YIj5lsD_FOljeIVOGWatdAI9pazbCP/pub?w=960&h=720)

![](https://raw.githubusercontent.com/thanos-io/thanos/master/docs/img/Thanos-logo_fullmedium.png)


###### 项目介绍

在当今的互联网技术环境中，随着数据量的激增，以及对数据处理和监控的需求日益增加，Prometheus 作为一款开源系统监控和警报工具，已经被广泛应用于各种规模的企业中。然而，Prometheus 在处理长期存储、高可用性和大规模数据集时仍面临一些挑战。例如，它默认不支持长期数据存储，而且在多个 Prometheus 实例之间进行数据聚合和去重也相对复杂，这些问题极大地限制了 Prometheus 的应用场景和效率。

针对上述问题，《Thanos》项目应运而生。Thanos 是一组组件，可以组合成一个高可用的指标系统，具有无限存储能力，可以无缝地添加到现有的 Prometheus 部署之上。作为一个 CNCF 孵化项目，Thanos 利用 Prometheus 2.0 存储格式，在任何对象存储中成本有效地存储历史度量数据，同时保持快速的查询延迟。此外，Thanos 提供了一个全局查询视图，能够跨所有 Prometheus 安装实例查询，并能即时合并来自 Prometheus HA 对的数据。

主要特点包括：
- 跨所有连接的 Prometheus 服务器的全局查询视图
- 来自 Prometheus HA 对的度量数据的去重复和合并
- 与现有 Prometheus 设置的无缝整合
- 可选依赖任何对象存储
- 降采样历史数据以大幅提速查询
- 跨集群联合
- 容错查询路由
- 简单的 gRPC "Store API"，用于跨所有度量数据的统一数据访问
- 易于集成自定义度量提供者的接点

使用方法简介如下：
- 获取入门请访问官方文档 [Getting Started](https://thanos.io/tip/thanos/getting-started.md/)
- Thanos 需要与 Prometheus 配合使用，并且可以通过 Docker 来部署 Thanos 组件，例如使用 Thanos Sidecar 与 Prometheus 实例相连接，实现数据的长期存储。

推荐理由：
Thanos 项目是一个活跃的开源项目，持续获得社区和贡献者的支持。它不仅解决了 Prometheus 在规模扩展、长期存储和高可用性方面的挑战，还因其设计哲学、易用性和灵活性而受到业内的高度评价。目前，多家知名公司和组织已经采用 Thanos，来优化他们的监控系统。此外，作为 CNCF 的孵化项目，Thanos 证明了其在云原生生态系统中的重要地位和未来增长的潜力。

总的来说，如果您正在寻找一种高效、可靠的方法来扩展您的 Prometheus 设置，实现长期存储和全球视图查询，那么 Thanos 绝对值得您的考虑。随着其社区的不断成长和技术的不断进步，Thanos 将继续为开源监控领域贡献力量。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=thanos-io/thanos&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/thanos-io/thanos 

开源项目作者：thanos-io

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=thanos-io/thanos)

关注我们，一起探索有意思的开源项目。

