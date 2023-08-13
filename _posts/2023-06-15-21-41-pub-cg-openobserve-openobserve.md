---
layout: post
title: OpenObserve - 一个云原生的观测性平台，Elasticsearch/Splunk/Datadog 的替代产品
tags: All
---

大家好，又见面了，我是 GitHub 精选君！

## 背景介绍

在日志、指标、跟踪和分析领域，我们面临着许多问题，其中核心痛点包括难以操作、高存储成本和低性能。为了解决这些问题，今天要介绍一个名为 OpenObserve 的开源项目。OpenObserve 是一个云原生的观测性平台，专为处理 PB 字节级规模的日志、指标、跟踪和分析而设计。它不仅易于操作，而且能够极大地降低存储成本、提升性能。

openobserve 项目在 GitHub 有超过 3.9k Star，用一句话介绍该项目就是：“🚀 10x easier, 🚀 140x lower storage cost, 🚀 high performance,  🚀 petabyte scale - Elasticsearch/Splunk/Datadog alternative for 🚀 (logs, metrics, traces).”。

## 项目介绍	

OpenObserve是一个可以替代Elasticsearch/Splunk/Datadog的开源项目，它具有以下突出特点：

- 简单易用：与Elasticsearch相比，OpenObserve的操作非常简单，几乎不需要理解和调整大量参数即可快速上手。您只需花费不到2分钟的时间，即可开始使用OpenObserve。

- 降低存储成本：通过使用OpenObserve，您可以将日志存储成本降低约140倍，相比于Elasticsearch，这是一个巨大的节省。

- 高性能：OpenObserve提供高性能的日志、指标和跟踪处理能力，能够处理宠字节级规模的数据，满足大规模应用的需求。

- 丰富的功能：OpenObserve提供了多种功能，包括日志、指标、跟踪的处理、警报和仪表盘等。它还提供了丰富的内置功能，如数据增强、数据脱敏、日志压缩等，无需学习额外的查询语言。

- 开源兼容：OpenObserve是一个开源项目，您可以自由地修改和定制，满足自己的特定需求。

除了以上主要特点外，OpenObserve还具有高可用性和集群支持，可以作为Elasticsearch的替代方案，且不需要单独安装Kibana，OpenObserve提供了自己的用户界面。

以下是 OpenObserve 使用界面。

![](https://raw.githubusercontent.com/openobserve/openobserve/master/./screenshots/zo_home.png)

![](https://raw.githubusercontent.com/openobserve/openobserve/master/./screenshots/logs.webp)

![](https://raw.githubusercontent.com/openobserve/openobserve/master/./screenshots/dashboard.png)

以下是与 Elasticsearch 的对比，在成本上有明显的优势。

![](https://raw.githubusercontent.com/openobserve/openobserve/master/./screenshots/zo_vs_es.png)

## 如何使用

使用OpenObserve非常简单。您可以按照以下步骤安装和使用该项目：

1. 克隆或下载项目代码，并根据文档中的快速入门指南进行配置。
2. 参考文档中的详细说明，了解如何将日志、指标和跟踪数据导入到OpenObserve中，并进行查询和分析。
3. 如果您不想安装OpenObserve，您还可以在OpenObserve Cloud上进行试用，只需花费不到2分钟即可体验OpenObserve的功能。

通过上述步骤，您可以轻松地开始使用OpenObserve。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=openobserve/openobserve&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/openobserve/openobserve 

开源项目作者：openobserve

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=openobserve/openobserve)

关注我们，一起探索有意思的开源项目。

