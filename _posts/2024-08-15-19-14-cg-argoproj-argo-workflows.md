---
layout: post
title: 容器原生的工作流引擎推荐
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代软件开发中，自动化工作流的搭建成为了提高效率、保障稳定性和可扩展性的关键。尤其是在容器化和微服务架构的兴起下，开发者和运维团队急需一种能在 Kubernetes 环境中轻松编排和管理复杂工作流的工具。例如，机器学习的管道处理、大量的数据批处理、基础设施的自动化操作、CI/CD 流程等都面临着管理复杂度高、执行效率不理想等问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-b0a7d3183c9ea91fe2a30dcc328c3169.png)

今天要给大家推荐一个 GitHub 开源项目 argo-workflows，该项目在 GitHub 有超过 14.8k Star。

![](https://stats.deeptrain.net/repo/argoproj/argo-workflows/?theme=light)

一句话介绍该项目：Workflow Engine for Kubernetes


![Screenshot](https://raw.githubusercontent.com/argoproj/argo-workflows/master/docs/assets/screenshot.png)


###### 项目介绍

Argo Workflows 是一个容器原生的工作流引擎，专门为 Kubernetes 环境设计，用于编排并行作业。它通过 Kubernetes CRD (自定义资源定义) 实现，让用户能够定义每个步骤为一个容器，支持将多步骤工作流建模为任务序列或使用有向无环图 (DAG) 捕获任务之间的依赖。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825195004411.png)

Argo Workflows 能够极大地简化计算密集型作业，如机器学习或数据处理的执行，使其运行时间大大缩短。作为 [云原生计算基金会 (CNCF)](https://cncf.io/) 的毕业项目，它提供了轻量级、可伸缩和易于使用的特点，是 Kubernetes 上最受欢迎的工作流执行引擎。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825195016581.png)

###### 如何使用

想要开始使用 Argo Workflows，你可以通过以下步骤快速开始：

1、访问官方文档 [Quickstart](https://argo-workflows.readthedocs.io/en/latest/quick-start/) 指南来安装 Argo Workflows。

2、通过 [walk-through examples](https://argo-workflows.readthedocs.io/en/latest/walk-through/) 深入了解 Argo Workflows 的使用示例。

例如，用 Argo 创建一个简单的工作流可以通过 Kubernetes yaml 文件定义如下：

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-
spec:
  entrypoint: whalesay
  templates:
  - name: whalesay
    container:
      image: docker/whalesay:latest
      command: [cowsay]
      args: ["hello world"]
```

这个 YAML 文件定义了一个简单的工作流，其中包含了一个名为 `whalesay` 的步骤，执行了 Docker 镜像 `docker/whalesay` 的 `cowsay hello world` 命令。

###### 项目推介

Argo Workflows 自推出以来，已被超过 200+ 组织官方使用，包括不止于数据处理、机器学习、CI/CD 和基础设施自动化等多种用例。它的设计轻量级且易于上手，可以无关心云平台地在任何 Kubernetes 集群上运行。此外，作为 CNCF 的毕业项目，其社区活跃和持续发展，拥有庞大的用户和贡献者基础，确保了项目的长期维护和更新。多家知名公司和组织的背书，如 Netflix、Seldon、Onepanel 等在内的多个项目也在使用或依赖 Argo Workflows，进一步证明了其在行业内的影响力和实用性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825195214167.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=argoproj/argo-workflows&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/argoproj/argo-workflows 

开源项目作者：argoproj

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=argoproj/argo-workflows)

关注我们，一起探索有意思的开源项目。

