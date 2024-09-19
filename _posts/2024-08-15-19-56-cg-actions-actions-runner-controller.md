---
layout: post
title: 为 GitHub Actions 提供自托管 runners 的编排扩展能力
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

持续集成（CI）和持续部署（CD）已成为提高开发效率和代码质量的关键,GitHub Actions 是面向 CI/CD 的强大工具，但在使用 GitHub 官方托管的 runners 时，我们可能会遇到资源限制、定制化程度不足以及运行成本高等问题。特别是对于大型或有特定安全需求的项目，这些问题成为了业务发展的痛点。

今天要给大家推荐一个 GitHub 开源项目 actions-runner-controller，该项目在 GitHub 有超过 4.5k Star。

![](https://stats.deeptrain.net/repo/actions/actions-runner-controller/?theme=light)

一句话介绍该项目：Kubernetes controller for GitHub Actions self-hosted runners

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909221711960.png)

###### 项目介绍

Actions Runner Controller (ARC) 是一个 Kubernetes Operator，它为 GitHub Actions 提供自托管 runners 的编排和扩展能力。通过 ARC，你可以创建自动根据仓库、组织或企业中正在运行的工作流数量自动扩展的 runner 缩放集。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909221856147.png)

得益于其容器化的设计，这些自托管 runners 可以快速动态地扩展或收缩，为 CI/CD 流水线提供灵活、高效和成本可控的执行环境。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909221912095.png)

###### 如何使用

首先需要在 Kubernetes 集群上通过 Helm 安装 ARC，随后便可创建并运行使用 runner 缩放集的工作流。关于安装与具体使用，可以参照以下简易步骤：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909222027842.png)

1、使用 Helm 安装 ARC 到你的 Kubernetes 集群

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909222116322.png)

2、根据 GitHub 官方文档配置自托管 runners

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909222153219.png)

3、在你的 GitHub Actions 工作流中引用这些自托管 runners

以下是一个使用 ARC 的基本示例代码：

```yaml
name: Actions Runner Controller Demo
on:
  workflow_dispatch:

jobs:
  Explore-GitHub-Actions:
    # You need to use the INSTALLATION_NAME from the previous step
    runs-on: arc-runner-set
    steps:
    - run: echo "🎉 This job uses runner scale set runners!"
```

###### 项目推介

ARC 不仅受到了广泛的社区支持，其背后还有与 GitHub Actions 团队的紧密合作。项目活跃、持续更新，并且对于希望在 Kubernetes 集群上高效地运行自托管 GitHub Actions runners 的组织来说，是一个充满价值的选择。其在各类规模的组织和公司中都有应用案例，证明了其在实际业务中的可靠性与效率。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=actions/actions-runner-controller&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/actions/actions-runner-controller 

开源项目作者：actions

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=actions/actions-runner-controller)

关注我们，一起探索有意思的开源项目。

