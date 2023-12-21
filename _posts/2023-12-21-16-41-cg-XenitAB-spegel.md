---
layout: post
title: GitHub 开源项目 XenitAB/spegel 介绍，Stateless cluster local OCI registry mirror.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 XenitAB/spegel，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Stateless cluster local OCI registry mirror.”。


![](https://raw.githubusercontent.com/XenitAB/spegel/master/./assets/overview.gif)
![](https://raw.githubusercontent.com/XenitAB/spegel/master/./assets/architecture.jpg)



背景介绍：在使用 Kubernetes 分布式工作负载的过程中，我们常常会遇到一些问题。每个节点在启动前都需要提取工作负载的图像，而运行在一个节点上的每个副本都将产生一个拉取操作。无论是从地理范围内靠近的云服务提供商注册表还是公有注册表，或自承载注册表，图像都可能会被提取。这个过程中的一个问题在于，每个节点都需要分别执行这个操作，这导致了效率低下，也增加了各节点之间的网络压力。

项目介绍：Spegel，瑞典语中的 "镜子"，作为一个无状态的集群本地 OCI 注册表镜像，解决了这个问题。Spegel 的主要功能是允许 Kubernetes 集群中的每个节点充当本地注册表镜像，这样节点之间就可以共享图像。任何一个节点已经提取的图像，其他节点都可以直接拉取。这样既能够减少工作负载启动时间，又减少了出口流量，因为图像将存储在本地集群中。另外，即使外部注册表关闭，新的工作负载也能够继续排期。

如何使用：在安装 Spegel 之前，你可以先查看[兼容性指南](./docs/COMPATIBILITY.md),确认 Spegel 适用于你的 Kubernetes。如果一切正常，最方便的部署 Spegel 的方式就是使用 Helm。

```shell
helm upgrade --create-namespace --namespace spegel --install --version v0.0.16 spegel oci://ghcr.io/xenitab/helm-charts/spegel
```
想了解更多细节的配置文件，可以参考[Helm Chart](./charts/spegel)。

项目推介：无论是你想要从本地缓存提取图像，还是抵抗外部注册表停工时的集群失败，或者是避免从外部注册表提取图像时的频繁限制，甚至在边缘节点部署时提高图像提取效率，Spegel 都是你的首选方案。他针对很多常见问题提供了解决方案，使用简单方便，确实值得推荐。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=XenitAB/spegel&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/XenitAB/spegel 

开源项目作者：XenitAB

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=XenitAB/spegel)

关注我们，一起探索有意思的开源项目。

