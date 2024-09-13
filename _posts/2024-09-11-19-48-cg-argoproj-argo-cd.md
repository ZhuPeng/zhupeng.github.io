---
layout: post
title: GitHub 开源项目 argoproj/argo-cd 介绍，Declarative Continuous Deployment for Kubernetes
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 argoproj/argo-cd，该项目在 GitHub 有超过 17.4k Star。

![](https://stats.deeptrain.net/repo/argoproj/argo-cd/?theme=light)

一句话介绍该项目：Declarative Continuous Deployment for Kubernetes




![Argo CD UI](https://raw.githubusercontent.com/argoproj/argo-cd/master/docs/assets/argocd-ui.gif)

![Argo CD Demo](https://img.youtube.com/vi/0WAm0y2vLIo/0.jpg)


###### 项目介绍

背景介绍：
随着云原生技术和 Kubernetes 的日益普及，软件部署和生命周期管理变得日益复杂和多变。团队面临的挑战是如何确保应用程序的配置和部署过程既高效又可靠。在持续部署（CD）的背景下，开发者和运维团队需要一种既可以自动化管理应用生命周期，又能保证部署的稳定性和可回溯性的解决方案。传统的 CI/CD 工具在处理 Kubernetes 资源对象的声明式配置和版本控制方面存在局限，这就需要一种新的工具来满足当前的需求。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-3bf71c5ef89bb4901e073befd99f81c8.png)

项目介绍：
Argo CD 是一个为 Kubernetes 设计的声明式、GitOps 风格的持续部署工具，它通过直接使用 Git 仓库作为应用程序部署的真实来源来自动化部署过程。Argo CD 遵循 GitOps 原则，确保应用程序的定义、配置和环境都是声明式和版本控制的，同时实现了部署和生命周期管理的自动化、审计和易于理解。

Argo CD 的主要功能包括：
- 自动化的部署和更新：使用 Git 仓库作为唯一信任源来自动同步和部署 Kubernetes 资源。
- 环境差异可视化：清晰显示当前部署状态与 Git 仓库定义之间的差异。
- 多种应用支持：支持从简单的 Web 应用到复杂的多层微服务应用的部署。
- 授权和访问控制：与 Kubernetes 的 RBAC 紧密集成，支持精细的访问控制。

如何使用：
安装 Argo CD 可以通过 Helm chart、Kustomize 或直接使用 Argo CD 的命令行工具进行。以下是一个简单的安装步骤例子：
```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
使用时，只需将 Kubernetes 清单文件推送到 Git 仓库然后配置 Argo CD 监视该仓库。当 Git 仓库更新时，Argo CD 会自动将变更同步到 Kubernetes 集群中。

项目推介：
Argo CD 已经在业界获得了广泛认可和应用，它不仅活跃开发，还有着庞大的用户和贡献者社区。它已被很多知名公司和组织采用来管理他们的 Kubernetes 部署，如谷歌（Google）、红帽（Red Hat）、Intuit 等。Argo CD 的设计理念、易用性和强大的功能使它成为 Kubernetes 持续部署的首选工具之一。此外，它还通过了 Cloud Native Computing Foundation（CNCF）的最佳实践认证，保证了其高质量和可靠性。如果您是 Kubernetes 的使用者，寻找一种高效、可靠的持续部署工具，Argo CD 绝对是您不错的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=argoproj/argo-cd&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/argoproj/argo-cd 

开源项目作者：argoproj

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=argoproj/argo-cd)

关注我们，一起探索有意思的开源项目。

