---
layout: post
title: GitHub 开源项目 loxilb-io/loxilb 介绍，eBPF based cloud-native load-balancer. Powering K8s|Edge|5G|IoT|XaaS Apps.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 loxilb-io/loxilb，该项目在 GitHub 有超过 1.1k Star，用一句话介绍该项目就是：“eBPF based cloud-native load-balancer. Powering K8s|Edge|5G|IoT|XaaS Apps.”。


![](https://github.com/loxilb-io/loxilb/assets/75648333/6f933bcf-96b7-42ba-bfe2-ea4b85b9a73b)



背景介绍：在构建和运行云原生应用的过程中，我们面临着许多挑战。一个主要的挑战是跨不同环境（包括本地、公有云或混合的 K8s 环境）实现负载均衡的需求。标准的解决方案可能无法满足性能、灵活性、可定制性和所有 Kubernetes 发行版本/CNI 的兼容性等各方面的需求。这就是我们需要 loxilb 这个项目的原因。

项目介绍：[loxilb](https://github.com/loxilb-io/loxilb) 是一款基于 GoLang / eBPF 的开源云原生负载均衡器，能实现跨广泛的 K8s 环境的互通性。loxilb 主要用于提供服务类型的负载均衡，可以根据用户需求在集群内或集群外运行，还支持 cluster-ip 和 node-port 服务，从而为 Kubernetes 提供端到端的连通性。它的性能优于众多竞品，使用了 eBPF 实现了高度的灵活性和可定制性，还提供了高级的服务质量（可分别针对负载均衡器、端点或客户端进行调整）。此外，loxilb 还在 K8s 中启用了对 SCTP 工作负载（带有多主机性）的全面支持，并实现了双堆栈，支持 NAT66、NAT64等。

如何使用：在 Github 项目页面上提供了详细的文档和讨论，包括如何使用 loxilb。首先，你可以访问项目的 [文档](https://loxilb-io.github.io/loxilbdocs/) 来了解更多关于 loxilb 的信息。然后，你可以将 loxilb 安装到 Kubernetes 集群中，开始对负载进行均衡处理。

项目推介：loxilb 项目的开发活跃，目前正被多家知名公司使用。在众多负载均衡器中，loxilb 以其卓越的性能和灵活性引人注目。在各种架构中，它的性能都优于其竞品，具有许多功能和特性。无论是在云环境还是在单机环境中，无论你的需求是什么，都可以轻松地将 loxilb 集成到你的 Kubernetes 集群中，以满足你的负载均衡需求。因此，我强烈推荐你关注并试用 loxilb。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=loxilb-io/loxilb&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/loxilb-io/loxilb 

开源项目作者：loxilb-io

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=loxilb-io/loxilb)

关注我们，一起探索有意思的开源项目。

