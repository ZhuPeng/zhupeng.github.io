---
layout: post
title: BlockSuite - 一款开源专注团队协作的编辑器
tags: All
---

大家好，又见面了，我是 GitHub 精选君！

## 背景介绍

在构建协作编辑器项目时，我们经常面临许多问题，例如如何实现实时协作、如何设计一个灵活可扩展的编辑器框架、如何处理复杂的富文本内容等。BlockSuite是一个开源项目，旨在解决这些问题并提供一个功能强大且易于使用的协作编辑器解决方案。

今天要给大家推荐一个 GitHub 开源项目 toeverything/blocksuite，该项目在 GitHub 有超过 2.0k Star，用一句话介绍该项目就是：“🍬 BlockSuite is the open-source collaborative editor project behind AFFiNE.”。

![](https://raw.githubusercontent.com/toeverything/blocksuite/master/assets/logo-and-name-h.svg)



## 项目介绍

BlockSuite是 AFFiNE (https://github.com/toeverything/AFFiNE) 背后的开源编辑器项目，它提供了一个开箱即用的基于块的编辑器，构建在为通用协作应用设计的框架之上。这个项目采用了monorepo结构，同时维护着编辑器和底层框架。

![](https://user-images.githubusercontent.com/79301703/230893796-dc707955-e4e5-4a42-a3c9-18d1ea754f6f.gif)

BlockSuite的特点包括：

- **基于块的编辑**：BlockSuite将富文本内容分解为离散的可编辑块，避免了传统的富文本容器带来的问题。
- **内在协作支持**：通过利用CRDT的强大功能，任何使用BlockSuite构建的应用都可以轻松实现实时协作。
- **框架无关**：使用Web组件实现的UI组件使得BlockSuite的编辑器可以轻松嵌入，并消除了供应商锁定的风险。
- **增量状态同步**：BlockSuite中的状态更新可以按照标准化二进制格式进行增量编码，从而实现在各种网络协议上的高效数据同步。
- **紧凑的富文本**：BlockSuite构建了自己的富文本组件，该组件在块状架构的基础上具有最小的职责，因此它轻巧、简单且可靠。
- **混合无限画布**：BlockSuite还提供了一个基于画布的高性能渲染器，满足白板功能的需求。

详细介绍请参考 https://blocksuite.affine.pro/blocksuite-overview.html 。

## 如何使用
你可以按照以下步骤安装和使用BlockSuite：
1. 克隆项目仓库：`git clone https://github.com/toeverything/blocksuite.git`
2. 进入项目目录：`cd blocksuite`
3. 安装依赖：`pnpm install`
4. 运行示例应用：`pnpm dev`

如果你是一个开发人员，你可以在项目的示例页面 (https://blocksuite-toeverything.vercel.app) 中找到更多示例代码和演示。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=toeverything/blocksuite&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/toeverything/blocksuite 

开源项目作者：toeverything

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=toeverything/blocksuite)

关注我们，一起探索有意思的开源项目。

