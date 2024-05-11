---
layout: post
title: 全语言无差别应用性能分析器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在生产级数据中心进行应用性能分析时，实现低开销、高效准确的程序性能分析是个极具挑战的问题。特别是在复杂的服务环境下，需要跨语言、跨系统进行全面的性能剖析，以便于快速准确地定位性能瓶颈。常规的性能分析工具要么侵入性太强、要么难以提供足够深度的信息、要么运行成本过高。在不打扰现有服务运行的前提下，进行细粒度性能分析一直是工程师们面临的一个核心痛点。

今天要给大家推荐一个 GitHub 开源项目 elastic/otel-profiling-agent，该项目在 GitHub 有超过 1.3k Star，一句话介绍该项目：The production-scale datacenter profiler

![](https://raw.githubusercontent.com/elastic/otel-profiling-agent/master/./docs/devfiler.png)

###### 项目介绍

`otel-profiling-agent` 是一个为 Linux 系统设计的跨语言、全系统级性能分析器，通过利用 eBPF 技术，实现了对程序运行时性能的准确分析而又几乎不增加额外开销。这个项目旨在通过 OpenTelemetry 捐赠给开源社区，目前暂时存放于一个临时仓库中。其核心优势包括对 C/C++ 等本地程序的高效支持、底至 1% 的 CPU 和 250MB 的内存上限、对混合运行时栈跟踪的完整支持、以及 100% 的非侵入式设计。此外，它还预备支持 .NET，并且已经支持了如 JVM、Python、Ruby 等多种高级语言，甚至在不需要调试符号的情况下也能进行性能分析。

![](https://raw.githubusercontent.com/elastic/otel-profiling-agent/master/docs/trace-pipe.drawio.svg)

###### 如何使用

使用 `otel-profiling-agent` 非常简单，首先需要通过 Docker 构建环境，然后编译项目：

```sh
make docker-image
make agent
```
编译完成后，你可以这样启动分析器：
```sh
sudo ./otel-profiling-agent -collection-agent=127.0.0.1:11000 -disable-tls
```
此外，项目还提供了一个名为 `devfiler` 的本地数据可视化工具，方便开发者对分析结果进行初步的查看和理解。

###### 项目推介

尽管 `otel-profiling-agent` 目前仍处于捐赠和讨论阶段，不过，其背后的技术、思想以及早期的应用效果已经显示出它成为生产级性能分析工具的潜力和价值。特别是对于追求低侵入性、高精准度和全面性能剖析的复杂系统，`otel-profiling-agent` 提供了一个非常有吸引力的解决方案。其开发背景源于业界领先的 Elastic 公司，而待该项目正式成为 OpenTelemetry 的一部分后，无疑将获得更广泛的社区支持和开发活力。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=elastic/otel-profiling-agent&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/elastic/otel-profiling-agent 

开源项目作者：elastic

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=elastic/otel-profiling-agent)

关注我们，一起探索有意思的开源项目。

