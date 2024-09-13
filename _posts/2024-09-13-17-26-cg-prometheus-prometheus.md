---
layout: post
title: GitHub 开源项目 prometheus/prometheus 介绍，The Prometheus monitoring system and time series database.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 prometheus/prometheus，该项目在 GitHub 有超过 54.8k Star。

![](https://stats.deeptrain.net/repo/prometheus/prometheus/?theme=light)

一句话介绍该项目：The Prometheus monitoring system and time series database.




![Docker Repository on Quay](https://quay.io/repository/prometheus/prometheus/status)

![Architecture overview](https://raw.githubusercontent.com/prometheus/prometheus/master/documentation/images/architecture.svg)

![](https://raw.githubusercontent.com/prometheus/prometheus/master//documentation/images/prometheus-logo.svg)


###### 项目介绍

在当今的数字化时代，监控系统的性能、健康状态和运行指标对于确保应用和服务可靠性至关重要。随着微服务架构、云计算和容器技术的兴起，传统的监控解决方案往往难以适应动态扩缩和高度分布式的环境，这就是我们需要一个高度灵活、可扩展并且能够提供即时见解的监控工具的原因。

**Prometheus** 是一个开源的系统监控和时间序列数据库，属于 **Cloud Native Computing Foundation (CNCF)** 的项目之一，旨在解决现代化监控所面临的挑战。它通过采集配置目标的指标、评估规则表达式、显示结果，并在观察到特定条件时触发警报，帮助开发者和运维人员高效地监控和故障排查系统问题。Prometheus 的主要特点包括：

- 多维数据模型，通过指标名和键/值维度集来定义时间序列
- 强大灵活的查询语言 **PromQL**，充分利用这种维度性
- 无需依赖分布式存储，单个服务器节点即可自主运行
- 时间序列采集采取 **HTTP 拉模式**
- 支持通过中间网关批量推送时间序列
- 支持服务发现和静态配置的目标发现
- 提供多种图形和仪表板支持
- 支持层次化和水平化的联合

### 如何安装和使用 Prometheus

#### 使用预编译二进制文件：

1. 访问 [prometheus.io/download/](https://prometheus.io/download/) 获取最新的生产版本二进制文件。
2. 根据 [安装指南](https://prometheus.io/docs/introduction/install/) 完成安装。

#### 使用 Docker：

```bash
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

启动后，Prometheus 将在 `localhost:9090` 上可访问。

#### 从源代码构建：

需要 Go（1.17 或更高版本）、NodeJS（16 或更高版本）和 npm（7 或更高版本）。

```bash
git clone https://github.com/prometheus/prometheus.git
cd prometheus
make build
./prometheus --config.file=your_config.yml
```

以上代码将 Prometheus 从源代码构建并运行起来。

### 为什么选择 Prometheus

Prometheus 不仅因其强大的功能和灵活性受到开源社区的广泛支持，同时也因为其云原生的特性被许多知名公司采用。作为 CNCF 的一部分，它拥有活跃的开发人员社区和稳定的更新周期，保证了项目的长期可持续发展。实际应用案例包括但不限于 SoundCloud、DigitalOcean、Percona 等知名企业，这些成功案例进一步证明了 Prometheus 在业界的领先地位和它对于现代监控解决方案的重要性。

综上所述，不论是您正在寻找一种适应于微服务架构的监控工具，还是需要一个强大的时间序列数据库来帮助您分析和理解数据，Prometheus 都是一个值得考虑的优秀选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=prometheus/prometheus&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/prometheus/prometheus 

开源项目作者：prometheus

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=prometheus/prometheus)

关注我们，一起探索有意思的开源项目。

