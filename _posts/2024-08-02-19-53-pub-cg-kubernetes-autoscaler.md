---
layout: post
title: 专为 K8S 设计的自动伸缩组件集合
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的云计算和微服务架构中，资源管理成为了一项挑战。对于运行在 Kubernetes 上的应用来说，如何合理高效地分配和使用资源是一个大问题。开发者和运维团队常常需要在资源利用率和应用性能之间寻找微妙的平衡。太多资源意味着浪费，太少则可能导致服务不稳定甚至中断。自动伸缩技术应运而生，可以根据实际工作负载动态地调整资源，但实现一个既准确又高效的自动伸缩系统并非易事。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-ebf90a826961af8810b04381175c2995.png)

今天要给大家推荐一个 GitHub 开源项目 autoscaler，该项目在 GitHub 有超过 8k Star。

![](https://stats.deeptrain.net/repo/kubernetes/autoscaler/?theme=light)

一句话介绍该项目：Autoscaling components for Kubernetes

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240818200730296.png)

###### 项目介绍

Kubernetes Autoscaler 是一个专为 Kubernetes 设计的自动伸缩组件集合，其核心目标是优化资源使用，确保服务稳定运行。该项目包含三个主要组件：

1、Cluster Autoscaler：自动调整 Kubernetes 集群的大小，保证所有 Pod 都有合适的地方运行，同时避免资源闲置。它支持多个公有云提供商，并在 Kubernetes 1.8 版本中达到了 1.0 正式版本（GA）。

2、Vertical Pod Autoscaler：自动调整运行在 Kubernetes 集群中的 Pod 所请求的 CPU 和内存量，当前状态为 beta。

3、Addon Resizer：基于集群节点数量调整 Deployment 请求资源的简化版 Vertical Pod Autoscaler，当前状态也是 beta。

项目还包括支持上述组件的 Helm charts，以便于在 Kubernetes 环境中部署和管理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240818202712608.png)

###### 如何使用

Kubernetes Autoscaler 的代码库必须作为 `k8s.io` 的子目录检出，而不是 `github.com`。以下是克隆并开始使用它的基本步骤：

```bash
mkdir -p $GOPATH/src/k8s.io
cd $GOPATH/src/k8s.io
# replace $YOUR_GITHUB_USERNAME to your GitHub account
git clone https://github.com/$YOUR_GITHUB_USERNAME/autoscaler.git
cd autoscaler
```

更详尽的开发指南和使用说明可以在官方 GitHub 仓库以及 Kubernetes 社区指南中找到。

###### 项目推介

Kubernetes Autoscaler 是 Kubernetes 官方支持的自动伸缩解决方案，由一个活跃的开源社区维护。它是许多企业和组织管理 Kubernetes 集群资源不可或缺的工具。Kubernetes Autoscaler 都能帮助你实现精细、智能的资源管理，确保应用的高效稳定运行。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubernetes/autoscaler&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes/autoscaler 

开源项目作者：kubernetes

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubernetes/autoscaler)

关注我们，一起探索有意思的开源项目。

