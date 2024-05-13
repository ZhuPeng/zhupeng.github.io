---
layout: post
title: GitHub 开源项目 ledgerwatch/erigon 介绍，Ethereum implementation on the efficiency frontier
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 ledgerwatch/erigon，该项目在 GitHub 有超过 3.0k Star。

![](https://stats.deeptrain.net/repo/ledgerwatch/erigon)

一句话介绍该项目：Ethereum implementation on the efficiency frontier





###### 项目介绍

### 背景介绍

对于开发者和企业来说，构建和运行高性能的 Ethereum 节点始终是一个充满挑战的任务。随着区块链的不断成长和交易量的增加，节点必须处理大量的数据才能保持同步，这在很大程度上提高了存储空间、处理速度和效率的要求。传统的 Ethereum 实现方案可能难以满足当前市场对于速度、效率和可扩展性的需求，特别是对于大规模操作的企业级应用而言。此外，全节点和归档节点的运营成本也成为了一个不容忽视的问题，这对于希望更高效地参与 Ethereum 网络的用户来说，是一个核心痛点。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-fb41a96cbbd86e39eeb8b26688f74101.png)

项目介绍

Erigon 是一个高效前沿的 Ethereum 实现（执行层与可嵌入的共识层），默认为 [归档节点](https://ethereum.org/en/developers/docs/nodes-and-clients/archive-nodes/#what-is-an-archive-node)。Erigon 通过多种方式优化了 Ethereum 的存储和同步过程，包括更高效的状态存储、更快的初始同步速度，并提供了一个 JSON-RPC 守护进程。此外，Erigon 还支持通过 Docker Compose 来运行所有组件，并提供了 Grafana 仪表板用于实时监控数据。它还集成了 Caplin（内部共识层），为用户提供了一个全面而高效的 Ethereum 节点解决方案。

### 如何使用

要开始使用 Erigon，您可以通过下面的步骤来构建最新的发布版本：

```
git clone --branch release/ --single-branch https://github.com/ledgerwatch/erigon.git
cd erigon
make erigon
./build/bin/erigon
```

此外，您还可以选择构建开发版以获取最新的功能：

```
git clone --recurse-submodules https://github.com/ledgerwatch/erigon.git
cd erigon
git checkout main
make erigon
./build/bin/erigon
```

Erigon 允许用户通过 `--datadir` 来选择数据的存储位置，并通过不同的命令行选项来配置节点的运行环境，使其适用于各种场景，从私有链到主网不等。

### 项目推介

Erigon 不仅因其技术创新而备受关注，而且由于其开源和社区驱动的特性，拥有一个活跃的开发和用户社区。该项目由 Ledgerwatch 团队领导，这是一支在 Ethereum 生态系统中颇具声望的技术团队，他们长期致力于提高 Ethereum 的性能和效率。Erigon 因其卓越的性能和创新的技术解决方案已被多个知名组织使用，包括但不限于使用 Ethereum 网络的企业和开发者。凭借其优化的存储解决方案、快速的初始化同步和灵活的配置选项，Erigon 成为了一个理想的选择，尤其是对于那些寻求高效 Ethereum 节点操作的高级用户和企业。加之其详尽的文档和活跃的 Discord 社区，新用户也能够轻松上手并获得支持。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ledgerwatch/erigon&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ledgerwatch/erigon 

开源项目作者：ledgerwatch

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ledgerwatch/erigon)

关注我们，一起探索有意思的开源项目。

