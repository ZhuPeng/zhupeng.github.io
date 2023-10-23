---
layout: post
title: OpenTF - Terraform 的真正开源版本
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在云计算日益普及的今天，我们会遇到如何有效管理云基础设施的问题。这个问题可能涉及到如何实现基础设施的版本控制，如何并行创建和修改非依赖资源，以及如何自动化复杂的变更等。这些都是我们在云基础设施管理中的核心痛点。

今天要给大家推荐一个 GitHub 开源项目 opentffoundation/opentf，该项目在 GitHub 有超过 4.5k Star，用一句话介绍该项目就是：“OpenTF lets you declaratively manage your cloud infrastructure.”。


![](https://raw.githubusercontent.com/opentffoundation/brand-artifacts/main/full/transparent/SVG/on-light.svg)

###### 项目介绍

OpenTF 可以安全、高效地构建、更改和版本控制基础设施。它可以管理现有的流行服务提供商以及自定义的内部解决方案。OpenTF 的主要特点包括：

1、基础设施即代码，使用高级配置语法描述基础设施，使得数据中心的蓝图可以像其他代码一样进行版本控制，基础设施可以共享和重用；

2、执行计划，OpenTF 有一个 "规划" 步骤，生成执行计划，这让你在 OpenTF 操作基础设施时避免任何意外；

3、资源图，OpenTF 构建了所有资源的图，并并行创建和修改任何非依赖资源，这使得 OpenTF 能够尽可能高效地构建基础设施，操作员可以深入了解他们的基础设施中的依赖关系；

4、变更自动化，可以将复杂的变更集应用到你的基础设施上，几乎不需要人工干预。

OpenTF 的项目启动主要原因是 2023-08-10，Terraform 公司 HashiCorp 将 Terraform 的开源协议由 MPL 改成了 BUSL（Business Source License），意味着 Terraform 不在是一个真正意义的开源项目了，这对整个社区和生态都造成了严重的影响。

###### 项目推介

OpenTF 目前正在积极开发中，正在为首次 alpha 版本发布做准备，并对社区贡献过程进行微调。请注意，如果你从 Terraform Registry 获取你的提供商或模块，那么在当前状态下构建此仓库并运行可能会违反 Terraform Registry 的 ToS。我们欢迎大家加入我们的 Slack 社区，一起参与到 OpenTF 的开发中来。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=opentffoundation/opentf&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/opentffoundation/opentf 

开源项目作者：opentffoundation

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=opentffoundation/opentf)

关注我们，一起探索有意思的开源项目。

