---
layout: post
title: GitHub 开源项目 ethereum/go-ethereum 介绍，Official Go implementation of the Ethereum protocol
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ethereum/go-ethereum，该项目在 GitHub 有超过 45.1k Star，用一句话介绍该项目就是：“Official Go implementation of the Ethereum protocol”。



![Travis](https://app.travis-ci.com/ethereum/go-ethereum.svg?branch=master)



cumentation/rlp)) dumps (data encoding used by the Ethereum to serialize objects) into user-friendlier hierarchical representation.

## Running `geth`

Going through all the possible command line flags is out of scope here (please consult our
[CLI Wiki page](https://geth.ethereum.org/docs/fundamentals/command-line-options)), but we've
enumerated a few common parameter combos to get you up to speed quickly on how you can run
your own `geth` instance.

### Full node on the Ethereum mainnet

```shell
geth
```

### Full node on the Ethereum testnet (Ropsten)

```shell
geth --testnet
```

### Configuration

As an alternative to passing the numerous flags to the `geth` binary, you can also pass a
configuration file via:

```shell
geth --config /path/to/your_config.toml
```

### Docker quick start

One of the quickest ways to get Ethereum up and running on your machine is by using Docker:

```shell
docker run -p 8545:8545 -p 30303:30303 ethereum/client-go
```

## Contribution

Thank you for considering to help out with the source code! We welcome contributions from
anyone on the internet, and are grateful for even the smallest of fixes!

If you'd like to contribute to go-ethereum, please fork, fix, commit and send a pull request
for the maintainers to review and merge into the main code base.

背景介绍：
在区块链领域，以太坊是一种脱俗而出的技术，提供了一个开放的、全球性的去中心化的编程平台，使开发者能够建立和发布智能合约，从而改变互联网应用的开发方式。然而，更能起到敲门砖的是对以太坊协议的理解以及如何在以太坊上编写和执行代码。基于Go的以太坊实现，或称 "geth"，就是这个问题的解决方案。

项目介绍：
以太坊官方 Go 语言实现的以太坊协议，也称为 `geth`，它不仅是我们连接以太坊网络（主网、测试网或私有网）的重要接入点，而且还可以作为全节点（默认）、存档节点（保留所有历史状态）或轻节点（在线获取数据）运行。它还提供了其他进程能够通过 HTTP、WebSocket 和/或 IPC 运输层暴露的 JSON RPC 端点作为通向以太坊网络的网关。此外，它还包括用于与网络层节点交互的实用程序，一种在可配置环境和执行模式下运行字节码片段的 EVM 版本，以及一个可以将二进制 RLP 转换为用户更友好的层次结构表示的工具等等。

如何使用：
要构建 `geth`，需要 Go（版本 1.19 或更高）和C编译器，您可以使用您喜欢的包管理器来安装它们。一旦依赖项安装完成，运行下面的命令：
```shell
make geth
```
或者，构建所有工具集：
```shell
make all
```
你还可以使用 Docker 快速运行以太坊：
```shell
docker run -p 8545:8545 -p 30303:30303 ethereum/client-go
```
项目推介：
`go-ethereum` 是以太坊协议的官方 Go 语言实现，是以太坊开发者社区的集大成者，对于习惯使用 Go 语言的开发者来说，学习和利用该项目将有助于深入理解以太坊的许多内部机制，并能够更好地利用以太坊的各种特性。`go-ethereum` 项目在 GitHub 上已经累积了超过 1 万颗星，开发活跃，更新频繁，对 Issues 反馈也


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ethereum/go-ethereum&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ethereum/go-ethereum 

开源项目作者：ethereum

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ethereum/go-ethereum)

关注我们，一起探索有意思的开源项目。

