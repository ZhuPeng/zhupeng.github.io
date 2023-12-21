---
layout: post
title: GitHub 开源项目 anthdm/hollywood 介绍，Blazingly fast and light-weight Actor engine written in Golang
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 anthdm/hollywood，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Blazingly fast and light-weight Actor engine written in Golang”。


![](https://discordapp.com/api/guilds/1025692014903316490/widget.png?style=shield)
![](https://discordapp.com/api/guilds/1025692014903316490/widget.png?style=banner2)



背景介绍：在编写多并发和分布式系统时，常常会遇到许多挑战，如如何优化系统性能、如何降低系统应用延迟、怎样在遇到错误和故障时保证系统的稳健性等问题。为了克服这些挑战，卡尔·惠特在 1973 年引入了演员模型。演员模型是一种计算模型，最基本的构建单位是演员，每一个演员独立运行，通过发送接收消息与其他演员交互，这种方式可以使系统具有高度的并发性和分布性。

项目介绍： Hollywood 是一个基于 Golang 的超快安全轻量级的演员引擎项目。它是为快速和低延迟的应用程序（如游戏服务器，广告代理商，交易引擎等）而构建的，能在一秒内处理超过 1000 万的消息。Hollywood 的主要特性包括消息在演员失败时的可靠传输 (缓冲机制)、忘却式或请求响应式消息传送，或两者都有、采用高性能的 dRPC 作为运输层、优化的 proto 缓冲区没有反射、轻量级和高度可定制、集群支持 [WIP] 等。

如何使用：如果你想要安装 Hollywood， 只需要简单指令 `go get github.com/anthdm/hollywood/...`。为了帮你理解如何使用 Hollywood ，我举个例子：创建一条Hello world 消息。你可以先新建一个 actor 简单终端打印消息，然后通过 Hollywood 的引擎 API 发送你的消息给 actor。具体的代码实例可以在 Hollywood README 文件中找到。

项目推介：Hollywood 是一个活跃开发并且广受好评的开源项目。该项目的主要开发者 Anthdm 是 GitHub 上的行业内知名开发者。在拥有很高的性能和灵活性的同时，Hollywood 也是一个非常轻量级的工具，它独特的演员模型设计解决了并发和分布式系统中的常见问题，使得它在业界广受赞誉。“Hollywood 有良好的代码质量，并且提供了强大、灵活且简单的 API”—— Go Report 评论。Hollywood 已经在许多知名的应用和公司中被使用，使得他们的系统更高效地运行。如果你是在构建并发和分布式系统，我强烈推荐你使用 Hollywood，它是一个值得你关注的重要工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=anthdm/hollywood&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anthdm/hollywood 

开源项目作者：anthdm

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=anthdm/hollywood)

关注我们，一起探索有意思的开源项目。

