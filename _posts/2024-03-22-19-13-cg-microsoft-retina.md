---
layout: post
title: GitHub 开源项目 microsoft/retina 介绍，eBPF distributed networking observability tool for Kubernetes
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 microsoft/retina，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目：eBPF distributed networking observability tool for Kubernetes






ecurity](https://retina.sh/docs/security).  
For other concerns or comments, please [email us](mailto:retina@microsoft.com).

---

这款项目名为 “Retina”，由微软主导的开源项目，是一款面向 Kubernetes 的 eBPF 分布式网络可观测工具。

1、背景介绍：于云原生架构中，Kubernetes 已经成为了业界标准。然而，虽然 Kubernetes 提供了丰富的特性，但是网络监控和安全仍然是许多开发者和系统管理员头疼的问题。在微服务架构日益复杂，服务之间网络调用频繁的情况下，对网络的监控和洞察越来越重要，这不仅可以帮助我们排查网络问题，定位故障点，也可以帮助我们发现潜在的安全问题。

2、项目介绍：Retina 是一款云供应商无关、开源的 Kubernetes 网络可观测平台，提供了应用健康、网络健康和安全的集中式监控平台。Retina 收集可定制的遥测信息，可导出到多种存储选择（如 Prometheus，Azure Monitor 和其他供应商）并以各种方式可视化（如 Grafana，Azure Log Analytics，和其他供应商）。主要特点包括：基于高效的 eBPF 技术进行网络观测，运行时和配置均可提供高度定制，提供规范化的 Prometheus 指标，提供详细的数据包捕获等，完全支持 Linux，Windows，Azure Linux 等多种操作系统。

3、如何使用：首先，需要拷贝项目代码库，然后可以使用 Helm 在您的 Kubernetes 集群上安装 Retina。如果你更希望深入理解，Retina 还提供了 CLI 工具，例如你可以通过编译源代码来创建自己的 Retina CLI 工具。除此之外，Retina 也为大家提供了完整的[文档](http://retina.sh)，方便你了解和掌握使用 Retina。

4、项目推介：Retina 是微软主导的开源项目，这不仅保证了项目的开发积极性，也在一定程度上保证了项目的质量和安全性。项目自开源以来，已经得到了许多公司和开发者的关注和使用。此外，Retina 也在业界得到了广泛的认可，其在解决 Kubernetes 网络可观测问题上的实力毋庸置疑。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=microsoft/retina&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/microsoft/retina 

开源项目作者：microsoft

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=microsoft/retina)

关注我们，一起探索有意思的开源项目。

