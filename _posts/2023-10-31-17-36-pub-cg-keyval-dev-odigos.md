---
layout: post
title: Odigos - 一个能够无需改动代码为任何应用程序生成分布式追踪的工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常开发过程中，我们经常会遇到需要对应用程序进行分布式追踪的需求，但是这往往需要对代码进行改动，这无疑会增加开发的复杂性和工作量。特别是对于 Go 等编译型语言，无需代码改动的自动化工具更是少之又少。同时，我们还需要将收集到的数据与现有的观察工具进行整合，这也是一项繁琐的工作。

今天要给大家推荐一个 GitHub 开源项目 keyval-dev/odigos，该项目在 GitHub 有超过 1.9k Star，用一句话介绍该项目就是：“Distributed tracing without code changes. Instantly monitor any application using OpenTelemetry and eBPF”。

![](https://raw.githubusercontent.com/keyval-dev/odigos/master/assets/logo.png)

###### 项目介绍

Odigos 是一个能够无需改动代码就能为任何应用程序生成分布式追踪的工具，它支持 Java、Python、.NET、Node.js 和 Go 等语言编写的应用程序。Odigos 通过独特地利用 eBPF 来解决编译型语言如 Go 的自动化工具缺乏的问题。此外，Odigos 还支持所有流行的托管和开源目标，可以将数据生成为 OpenTelemetry 格式，与任何支持 OTLP 的观察工具一起使用。Odigos 还能根据观察数据量自动调整 OpenTelemetry 收集器的规模，并通过方便的 web UI 管理和配置收集器。

以下是部分 Odigos 的是用页面：

1、支持任意语言编写的服务

![](https://raw.githubusercontent.com/keyval-dev/odigos/master/assets/choose_apps.png)

2、监控数据支撑多达 17 种目标源

![](https://raw.githubusercontent.com/keyval-dev/odigos/master/assets/choose_dest.png)

3、数据收集器配置

![](https://raw.githubusercontent.com/keyval-dev/odigos/master/assets/overview_page.png)

###### 如何使用

安装 Odigos 非常简单，只需下载 CLI 并运行以下命令：

```
odigos install
```
安装过程不到 5 分钟，无需进行任何代码更改。使用 odigos ui 命令即可查看 Odigos 的 WebUI。

默认的访问地址为：[http://localhost:3000](http://localhost:3000/)

###### 项目推介

Odigos 支持的目标包括 New Relic、Datadog、Grafana Cloud、Honeycomb 等知名的托管服务，以及 Prometheus、Tempo、Loki、Jaeger 等开源服务，这使得 Odigos 可以适应各种不同的使用场景。如果你在寻找一个无需改动代码就能进行分布式追踪的工具，Odigos 无疑是一个值得尝试的选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=keyval-dev/odigos&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/keyval-dev/odigos 

开源项目作者：keyval-dev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=keyval-dev/odigos)

关注我们，一起探索有意思的开源项目。

