---
layout: post
title: 云原生毕业项目，事件驱动的资源扩缩容组件
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在实时计算或事件驱动的微服务中，我们常常会遇到一个问题，即如何根据实时任务的数量，动态的分配相关的计算和存储资源。这是一个比较难以解决的问题，因为我们需要实时监控系统的负载并根据实时负载来调整计算资源，这需要有复杂的负载均衡器和资源管理器，对于 Kubernetes（简称 k8s）用户来说，难以实现精细化的、基于事件驱动的自动化扩容。

今天要给大家推荐一个 GitHub 开源项目 kedacore/keda，该项目在 GitHub 有超过 7.4k Star，用一句话介绍该项目就是：“ KEDA is a Kubernetes-based Event Driven Autoscaling component. It provides event driven scale for any container running in Kubernetes ”。

![](https://raw.githubusercontent.com/kedacore/keda/master/images/logos/keda-word-colour.png)

###### 项目介绍

[KEDA](https://github.com/kedacore/keda)（Kubernetes-based Event Driven Autoscaling）是一个基于 Kubernetes 的事件驱动自动化扩容组件。KEDA 提供了细粒度的自动扩容（包括从零开始扩容和缩减到零），适用于任何在 Kubernetes 中运行的容器。 KEDA 可以同时运行在云端和边缘端，并且原生的和 Kubernetes 组件（如 Horizontal Pod Autoscaler）集成。此外，KEDA 没有外部依赖，这极大的简化了使用者的操作。KEDA 已经是云原生计算基金会 (CNCF) 毕业项目。

![](https://raw.githubusercontent.com/kedacore/keda/main/images/logo-cncf.svg)

###### 如何使用

KEDA 提供了多种部署方式，包括 Helm、Operator Hub 和 YAML 文件，用户可以根据自己的实际情况和习惯选择合适的部署方式。以下是一些 QuickStart 指南，你可以通过这些指南来学习如何使用 KEDA：

- RabbitMQ 和 Go 的 QuickStart 链接：https://github.com/kedacore/sample-go-rabbitmq
- Azure Functions 和 Queues 的 QuickStart 链接：https://github.com/kedacore/sample-hello-world-azure-functions
- Azure Functions 和 Kafka on Openshift 4 的 QuickStart 链接：https://github.com/kedacore/sample-azure-functions-on-ocp4
- Azure Storage Queue with ScaledJob 的 QuickStart 链接：https://github.com/kedacore/sample-go-storage-queue

对于一些其他的事件源，你可以在这里（https://github.com/kedacore/samples）找到相关样例。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240229230920123.png)

###### 项目推介

KEDA 是一个非常活跃的开源项目，并且已经成为了 CNCF 毕业项目，这意味着它不仅是一个功能强大，而且是一个成熟稳定的开源项目，许多知名的公司和组织已经在生产环境中使用了 KEDA。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240229230848978.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kedacore/keda&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kedacore/keda 

开源项目作者：kedacore

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kedacore/keda)

关注我们，一起探索有意思的开源项目。

