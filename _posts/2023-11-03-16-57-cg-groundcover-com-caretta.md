---
layout: post
title: GitHub 开源项目 groundcover-com/caretta 介绍，Instant K8s service dependency map, right to your Grafana.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 groundcover-com/caretta，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“Instant K8s service dependency map, right to your Grafana.”。


![](https://raw.githubusercontent.com/groundcover-com/caretta/master/images/logo.svg)
![](https://raw.githubusercontent.com/groundcover-com/caretta/master/images/caretta.gif)



背景介绍：
随着 Kubernetes 的广泛应用，对 Kubernetes 集群中微服务的管理和监控需要更高效的工具。传统的分析工具需要手动配置，有时对系统的资源占用过大，不仅耗时，而且可能影响系统性能。而我们等待的，是一款能够实时生成 Kubernetes 服务依赖图的工具，它需要能轻松地集成到 Grafana，同时对系统资源的占用尽可能的小。Caretta 实现了这些需求，而且还具备独特的设计理念。

项目介绍：
Caretta 是一款轻量级的独立工具，能够快速创建出 Kubernetes 集群中运行服务的视觉网络地图。它紧密地依赖 eBPF ，使得你可以高效地映射出 Kubernetes 集群中所有服务网络交互的地图，然后使用 Grafana 来查询和可视化所收集到的数据。Caretta 旨在高效，对系统资源的占用尽可能小，并且不需要对集群进行任何修改。

如何使用：
使用 Helm 图表就可以简单地安装 Caretta。推荐在一个新的，唯一的命名空间中安装 Caretta。
```bash
helm repo add groundcover https://helm.groundcover.com/
helm repo update
helm install caretta --namespace caretta --create-namespace groundcover/caretta
```
在安装过程中还可以通过 Helm 修改 Caretta 的配置。例如，使用以下配置文件，可以设置数据拉取间隔，设置需要容忍的节点，以及是否开启持久化存储：
```yaml
pollIntervalSeconds: 15

tolerations:
- key: node-role.kubernetes.io/control-plane
    operator: Exists
    effect: NoSchedule

victoria-metrics-single:
  server:
    persistentVolume:
      enabled: true
```
如果你想要卸载 Caretta ，只需要删除 Helm 发布就可以了:
```bash
helm delete caretta --namespace caretta
```

项目推介：
Caretta 是由 groundcover 匿名开发并维护的，虽然他们并非知名开发者，但是他们的稳定贡献和认真态度使得该项目非常值得我们的关注和尝试。作为 Kubernetes 服务的可视化地图工具，Caretta 的开发思路和身临其境的用户体验使得该项目在同类开源项目中独树一帜。Caretta 还能通过 Grafana 来查询和可视化所收集到的数据，这一功能对于需要在 Grafana 中集成 Kubernetes 服务依赖的使用者来说尤为重要。在此，我强烈推荐你尝试一下 Caretta，可能它正是你一直在寻找的优秀的 Kubernetes 服务依赖地图工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=groundcover-com/caretta&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/groundcover-com/caretta 

开源项目作者：groundcover-com

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=groundcover-com/caretta)

关注我们，一起探索有意思的开源项目。

