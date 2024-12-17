---
layout: post
title: GitHub 开源项目 smartcontractkit/chainlink 介绍，node of the decentralized oracle network, bridging on and off-chain computation
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 smartcontractkit/chainlink，该项目在 GitHub 有超过 7.1k Star。

![](https://stats.deeptrain.net/repo/smartcontractkit/chainlink/?theme=light)

一句话介绍该项目：node of the decentralized oracle network, bridging on and off-chain computation




![](https://raw.githubusercontent.com/smartcontractkit/chainlink/develop/docs/logo-chainlink-blue.svg)


###### 项目介绍

在当前的区块链领域，智能合约因为其可信、去中心化的特性而受到广泛的关注和应用。然而，一个核心的挑战是，现有的智能合约无法直接与现实世界的数据和外部计算进行互动。这就意味着，如果一个智能合约需要天气信息、股价信息或者其他任何外部数据，那么它就无法直接获取，这极大限制了智能合约的潜在应用场景和价值。

在此背景下，[Chainlink](https://github.com/smartcontractkit/chainlink) 应运而生。它是一个去中心化的预言机网络节点，致力于连接链上与链下的计算。通过 Chainlink，智能合约可以安全、可靠地访问链外数据，同时保持了区块链技术固有的安全和可靠性保证。简而言之，Chainlink 为智能合约打开了连接真实世界的大门。

Chainlink 的核心节点和合约是其主要的两大构件。核心节点是可由参与去中心化预言机网络的节点操作者运行的打包二进制文件。该项目在 [Chainlink dockerhub](https://hub.docker.com/r/smartcontract/chainlink/tags) 上提供了所有主要发布版本的预建 docker 镜像，便于用户下载和使用。

对于想要参与到 Chainlink 贡献的开发者，项目提供了[贡献指南](https://github.com/smartcontractkit/chainlink/docs/CONTRIBUTING.md)。同时，如果用户遇到bug或者有功能请求，可以在项目的 [Issues 页面](https://github.com/smartcontractkit/chainlink/issues) 查找或创建新的 Issue。

Chainlink 的社区非常活跃，开发者和用户可以使用 [Discord](https://discordapp.com/invite/aSK4zew) 来进行日常的沟通，解答开发问题，聚集与 Chainlink 相关的内容。

安装和运行 Chainlink 的步骤非常简单：下载 Chainlink 代码，构建并安装，最后运行节点。具体的安装步骤包括安装 Go 1.23、NodeJS v20、pnpm v9、Postgres (>= 12.x)，以及 Python 3。构建项目仅需执行 `make install` 命令，运行节点使用 `chainlink help` 命令。

Chainlink 不仅支持传统架构，还考虑到了在 Apple Silicon 上的原生构建和使用 Docker 镜像的情况，为使用不同技术栈的开发者提供了方便。

为了让 Chainlink 节点运行，你需要访问一个开放了 websocket 连接的运行中以太坊节点。目前，Chainlink 支持并测试了如 Parity/Openethereum、Geth、Besu 等官方支持的以太坊执行客户端。

Chainlink 目前享有来自开发者和企业的广泛关注和使用，包括但不限于其开发活跃程度、作者团队的知名度、在业内的获奖情况以及已经在使用的知名用户或公司等。此外，Chainlink 因其创新的去中心化预言机技术，受到了业内专家和知名人士的高度评价和推荐。如果你寻找一个连接智能合约与现实世界数据的可靠桥梁，Chainlink 无疑是一个值得考虑的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=smartcontractkit/chainlink&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/smartcontractkit/chainlink 

开源项目作者：smartcontractkit

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=smartcontractkit/chainlink)

关注我们，一起探索有意思的开源项目。

