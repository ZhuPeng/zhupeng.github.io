---
layout: post
title: GitHub 开源项目 runatlantis/atlantis 介绍，Terraform Pull Request Automation
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 runatlantis/atlantis，该项目在 GitHub 有超过 7.6k Star。

![](https://stats.deeptrain.net/repo/runatlantis/atlantis/?theme=light)

一句话介绍该项目：Terraform Pull Request Automation




![](https://raw.githubusercontent.com/runatlantis/atlantis/master/./runatlantis.io/public/hero.png)


###### 项目介绍

### 背景介绍

在持续集成和持续部署（CI/CD）的自动化流程中，Terraform 作为一款强大的基础设施即代码（Infrastructure as Code, IaC）工具，对云资源的管理提供了极大的便利性。然而，团队在使用 Terraform 管理复杂的云基础设施时，往往面临着一系列挑战：如何确保代码提交前对 Terraform 的变更进行充分的审查？如何让非运维背景的开发人员有效参与到 Terraform 的变更过程中？如何统一 Terraform 工作流程以提高团队的工作效率？这些核心痛点加剧了团队的协作难度，降低了运维自动化的效率。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0e872344179593c672fd3161a6a1a76b.png)

项目介绍

**Atlantis** 是一个自托管的 Go 语言应用，旨在通过监听基于 Webhooks 的 Terraform 拉取请求（Pull Request, PR）事件，提供自动化的 Terraform PR 操作。它能够执行 `terraform plan`, `import`, `apply` 等命令，并将执行结果通过评论的方式反馈到 PR 上，从而提高了 Terraform 在团队中的可见性和可操作性。通过使用 Atlantis，团队可以：
- 使 Terraform 变更对全团队可见，增强透明度；
- 允许非运维工程师参与 Terraform 流程，拓展协作边界；
- 标准化 Terraform 工作流程，统一变更管理方式。

### 如何使用

要开始使用 **Atlantis**，需要先进行简单的安装和配置：
1. 从 [Atlantis GitHub 仓库的最新发布版本](https://github.com/runatlantis/atlantis/releases/latest)下载相应的应用包。
2. 根据 [官方文档](https://www.runatlantis.io/docs) 对 Atlantis 进行配置，包括设置 Webhooks 和配置文件等。
3. 启动 Atlantis 服务器后，它会监听来自 GitHub 的 Terraform PR 事件。

当 PR 提交到 GitHub 上后，Atlantis 会自动执行设定的 Terraform 命令，并将结果评论到 PR 下，使得团队成员能够清晰地看到变更效果。

### 项目推介

由于 Atlantis 是围绕 Terraform PR 自动化而设计，它在 DevOps 和云基础设施管理的应用场景中提供了极大的价值。Atlantis 项目自推出以来活跃度持续上升，其稳定、高效的特性受到了包括 Kelsey Hightower 在内的业内知名人士的推荐。其 GitHub 星标也在持续增加，显示了广泛的用户基础和社区的积极参与度。

无论是刚开始接触 Terraform，还是已经在大规模使用 Terraform 的团队，Atlantis 都提供了一种标准化、自动化的解决方案，帮助团队更高效地管理和审查基础设施变更。这不仅增加了协作效率，还提高了代码变更的可靠性。随着越来越多的公司和开发者开始使用 Atlantis，它已经成为了云基础设施管理领域不可或缺的工具之一。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=runatlantis/atlantis&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/runatlantis/atlantis 

开源项目作者：runatlantis

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=runatlantis/atlantis)

关注我们，一起探索有意思的开源项目。

