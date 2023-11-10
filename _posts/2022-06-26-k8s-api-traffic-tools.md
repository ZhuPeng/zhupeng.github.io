---
layout: post
title: 云原生服务 API 流量可视化工具
tags: 云原生 Kubernetes API
---

大家好。

现在的很多公司都是用云来部署自己的服务了，不让自己的服务只绑定在一个云上，可以让后续自己有更多的选择。现在业界比较火的云原生的概念，就是让服务的部署符合多云部署的条件，而这依赖 Kubernetes 本身包含的一套标准，这样使用云的用户和云厂商能够在统一的标准下合作。

在这样的条件下，今天推荐一个实用的工具 mizu，一款能够轻松查看 Kubernetes 集群内微服务 API 流量走向的可视化工具。

![image-20220626224304758](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220626224304758.png)

以下是具体的使用界面：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_mizu-ui.api.traffic.png)

mizu 和 Kubernetes 之间的关系如下图：

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_Mizu-architecture.png)

**Mizu** 支持很多协议的实时监测，比如：HTTP、gRPC，甚至 Kafka、AMQP (activeMQ / RabbitMQ)、和 Redis 也是支持的。

Mizu 的安装和使用都是无侵入的，安装好后除了看到 API 的请求流量，也能将整个集群的服务依赖图绘制出来。以下就是一个样例：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_mizu-service-map.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/up9inc/mizu

开源项目作者：[up9inc](https://github.com/up9inc)
