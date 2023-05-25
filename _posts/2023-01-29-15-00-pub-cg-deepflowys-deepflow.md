---
layout: post
title: 面向云原生开发者，基于 eBPF 的应用可观测性平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 deepflowio/deepflow，该项目在 GitHub 有超过 800 Star，用一句话介绍该项目就是：“Application Observability using eBPF”，面向云原生开发者，基于 eBPF 的应用可观测性平台。

![](https://raw.githubusercontent.com/deepflowys/deepflow/master/./docs/deepflow-logo.png)

那么什么是 eBPF 呢，这里简单介绍以下。

> eBPF 是一项革命性的技术，可以在 Linux 内核中运行沙盒程序，而无需更改内核源代码或加载内核模块。通过使 Linux 内核可编程，基础架构软件可以利用现有的层，从而使它们更加智能和功能丰富，而无需继续为系统增加额外的复杂性层。
>
> eBPF 导致了网络，安全性，应用程序配置/跟踪和性能故障排除等领域的新一代工具的开发，这些工具不再依赖现有的内核功能，而是在不影响执行效率或安全性的情况下主动重新编程运行时行为。 

DeepFlow 是一款面向云原生开发者的**高度自动化**的可观测性平台。使用 **eBPF**、WASM、OpenTelemetry 等新技术，DeepFlow 创新的实现了 **AutoTracing**、**AutoMetrics**、**AutoTagging**、**SmartEncoding** 等核心机制，极大的避免了埋点插码，显著的降低了后端数仓的资源开销。基于 DeepFlow 的可编程性和开放接口，开发者可以快速将其融入到自己的可观测性技术栈中。以下是 DeepFlow 与其他上下游系统的关联图，以及 DeepFlow 的系统架构，主要由 Agent 和 Server 两个进程组成。

![](https://raw.githubusercontent.com/deepflowys/deepflow/master/./docs/deepflow-architecture.png)

DeepFlow 有六大特性，包括全栈语言支持、全链路、高性能、可编程、开放接口和易于维护，详情如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230416213658068.png)

DeepFlow 提供三个版本，大家可根据需要按需使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230416213902890.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=deepflowio/deepflow&type=Timeline)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/deepflowio/deepflow

开源项目作者：deepflowys

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=deepflowys/deepflow)



关注我们，一起探索有意思的开源项目。
