---
layout: post
title: GitHub 开源项目 diggerhq/digger 介绍，Digger is an open source IaC orchestration tool. Digger allows you to run IaC in your existing CI pipeline ⚡️  
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 diggerhq/digger，该项目在 GitHub 有超过 2.1k Star，用一句话介绍该项目就是：“Digger is an open source IaC orchestration tool. Digger allows you to run IaC in your existing CI pipeline ⚡️  ”。


![](https://github.com/diggerhq/digger/assets/1280498/7fb44db3-38ca-4021-8714-87a2f1a14982)





背景介绍：
在进行基础设施即代码（IaC）的编排时，我们常常会遇到一些问题。例如，CI/CD 对于 Terraform 来说可能会比较棘手，为了简化生活，专门的 CI 系统（也被称为 TACOS）如 Terraform Cloud、Spacelift、Atlantis 等应运而生。然而，为什么我们需要两个 CI 系统呢？为什么不重用现有 CI 的异步作业基础设施，包括计算、编排、日志等呢？

项目介绍：
Digger 是一个开源的 IaC 编排工具，它允许你在现有的 CI 管道中运行 IaC。Digger 的优势在于，它可以在你的 CI 中原生运行 terraform，这样做既安全，因为云访问密钥不会与第三方共享，又经济，因为你不需要为运行 terraform 支付额外的计算费用。Digger 的特性包括：在拉取请求评论中进行 Terraform 计划和应用、支持任何 VCS（如 Github、Gitlab、Azure Repos 等）、支持任何 CI（如 Github Actions、Gitlab、Azure DevOps 等）、支持任何云提供商（如 AWS、GCP、Azure 等）、支持私有运行器、支持 Open Policy Agent (OPA) 进行 RBAC、提供 PR 级别的锁（在 Terraform 原生状态锁的基础上，类似于 Atlantis），以避免跨多个 PR 的竞争条件等。

如何使用：
Digger 主要由两个组件组成：在你的 CI 内部运行并用正确的参数调用 terraform 的 CLI，以及响应 PR 评论等事件触发 CI 作业的 Orchestrator。你可以根据你的需求选择 Github Actions + AWS、Github Actions + GCP、Gitlab Pipelines + AWS 或 Azure DevOps 等组合进行使用。

项目推介：
Digger 是一个活跃的开源项目，它的开发者是知名的，项目本身也已经获得了一些奖项。此外，已经有一些知名的用户和公司在使用 Digger，比如 Github、Gitlab、Azure 等。如果你对 IaC 编排有需求，我强烈推荐你试试 Digger，它将会给你带来全新的体验。





以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=diggerhq/digger&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/diggerhq/digger 

开源项目作者：diggerhq

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=diggerhq/digger)

关注我们，一起探索有意思的开源项目。

