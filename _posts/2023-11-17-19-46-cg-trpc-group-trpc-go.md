---
layout: post
title: GitHub 开源项目 trpc-group/trpc-go 介绍，A pluggable, high-performance RPC framework written in golang
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 trpc-group/trpc-go，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“A pluggable, high-performance RPC framework written in golang”。


![Architecture](https://raw.githubusercontent.com/trpc-group/trpc-go/master/.resources/overall.png)



背景介绍：
在分布式系统领域，RPC（远程过程调用）协议被广泛应用在跨机器和跨进程的通信中，但是传统的 RPC 协议无法满足我们需求，如高性能和易扩展性。tRPC-Go 就是这样一个针对现代服务化开发需求而设计的开源项目。

项目介绍：
tRPC-Go，一个灵活、高性能的 RPC 框架，是 tRPC 在 golang 语言下的实现。tRPC-Go 拥有如下特性：
- 在单个进程中可以启动多个服务，能同时在多个地址上进行监听。
- 所有的组件都是可插拔的，其中一些基本功能有默认的实现方式，也可以进行替换。第三方还可以实现其他组件，并在框架中进行注册。
- 所有的接口都可以同时用 gomock&mockgen 生成 mock 代码进行 mock 测试，这将方便进行测试。
- 通过实现各自协议的 `codec` 接口，该框架支持任意第三方协议。它默认支持 trpc 和 http 协议，并且可以随时进行切换。
- 提供了 [trpc 命令行工具][trpc-cmdline]用于生成代码模板。

如何使用：
您可以将 tRPC-Go 带入您的 golang 项目，然后使用 trpc 命令行工具生成代码模板。详细的使用步骤你可以参考官方的 [快速入门指南][quick start] 和 [详细文档][docs]。此外，该项目还提供 [helloworld 案例开发指南][helloworld] 和 [各种特性示例文档][features]，你可以通过这些案例来了解如何使用 tRPC-Go 框架。

项目推介：
如果你在寻找一个高效灵活、支持多协议和容易与其他组件整合的 RPC 框架，那么 tRPC-Go 可能会是你的首选。项目维护者团队 tRPC Group 除了在该项目上有很积极的开发进度之外，还提供了一系列与 tRPC-Go 相关的插件，如 codec 插件、过滤器插件和数据库插件，使得该项目具备更强大的拓展能力。此外，他们不仅拥有详细的文档，还在  [https://github.com/trpc-group/trpc-go/issues][issues] 中邀请大家参与贡献项目。

点击此链接查看项目：https://github.com/trpc-group/trpc-go



以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=trpc-group/trpc-go&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/trpc-group/trpc-go 

开源项目作者：trpc-group

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=trpc-group/trpc-go)

关注我们，一起探索有意思的开源项目。

