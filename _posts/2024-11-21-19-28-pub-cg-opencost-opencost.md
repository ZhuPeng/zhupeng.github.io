---
layout: post
title: 云成本监控的开源解决方案
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的云计算中， Kubernetes 成为了云服务中不可或缺的组成部分。然而，随之带来的是成本监控的挑战，尤其是在多应用、多团队、多部门的 Kubernetes 环境中。企业通常面临着如何有效监控并优化 Kubernetes 工作负载和跨多个云服务商的云成本的问题，这些问题核心在于：缺乏透明度、成本分配复杂、难以监控多云成本。

今天要给大家推荐一个 GitHub 开源项目 opencost，该项目在 GitHub 有超过 5.3k Star。

![](https://stats.deeptrain.net/repo/opencost/opencost/?theme=light)

一句话介绍该项目：Cost monitoring for Kubernetes workloads and cloud costs

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125230922756.png)


###### 项目介绍

OpenCost 为团队提供了当前和历史 Kubernetes 及云支出和资源分配的可见性。它支持跨多个应用、团队、部门等的成本透明度，同时提供多个云服务商的云成本可见性。



项目亮点如下：

1、全面成本监控：实时按 Kubernetes 集群、节点、命名空间、控制器类型、控制器、服务或 Pod 分配成本。

2、多云成本监控：支持 AWS、Azure、GCP 等所有云服务的成本监控。

3、动态定价：通过 AWS、Azure 和 GCP 计费 API 集成，实现 K8s 资产的动态即时定价。

4、On-prem 支持：支持使用自定义 CSV 定价的本地 K8s 集群。

5、环境友好：支持云资源的碳成本核算。

6、易于扩展：通过 OpenCost 插件支持第三方成本，例如 Datadog。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125231119270.png)

###### 如何使用

只需几分钟，就可以在任何 Kubernetes 1.20+ 集群上部署 OpenCost！推荐访问完整文档 [Install Guide](https://www.opencost.io/docs/installation/install)

OpenCost 提供了丰富的使用途径，包括成本 API、CLI/kubectl 成本命令、Prometheus 指标和用户界面等，为用户带来便利和灵活性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241125231405971.png)

###### 项目推介

OpenCost 拥有活跃的开发社区、深受业内人士和公司的推荐。其跨云和 on-prem 方案的全面覆盖，以及丰富的功能特性，使其成为 Kubernetes 成本监控领域的佼佼者。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=opencost/opencost&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/opencost/opencost 

开源项目作者：opencost

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=opencost/opencost)

关注我们，一起探索有意思的开源项目。

