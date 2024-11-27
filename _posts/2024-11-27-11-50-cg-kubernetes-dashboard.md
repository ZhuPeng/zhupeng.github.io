---
layout: post
title: GitHub 开源项目 kubernetes/dashboard 介绍，General-purpose web UI for Kubernetes clusters
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 kubernetes/dashboard，该项目在 GitHub 有超过 14.5k Star。

![](https://stats.deeptrain.net/repo/kubernetes/dashboard/?theme=light)

一句话介绍该项目：General-purpose web UI for Kubernetes clusters




![Coverage Status](https://codecov.io/github/kubernetes/dashboard/coverage.svg?branch=master)

![Dashboard UI workloads page](https://raw.githubusercontent.com/kubernetes/dashboard/master/docs/images/overview.png)


###### 项目介绍

### Kubernetes Dashboard 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1718bd06bc9f143b3b36b54a366fda6b.png)

项目介绍

#### 背景介绍

随着微服务和容器化技术的发展，Kubernetes 已成为最受欢迎的容器编排工具之一。但是，管理和监控一个或多个 Kubernetes 集群却是一项挑战。开发者和系统管理员需要一个直观、易用的界面来管理应用程序、监控服务状态、调试问题以及管理集群资源。而这正是 Kubernetes Dashboard 诞生的背景。

#### 项目介绍

Kubernetes Dashboard 是一个通用的、基于 Web 的 Kubernetes 集群 UI。它提供了一个可视化的界面让用户能够管理在集群中运行的应用，解决应用的问题，以及管理集群本身。从版本 7.0.0 开始，项目放弃了基于 Manifest 的安装方法，转而支持基于 Helm 的安装。这个变化带来了安装速度更快、对于所有依赖项能够有更好控制的优势。Kubernetes Dashboard 现在采用一个单容器、无数据库的 [Kong](https://hub.docker.com/r/kong/kong-gateway) 网关安装，通过 Kong 网关连接所有的容器，并暴露 UI。

#### 如何使用

安装 Kubernetes Dashboard 的步骤相当简单。首先，您需要通过 Helm 添加 Kubernetes Dashboard 的仓库。

```console
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
```

然后，使用 Helm chart 安装 Kubernetes Dashboard。

```console
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```

更多关于 Helm chart 的信息，可以访问 [ArtifactHub](https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard)。

#### 项目推介

Kubernetes Dashboard 是一个活跃发展的项目，由 Kubernetes 社区维护，拥有强大的社区支持。它是 Kubernetes 用户理想的管理界面，不仅适合新手了解和管理集群，还适合经验丰富的管理员进行高级操作。随着项目的发展，它已获得广泛的应用，被世界各地众多企业和组织所采用。其直观的 UI、强大的功能以及社区的活跃参与，使得 Kubernetes Dashboard 成为管理 Kubernetes 集群不可或缺的工具之一。

此外，如果你想贡献于项目，Kubernetes Dashboard 项目的维护者和社区非常欢迎新的贡献者。你可以通过 Kubernetes Slack 上的 **#sig-ui** 频道、kubernetes-sig-ui 邮件列表或贡献指南了解如何开始你的贡献之旅。

总之，无论你是 Kubernetes 的初学者还是有经验的专业人士，Kubernetes Dashboard 都是一个值得尝试和使用的项目，它将大大简化你的 Kubernetes 集群管理工作。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubernetes/dashboard&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes/dashboard 

开源项目作者：kubernetes

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubernetes/dashboard)

关注我们，一起探索有意思的开源项目。

