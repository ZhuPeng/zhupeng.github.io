---
layout: post
title: Kubestack - 一个 Terraform 代码库中定义整个云原生技术栈
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在如今云原生的浪潮下，Kubernetes 成为了云原生技术栈的核心。然而，对于很多的平台工程团队而言，我们所面临的问题有两个：一方面是使用 Terraform 为每个云厂商的 Kubernetes 平台都编写和维护一个独立的代码库，耗时且繁琐；另一方面则是将云原生的开发力量传递给全体工程团队，保证他们迭代安全，保护环境不受影响。

今天要给大家推荐一个 GitHub 开源项目 kbst/terraform-kubestack，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Kubestack is a framework for Kubernetes platform engineering teams to define the entire cloud native stack in one Terraform code base and continuously evolve the platform safely through GitOps.”。


![](https://raw.githubusercontent.com/kbst/terraform-kubestack/master/./assets/favicon.png)





###### 项目介绍

Kubestack 是一个 Terraform 框架，这个项目打破了云厂商和具体框架的边界，让工程团队可以在一个 Terraform 代码库中定义整个云原生技术栈。此外，这个项目还将 GitOps 工作流集成进来，让你持续不断、安全地变更你的平台。Kubestack 的特点包括有：约定优于配置的平台工程框架，可扩展、未来兼容性强、维护成本低的 Terraform 代码库，以及即便在复杂的 Kubernetes 平台上依然强大的自动化功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20231230201729915.png)

###### 如何使用

对于想要开始使用的用户，可以按照 Kubestack 教程 (https://www.kubestack.com/framework/tutorial/) 进行。官方也提供了一套深入教程 (https://www.kubestack.com/framework/documentation)，你可以在此查阅到关于如何使用和配置 Kubestack 的资料。

可以在 GitHub Release 按需下载相应平台的二进制命令行，即可开始使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20231230201859040.png)

整体的使用流程分为三步：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20231230201926660.png)

###### 项目推介

Kubestack 已经是一个活跃的开源项目，持续得到维护与更新。如果你是 Kubernetes、Terraform 或 Cloud 的爱好者，学习和使用 Kubestack 将会对你自身技术的提升带来很大的帮助。如果你正在寻找统一管理 Kubernetes 平台和实现跨云部署，同样也可以考虑使用 Kubestack。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kbst/terraform-kubestack&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kbst/terraform-kubestack 

开源项目作者：kbst

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kbst/terraform-kubestack)

关注我们，一起探索有意思的开源项目。

