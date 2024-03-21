---
layout: post
title: 基于 Go/eBPF 的开源云原生负载均衡器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在构建和运行云原生应用的过程中，我们会面临这样的一个挑战，需要跨不同环境（包括本地、公有云或混合的 K8s 环境）实现负载均衡的需求。标准的解决方案可能无法满足性能、灵活性、可定制性和所有 Kubernetes 发行版本/CNI 的兼容性等各方面的需求。

今天要给大家推荐一个 GitHub 开源项目 loxilb-io/loxilb，该项目在 GitHub 有超过 1.1k Star，用一句话介绍该项目就是：“eBPF based cloud-native load-balancer. Powering K8s|Edge|5G|IoT|XaaS Apps.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306230311681.png)

###### 项目介绍

loxilb 是一款基于 GoLang / eBPF 的开源云原生负载均衡器，能实现广泛的 K8S 环境的互通性。loxilb 主要用于提供服务类型的负载均衡，可以根据用户需求在集群内或集群外运行，还支持 cluster-ip 和 node-port 服务，从而为 Kubernetes 提供端到端的连通性。它的性能优于众多竞品，使用了 eBPF 实现了高度的灵活性和可定制性，还提供了高级的服务质量（可分别针对负载均衡器、端点或客户端进行调整）。

![](https://github.com/loxilb-io/loxilb/assets/75648333/6f933bcf-96b7-42ba-bfe2-ea4b85b9a73b)

此外，loxilb 还在 K8s 中启用了对 SCTP 工作负载（带有多主机性）的全面支持，并实现了双堆栈，支持 NAT66、NAT64等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306230341064.png)

###### 如何使用

在 Github 项目页面上提供了详细的文档和讨论，包括如何使用 loxilb。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306230418674.png)

同时，项目还提供了很多的文档用来介绍相关的技术。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306230453698.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=loxilb-io/loxilb&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/loxilb-io/loxilb 

开源项目作者：loxilb-io

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=loxilb-io/loxilb)

关注我们，一起探索有意思的开源项目。

