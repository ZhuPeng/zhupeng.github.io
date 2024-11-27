---
layout: post
title: GitHub 开源项目 Shopify/toxiproxy 介绍，:alarm_clock: :fire: A TCP proxy to simulate network and system conditions for chaos and resiliency testing
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 Shopify/toxiproxy，该项目在 GitHub 有超过 10.9k Star。

![](https://stats.deeptrain.net/repo/Shopify/toxiproxy/?theme=light)

一句话介绍该项目：:alarm_clock: :fire: A TCP proxy to simulate network and system conditions for chaos and resiliency testing




![](http://i.imgur.com/sOaNw0o.png)


###### 项目介绍

### 背景介绍
在软件开发和运维过程中，我们常会遇到网络环境变化给系统带来的挑战。例如，服务之间的通信延迟增加、连接突然中断、带宽限制等问题，这些情况都可能在真实的生产环境中发生，导致系统表现异常或直接宕机。这类问题对于分布式系统尤为明显，因为其稳定性很大程度依赖于网络的可靠性。如何在开发、测试阶段就发现并处理好这些问题，成为了提升系统健壮性、确保服务高可用的关键部分。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-affa35600a75aa52b2c30c51d1a4dfce.png)

项目介绍
**Toxiproxy** 是由 Shopify 开发并维护的一个开源项目，是专门设计用于在测试、CI 和开发环境模拟各种网络条件的框架。它可以对连接进行确定性的干扰操作，并支持随机性的混乱场景和可自定义的模拟环境。Toxiproxy 的核心理念在于，通过模拟各种网络问题，帮助开发者验证他们的应用在面对单点故障时的行为，确保应用的鲁棒性。它自 2014 年 10 月以来，一直被 Shopify 在所有的开发和测试环境中成功使用。

Toxiproxy 主要由两部分组成：一个用 Go 语言编写的 TCP 代理以及一个通过 HTTP 与代理通信的客户端。你可以配置应用程序将所有测试连接通过 Toxiproxy 进行，并可以通过 HTTP 操作它们的健康状态。

### 如何使用
安装 Toxiproxy 相对简单。主要步骤包括：
1. **安装 Toxiproxy**：可以从 GitHub 的 [发布页面](https://github.com/Shopify/toxiproxy/releases/latest) 下载最新版本。
2. **配置**：使用 Toxiproxy，你需要先定义需要代理的服务（如 MySQL、Redis 等）的配置。
3. **使用**：通过对应的客户端库（如 toxiproxy-ruby）操控 Toxiproxy 来模拟网络问题。例如，如果你想给 MySQL 响应增加 1000ms 的延迟，可以使用如下 Ruby 代码：
   ```ruby
   Toxiproxy[:mysql_master].downstream(:latency, latency: 1000).apply do
     Shop.first # 这将至少需要 1 秒钟
   end
   ```

### 项目推介
Toxiproxy 在技术社区中受到广泛的认可和使用。它不仅因其强大的网络模拟能力受到开发者青睐，还因为 Shopify 这个背后的大公司支持而增强了开发者的信心。除了 Shopify，也有许多其他知名公司和项目在使用 Toxiproxy 来进行他们的混沌和韧性测试。此外，其丰富的客户端库支持（包括 Ruby、Go、Python、.NET、PHP、Node.js、Java、Haskell、Rust、Elixir 等）使得 Toxiproxy 成为了多语言环境下理想的测试伴侣。

结合它持续活跃的开发状态、社区对其的积极评价，以及广泛的使用案例，Toxiproxy 是一个值得任何关注服务稳定性和网络鲁棒性的团队考虑的项目。无论你是一个软件开发人员、测试工程师还是系统架构师，Toxiproxy 都能帮助你更加自信地确保你的系统能够抵御网络波动和故障，是构建高可靠性

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Shopify/toxiproxy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Shopify/toxiproxy 

开源项目作者：Shopify

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Shopify/toxiproxy)

关注我们，一起探索有意思的开源项目。

