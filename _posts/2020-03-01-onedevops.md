---
layout: post
title: 号称可替代 GitLab 的开源 DevOps 平台
tags: 其他
---

疫情之下，每个公司都走的很艰难，对于互联网公司来说，一直很注重效率，而今时今日效率将显得更为重要。如果你的公司开发测试效率更高，意味着你会相比同行更快的交付产品，做更多的领域尝试。

今天要推荐的是一个 DevOps 平台：onedev，其包含任务管理、Git 代码管理、代码评审和代码构建等功能，简单而强大。我们来具体看看都提供了什么功能。



### 原生支持 Kubernetes 的容器构建集群

你可以很容易的配置一个基于 Kubernetes 的大规模构建集群，不需要任何代理和 Worker，而且可以直接支持 Linux 和 Windows 容器。

[![Job Executor](https://raw.githubusercontent.com/theonedev/onedev/master/features/job-executor.png)](https://github.com/theonedev/onedev/blob/master/features/job-executor.png)



### 轻松定制化构建配置

对于服务的构建配置，不需要写 YAML 配置，没有复杂语法需要记。几乎不用学习就可以掌握创建项目的构建配置，只需要提供构建镜像和执行命令即可。

[![Cispec](https://github.com/theonedev/onedev/raw/master/features/cispec.gif)](https://github.com/theonedev/onedev/blob/master/features/cispec.gif)



### 弹性灵活的构建流水线

通过不同的构建参数，可以矩阵式的组合不同的构建流程，通过连接不同的任务而构成流水线。不管是并行执行任务、在特定事件发生时自动运行任务等场景，都可以很容易的在平台上配置。

[![Build Workflow](https://github.com/theonedev/onedev/raw/master/features/build-workflow.gif)](https://github.com/theonedev/onedev/blob/master/features/build-workflow.gif)



### 可定制化的任务状态和字段

平台提供对任务状态和字段的可定制化能力，可以配置字段的相互依赖，支持事件自动触发或者被认证用户手动更改任务状态。

[![Custom Issue](https://github.com/theonedev/onedev/raw/master/features/custom-issue.gif)](https://github.com/theonedev/onedev/blob/master/features/custom-issue.gif)



### 自动更新的任务看板

通过定制化的字段，可以定制自己的任务看板。操作任务状态不需要跳出任务看板。同时看板内容是自动刷新的，方便实时看到最近的任务状态变更。

[![Issue Boards](https://github.com/theonedev/onedev/raw/master/features/issue-boards.gif)](https://github.com/theonedev/onedev/blob/master/features/issue-boards.gif)



### 代码搜索和跳转

平台提供的搜索功能能够感知不同的编程语言，同时支持代码的高亮、Diff 和函数跳转，目前支持 Java, JavaScript, C, C++, CSharp, Go, PHP, Python, CSS, SCSS, LESS and R。

[![Symbol Search](https://github.com/theonedev/onedev/raw/master/features/symbol-search.gif)](https://github.com/theonedev/onedev/blob/master/features/symbol-search.gif)



### 代码讨论和注释

在平常工作中对一些代码有疑问，一般会咨询其他人，而方式一般是当面或者通过聊天工具，一般不能很好的保留沟通的记录方便后续其他同学查看。针对上述场景，onedev 在不需要创建 PR 的情况下，就可快速和轻量化的发起代码之间的讨论，讨论的记录会保留以便后续代码查看者参考。

[![Code Comments](https://github.com/theonedev/onedev/raw/master/features/code-comments.gif)](https://github.com/theonedev/onedev/blob/master/features/code-comments.gif)



### 灵活的代码评审策略

平台支持对仓库进行分支保护，提交的代码必须经过代码评审，同时可以对特定的文件匹配设置特定的代码评审员。

[![Branch Protection](https://github.com/theonedev/onedev/raw/master/features/branch-protection.gif)](https://github.com/theonedev/onedev/blob/master/features/branch-protection.gif)



### 简单易操作的代码评审

平台提供直接查看所有 PR 提交，和逐个依次查看的能力，并显示的展示 PR 中上一次评审的变更。

[![Increment Review](https://github.com/theonedev/onedev/raw/master/features/increment-review.gif)](https://github.com/theonedev/onedev/blob/master/features/increment-review.gif)



### 强大的查询语法

平台提供强大的查询能力，搜索内容范围覆盖了项目、Commits、构建、任务、PR、代码评论等。搜索语句可以被保存以便下次直接使用，同时支持搜索结果订阅，如果有更新将会获取相应的通知事件。

[![Powerful Query](https://github.com/theonedev/onedev/raw/master/features/powerful-query.gif)](https://github.com/theonedev/onedev/blob/master/features/powerful-query.gif)



### 深度集成代码、任务、PR和构建

通过配置不同的任务触发、状态变更方式，可以深度集成代码变更、任务状态变更、构建的操作，做到牵一发而动全身的自动化水平。

[![Issue Query](https://github.com/theonedev/onedev/raw/master/features/issue-query.gif)](https://github.com/theonedev/onedev/blob/master/features/issue-query.gif)



### 细粒度的权限控制

平台提供了非常细粒度的权限控制能力，完全可以满足你日常的开发需求。你可以配置对特定文件夹的权限；配置谁可以分配任务；配置谁可以运行发布构建；或者谁可以获取构建日志等。

[![Role](https://github.com/theonedev/onedev/raw/master/features/role.png)](https://github.com/theonedev/onedev/blob/master/features/role.png)

更多的功能和介绍参考如下链接。

> 项目链接：https://github.com/theonedev/onedev