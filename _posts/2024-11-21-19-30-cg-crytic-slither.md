---
layout: post
title: GitHub 开源项目 crytic/slither 介绍，Static Analyzer for Solidity and Vyper
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 crytic/slither，该项目在 GitHub 有超过 5.3k Star。

![](https://stats.deeptrain.net/repo/crytic/slither/?theme=light)

一句话介绍该项目：Static Analyzer for Solidity and Vyper




![](https://raw.githubusercontent.com/crytic/slither/master/logo.png)


###### 项目介绍

背景介绍：
在区块链开发中，智能合约的安全性至关重要。智能合约一旦部署上链，就无法修改，任何安全漏洞都可能导致重大财产损失。随着区块链技术的发展，Solidity 和 Vyper 成为了开发以太坊智能合约的主要编程语言。然而，即使是最经验丰富的开发者，也难以保证其编写的智能合约代码完全没有安全漏洞。因此，智能合约的静态分析工具成为了开发中不可或缺的一环，帮助开发者在合约部署前发现并修复潜在的安全问题。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1709592ae372c9eb4281d7b2fc43a3ae.png)

项目介绍：
**Slither** 是一个为 Solidity 和 Vyper 编写的智能合约静态分析框架，使用 Python3 实现。它能够运行一系列的漏洞检测程序，打印关于合约详情的可视化信息，并提供了一个 API，使开发者能够轻松编写自定义分析。Slither 使开发者能够发现漏洞，加深对代码的理解，以及快速原型自定义分析。该项目的特点包括：低误报的脆弱性代码检测、源代码中错误条件的精准定位、易于集成到持续集成和硬帽/铸造构建中、内置“打印机”快速报告重要合约信息、支持自定义分析的检测器 API 以及对 Solidity 版本高达 0.4 的合约分析能力。

如何使用：
安装 Slither 可以通过 pip、Git 或 Docker 进行。例如，使用 pip 的安装命令如下：
```console
python3 -m pip install slither-analyzer
```
使用 Slither 检查一个 Hardhat/Foundry/Dapp/Brownie 应用，可以简单执行：
```console
slither .
```
如果需要对不含依赖项的单个文件进行检查，可以执行：
```console
slither tests/uninitialized.sol
```

项目推介：
Slither 由 Trail of Bits 维护，这是一家知名的安全公司，代表着项目的高质量和专业性。自推出以来，Slither 成功地在多个项目中发现了安全漏洞，证明了其有效性和实用性。作为一个持续更新且活跃的项目，它支持最新版本的 Solidity 和 Vyper，确保了对新兴智能合约技术的广泛兼容性。Slither 已经集成到 GitHub 的代码扫描中，使其更容易为广大开发者所采纳和使用。无论您是智能合约的开发者，还是安全审计人员，Slither 都是提升您智能合约安全性的强大工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=crytic/slither&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/crytic/slither 

开源项目作者：crytic

开源协议：GNU Affero General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=crytic/slither)

关注我们，一起探索有意思的开源项目。

