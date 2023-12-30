---
layout: post
title: Dolt - Git 和 MySQL 的结合体，提供版本控制的数据管理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在时代进步的同时，大量的数据涌现出来，管理这些数据并存储其变化历史变得越来越复杂，我们需要一个能够记录、追踪和管理数据变更历史的工具。同时，我们还期望这个工具能够像操作 Git 仓库一样方便，使得我们可以轻易地 fork、clone、branch、merge，push 和 pull 等操作。

今天要给大家推荐一个 GitHub 开源项目 dolthub/dolt，该项目在 GitHub 有超过 15.8k Star，用一句话介绍该项目就是：“Dolt – Git for Data”。

![](https://raw.githubusercontent.com/dolthub/dolt/master/./images/Dolt-Logo@3x.svg)

![](https://img.youtube.com/vi/3F6LwZt6e-A/maxresdefault.jpg)

###### 项目介绍

Dolt 是一个 SQL 数据库，不仅能够像 MySQL 数据库一样读取或修改 schema 和数据，还具有版本控制的功能。它的版本控制功能通过 SQL 的系统表、函数和程序进行暴露，还可以像 Git 命令行接口一样进行 CSV 文件的导入，提交更改，向远程推送或合并队友的更改。除此之外，Dolt 还与 DoltHub (https://www.dolthub.com) 配合，提供了数据共享的平台，其中公开数据的托管是免费的。简而言之，Dolt 就像 Git 和 MySQL 的结合体。

以下是对应 Dolt 数据的 SQL Query，可以直接使用 MySQL 相关的语句，同时也支持进行 dolt_checkout、dolt_commit 等类似 Git 的操作，对数据进行不同的版本控制。 

![](https://raw.githubusercontent.com/dolthub/dolt/master/./images/getting-started-new-updates.png)

###### 如何使用

使用如下命令之一可以直接安装 dolt 命令行工具。

```bash
# curl 安装
sudo bash -c 'curl -L https://github.com/dolthub/dolt/releases/latest/download/install.sh | bash'

# Linux 安装
pacman -S dolt

# Mac Homebrew
brew install dolt
```

然后，通过命令行运行 `dolt init` 命令创建一个空的 Dolt 数据仓库，在仓库中运行 `dolt status` 可以查看工作区状态。运行 `dolt add` 可以将表更改添加到预期表更改列表中，`dolt commit` 可以将更改记录到仓库中。开发者还可以通过 `dolt sql` 运行 SQL 查询，或者 `dolt sql-server` 开启一个兼容 MySQL 的服务器。除了这些基本操作，还有许多其他命令供你探索和使用。

###### 项目推介

Dolt 是一款产品级别的开源项目，不仅适用于数据科学家，也适用于需要数据版本控制的开发人员。同时 Dolt 还提供了 Postgres 的版本 DoltgreSQL（https://github.com/dolthub/doltgresql），以及托管 Dolt 服务。这是一个相当有前景的项目，拥有强大的功能和广阔的应用场景。你可以通过 Discord 加入项目的社区，提问或查看项目的 RoadMap 了解我们接下来要做什么。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119223446379.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dolthub/dolt&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dolthub/dolt 

开源项目作者：dolthub

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dolthub/dolt)

关注我们，一起探索有意思的开源项目。

