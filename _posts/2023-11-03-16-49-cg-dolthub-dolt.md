---
layout: post
title: GitHub 开源项目 dolthub/dolt 介绍，Dolt – Git for Data
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 dolthub/dolt，该项目在 GitHub 有超过 15.8k Star，用一句话介绍该项目就是：“Dolt – Git for Data”。


![Dolt Explainer Video](https://img.youtube.com/vi/3F6LwZt6e-A/maxresdefault.jpg)
![Tableplus Connection](https://raw.githubusercontent.com/dolthub/dolt/master/./images/getting-started-tp-connect.png)
![Tableplus](https://raw.githubusercontent.com/dolthub/dolt/master/./images/getting-started-tp.png)
![New Updates](https://raw.githubusercontent.com/dolthub/dolt/master/./images/getting-started-new-updates.png)
![](https://raw.githubusercontent.com/dolthub/dolt/master/./images/Dolt-Logo@3x.svg)



背景介绍：

在时代进步的同时，大量的数据涌现出来，管理这些数据并存储其变化历史变得越来越复杂，我们需要一个能够记录、追踪和管理数据变更历史的工具。同时，我们还期望这个工具能够像操作 Git 仓库一样方便，使得我们可以轻易地 fork、clone、branch、merge，push 和 pull 等操作。这就是我们今天要介绍的开源项目 Dolt。 

项目介绍：

Dolt 是一个 SQL 数据库，不仅能够像 MySQL 数据库一样读取或修改 schema 和数据，还具有版本控制的功能。它的版本控制功能通过 SQL 的系统表、函数和程序进行暴露，还可以像 Git 命令行接口一样进行 CSV 文件的导入，提交更改，向远程推送或合并队友的更改。除此之外，Dolt 还与 [DoltHub](https://www.dolthub.com) 配合，提供了数据共享的平台，其中公开数据的托管是免费的。简而言之，Dolt 就像 Git 和 MySQL 的结合体。

如何使用：

首先，通过命令行运行 `dolt init` 命令创建一个空的 Dolt 数据仓库，在仓库中运行 `dolt status` 可以查看工作区状态。运行 `dolt add` 可以将表更改添加到预期表更改列表中，`dolt commit` 可以将更改记录到仓库中。开发者还可以通过 `dolt sql` 运行 SQL 查询，或者 `dolt sql-server` 开启一个兼容 MySQL 的服务器。除了这些基本操作，还有许多其他命令供你探索和使用。

项目推介：

Dolt 是一款产品级别的开源项目，开发活跃，不仅适用于数据科学家，也适用于需要数据版本控制的开发人员。它提供了 Postgres 版本的 Dolt ，以及托管 Dolt 服务。这是一个相当有前景的项目，拥有强大的功能和广阔的应用场景。快来加入我们，开始你的数据版本控制之旅吧！你也可以通过 [Discord](https://discord.com/invite/RFwfYpu) 加入我们的社区，提问或查看 [我们的路线图](https://docs.dolthub.com/other/roadmap)，了解我们接下来要做什么。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dolthub/dolt&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dolthub/dolt 

开源项目作者：dolthub

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dolthub/dolt)

关注我们，一起探索有意思的开源项目。

