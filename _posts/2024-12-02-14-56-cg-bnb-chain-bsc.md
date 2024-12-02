---
layout: post
title: GitHub 开源项目 bnb-chain/bsc 介绍，A BNB Smart Chain client based on the go-ethereum fork
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 bnb-chain/bsc，该项目在 GitHub 有超过 2.7k Star。

![](https://stats.deeptrain.net/repo/bnb-chain/bsc/?theme=light)

一句话介绍该项目：A BNB Smart Chain client based on the go-ethereum fork





###### 项目介绍

背景介绍：
随着区块链技术的快速发展，对高性能、高可扩展性的智能合约平台的需求日益增长。传统的区块链网络，如以太坊，虽然提供了强大的智能合约功能，但面临着交易处理速度慢、手续费高等问题，这些问题严重限制了区块链技术在大规模商业应用中的推广。在此背景下，寻找一种既能提供智能合约功能，又能实现快速、低成本交易的区块链平台，成为了区块链社区的重要课题。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-c8a2d989393ca512f1c388b15a5b7535.png)

项目介绍：
**BNB 智能链**（基于 go-ethereum 分叉的 BNB 公链客户端）正是为了解决上述问题而设计。项目的目标是将可编程性和互操作性带入 BNB 信标链（Beacon Chain），并确保与以太坊现有的所有智能合约和工具保持兼容，以发挥已有社区和技术的巨大优势。BNB 智能链通过采用基于股权授权证明（Proof of Staked Authority，PoSA）的 21 个验证器的系统，支持短区块时间和低费用，同时通过双重签名检测和其他斩杀逻辑保障了网络的安全、稳定性和最终一致性。

该链旨在为用户提供：
- 自主治理的区块链平台，通过选举出的验证器确保网络的安全与安全性。
- 与以太坊兼容，支持现有以太坊工具，同时具有更快的最终性和更便宜的交易费用。
- 基于链上治理的分布式系统，PoSA 机制带来去中心化和社区参与度，BNB 作为原生代币，既是智能合约执行的燃料，也是用于质押的代币。

如何使用：
构建源代码前，请确保您的系统安装了 Go（版本 1.21 或更高）和 GCC（5 或更高版本）编译器。构建项目主要通过以下命令：
```shell
make geth
```
该命令将构建主要的 BSC 客户端二进制文件 `geth`。之后，您可以通过 `./build/bin/geth` 命令启动 BNB 智能链节点，连接到主网、测试网或私有网络。

项目推介：
BNB 智能链自推出以来，凭借其与以太坊的兼容性、低交易费用和快速的交易确认时间，在区块链社区获得了广泛的认可。项目得到了活跃的开发支持，源代码频繁更新，反映了强大的开发活跃度和社区支持力度。此外，BNB 智能链支撑着 Binance 生态系统中的众多应用，包括去中心化交易所、金融产品等，已经成为区块链工程师和应用开发者的热门选择。由于其紧密结合 BNB 生态系统并兼容以太坊工具，不仅吸引了大量开发者，也被业界广泛采用，是一款值得信赖且前景广阔的区块链平台。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=bnb-chain/bsc&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/bnb-chain/bsc 

开源项目作者：bnb-chain

开源协议：GNU Lesser General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=bnb-chain/bsc)

关注我们，一起探索有意思的开源项目。

