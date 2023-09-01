---
layout: post
title: GitHub 开源项目 ccfos/nightingale 介绍，An enterprise-level cloud-native observability solution, which can be used as drop-in replacement of Prometheus for alerting and Grafana for visualization.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ccfos/nightingale，该项目在 GitHub 有超过 6.9k Star，用一句话介绍该项目就是：“An enterprise-level cloud-native observability solution, which can be used as drop-in replacement of Prometheus for alerting and Grafana for visualization.”。


![](https://raw.githubusercontent.com/ccfos/nightingale/master/doc/img/nightingale_logo_h.png)
![](https://raw.githubusercontent.com/ccfos/nightingale/master/doc/img/arch-product.png)







背景介绍：
在企业级的云原生环境中，我们常常会遇到一些监控问题。例如，我们可能需要使用 Prometheus 进行告警，使用 Grafana 进行可视化，但是这些系统往往是分散的，缺乏一个统一的视图，无法开箱即用。此外，通过修改配置文件来管理 Prometheus 和 Alertmanager 的方式学习曲线较大，难以进行协作。再者，如果数据量过大，可能会面临 Prometheus 集群扩展的问题。这些都是我们在实际应用中可能会遇到的问题。

项目介绍：
Nightingale 是一个企业级的云原生可观察性解决方案，可以作为 Prometheus 的告警替代品和 Grafana 的可视化替代品。它是一个开源的云原生监控系统，一站式解决方案，集成了数据收集、可视化和监控告警。Nightingale 支持多种部署方式，如 Docker、Helm Chart 和云服务，集成数据收集、监控和告警到一个系统中，附带各种监控仪表板、快速查看和告警规则模板。它大大降低了云原生监控系统的建设成本、学习成本和使用成本。

如何使用：
Nightingale 的安装和使用非常简单。你可以选择 Docker、Helm Chart 或者云服务等多种部署方式，根据你的实际需求进行选择。Nightingale 还提供了丰富的监控仪表板、快速查看和告警规则模板，你可以根据你的实际需求进行配置和使用。

项目推介：
Nightingale 已经在数千家企业中部署，并在严酷的生产实践中得到了测试。许多领先的互联网公司已经使用 Nightingale 处理了数百个节点的集群机器，处理了数十亿的时间序列数据。如果你正在使用 Prometheus，并且有一个或多个以上的需求场景，我们强烈推荐你升级到 Nightingale。如果你正在使用 Zabbix，并且有以下的场景，我们也推荐你升级到 Nightingale。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ccfos/nightingale&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ccfos/nightingale 

开源项目作者：ccfos

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ccfos/nightingale)

关注我们，一起探索有意思的开源项目。

