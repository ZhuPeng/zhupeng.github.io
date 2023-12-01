---
layout: post
title: GitHub 开源项目 berachain/polaris 介绍，Polaris is a modular implementation of the Ethereum Virtual Machine (EVM). It can be easily integrated into any consensus engine or application, including the Cosmos-SDK.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 berachain/polaris，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Polaris is a modular implementation of the Ethereum Virtual Machine (EVM). It can be easily integrated into any consensus engine or application, including the Cosmos-SDK.”。





背景介绍：在区块链技术蓬勃发展的今天，越来越多的项目寻求借助以太坊虚拟机（EVM）的优越特性如完备的智能合约系统设计，以此来实现项目的特色功能。然而如何将EVM顺畅的集成至项目中成为了一大制约。开发者们需要投入大量的时间和精力才能完成这一硬核任务，而且难度高、易出错。即使如此，实现的效果也常常无法满足需要。因此当下，我们急需一个模块化的EVM实现方案，能够轻松地集成至任何共识引擎或应用中。

项目介绍：[`Polaris（北极星）`](https://github.com/berachain/polaris) 应运而生，它是一款模块化的 EVM 实现方案，旨在为开发者大大简化集成 EVM 至应用中的复杂程度。该项目以几个核心原则为设计指向：
1. **模块化**：每个组件都作为一个独立的包进行开发，都附有全面的测试，文档和基准测试。你可以单独使用这些组件，也可以结合他们创新性地进行 EVM 集成。
2. **可配置性**：Polaris 高度可配置，你可以根据你的具体需求来定制它，以适应更多团队和使用场景。
3. **性能**：Polaris 针对当今热门的加密领域进行了优化，以提供最高级别的性能和效率。
4. **贡献者友好**：Polaris 当前在 BUSL-1.1 下获得许可，计划在接近生产就绪时调整许可证以支持基于贡献者的方案。

如何使用：使用 Polaris 你需要安装 [Golang 1.20+](https://go.dev/doc/install) 和 [Foundry](https://book.getfoundry.sh/getting-started/installation)。具体安装及使用可以按照项目的 README 文件提供的指南来操作，举个例子，如果你想克隆 Polaris 并进行单元测试，你可以按照下面的步骤进行。

```sh
cd $HOME
git clone https://github.com/berachain/polaris
cd polaris
git checkout main
make test-unit
```

项目推介：Polaris 是 BeraChain 的出品，虽然还在早期阶段，但已经有一定的活跃度。结合 BeraChain 在区块链领域的知名度， Polaris 的未来发展值得关注。另外，如果你是 EVM 的使用者或爱好者，如果你对区块链有兴趣，或者你有兴趣参与到这个令人兴奋的开源项目中，Polaris 都是你的理想之选。它将为你提供一个展示才华和实践技术的平台，同时你也将有机会和来自世界各地的优秀开发者共事。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=berachain/polaris&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/berachain/polaris 

开源项目作者：berachain

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=berachain/polaris)

关注我们，一起探索有意思的开源项目。

