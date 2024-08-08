---
layout: post
title: 与 Prometheus 无缝集成的日志收集与检索工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

对于开发人员和系统管理员而言，日志管理和分析是一项绕不开的任务，它对于调试应用、监控系统性能、追踪安全事件等方面都至关重要。然而，随着云原生应用和微服务架构的流行，系统和服务生成的日志量剧增，日志数据的管理和分析变得日益复杂和昂贵。常见的痛点包括日志数据海量而不易搜索、日志存储成本高昂以及难以实现高效的日志监控和分析。

今天要给大家推荐一个 GitHub 开源项目 loki，该项目在 GitHub 有超过 22.9k Star。

![](https://stats.deeptrain.net/repo/grafana/loki/?theme=light)

一句话介绍该项目：Like Prometheus, but for logs.


![](https://raw.githubusercontent.com/grafana/loki/master/docs/sources/logo_and_name.png)


###### 项目介绍

Loki 是一种水平可扩展、高可用、多租户的日志聚合系统，它的设计灵感来源于 Prometheus，旨在提供一种成本效益高且易于操作的日志解决方案。与其他日志聚合系统不同，Loki 不对日志内容进行全文索引，而是索引每个日志流的一组标签，这样既降低了运营成本又简化了操作。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725215112593.png)

Loki 的主要特点包括：

1、使用与 Prometheus 相同的标签索引和分组日志流，使得开发人员可以无缝地在度量指标和日志之间切换，使用相同的标签体系；

2、特别适合存储 Kubernetes Pod 日志，Pod 标签等元数据会被自动抓取和索引；

3、在 Grafana (需要 Grafana v6.0) 中有原生支持，便于查询和展示日志数据。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725215156075.png)

Loki 的日志堆栈由三个组件构成：

1、promtail：负责收集日志并将其发送到 Loki 的代理。

2、loki：主服务器，负责存储日志和处理查询请求。

3、Grafana：用于查询和显示日志的界面。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725215309572.png)

###### 如何使用

Loki 的安装和使用都非常简单。以下是一些基本步骤：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725215426582.png)

###### 项目推介

Loki 已经在开源社区获得广泛的关注和应用，不仅因为其设计上的创新（如与 Prometheus 的紧密集成和对标签的高效使用），还因为 Grafana Labs（Loki 项目的主要维护者）在可视化领域的权威和传统。Loki 适用于各种规模的企业，从小型团队到大型企业，都可以从中受益。目前，许多知名公司和组织已经在使用 Loki 来管理他们的日志数据，不仅因为其出色的性能和易用性，还因为与 Grafana 的无缝集成为日志分析和监控提供了强大的视觉能力。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240725215547118.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=grafana/loki&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/grafana/loki 

开源项目作者：grafana

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=grafana/loki)

关注我们，一起探索有意思的开源项目。

