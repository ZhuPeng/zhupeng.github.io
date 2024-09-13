---
layout: post
title: GitHub 开源项目 kyverno/kyverno 介绍，Cloud Native Policy Management
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 kyverno/kyverno，该项目在 GitHub 有超过 5.5k Star。

![](https://stats.deeptrain.net/repo/kyverno/kyverno/?theme=light)

一句话介绍该项目：Cloud Native Policy Management




![logo](https://raw.githubusercontent.com/kyverno/kyverno/master/img/Kyverno_Horizontal.png)


###### 项目介绍

### 背景介绍

随着云原生技术的迅速发展，越来越多的团队在日常运营中会遇到如何高效、安全地管理 Kubernetes 环境的问题。其中，如何实施有效的策略管理来确保集群安全、自动化运维、合规性及治理成为了一大挑战。传统的解决方案往往需要繁杂的配置和管理工作，且很难做到与云原生技术的无缝集成。这不仅消耗了大量的人力物力，也降低了团队的工作效率。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-946014d9c6f8746e773218f699df7be9.png)

项目介绍

**Kyverno（Cloud Native Policy Management）**正是为了解决上述问题而生。作为一个专为云原生平台工程团队设计的策略引擎，Kyverno 使安全、自动化、合规和治理的策略即代码 (Policy as Code) 变成可能。通过 Kubernetes 准入控制器、后台扫描和源代码仓库扫描，Kyverno 可以对配置进行验证、变更、生成和清理。它还可以用于 OCI 镜像的验证，以增强软件供应链的安全性。Kyverno 策略可作为 Kubernetes 资源进行管理，并且无需学习新的语言，非常适合与 kubectl、kustomize 和 Git 等你已经在使用的工具配合使用。

### 如何使用

安装 Kyverno 非常简单。你可以访问官方文档 [安装指南](https://kyverno.io/docs/installation/) 来找到详细的安装步骤。以下是快速开始的一个示例：

1. 通过 kubectl 直接安装到你的 Kubernetes 集群：

```shell
kubectl create -f https://raw.githubusercontent.com/kyverno/kyverno/main/config/install.yaml
```

2. 一旦安装，你可以开始定义自己的策略或者使用 [Kyverno 官网提供的样本策略](https://kyverno.io/policies/)。

### 项目推介

Kyverno 不仅拥有活跃的开发者社群，而且受到了众多知名公司和组织的信赖与使用，如被 Cloud Native Computing Foundation (CNCF) 纳入孵化项目，由知名公司 Nirmata 贡献。此外，Kyverno 在社区中的影响力也在不断扩大，凭借其强大的功能和易用性，吸引了众多开发者的关注和使用。

针对那些寻求云原生环境下策略管理解决方案的团队和个人，Kyverno 提供了一种高效、安全和简便的方法。无论是安全验证、资源管理、还是合规性检查，Kyverno 都能帮助你轻松实现。所以，如果你还在为 Kubernetes 环境中的策略管理头疼，不妨试试 Kyverno 吧！

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kyverno/kyverno&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kyverno/kyverno 

开源项目作者：kyverno

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kyverno/kyverno)

关注我们，一起探索有意思的开源项目。

