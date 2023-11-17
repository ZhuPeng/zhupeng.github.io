---
layout: post
title: GitHub 开源项目 dolthub/doltgresql 介绍，DoltgreSQL - Version Controlled PostgreSQL
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 dolthub/doltgresql，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“DoltgreSQL - Version Controlled PostgreSQL”。



你是否在日常的数据库操作中感受到版本控制的需求？是否想为你的 PostgreSQL 数据库增添 Git 类似的日志，分支，合并等功能？是否想采用你熟悉的 PostgreSQL 客户端和 PostgreSQL SQL，而不是 MySQL 客户端和 MySQL SQL 进行操作？那么，你的需求，[DoltgreSQL](https://github.com/dolthub/doltgresql) 完全可以搞定。

DoltgreSQL 是 Dolt 的 PostgreSQL 版本。Dolt 是世界上首个提供版本控制的 SQL 数据库。DoltgreSQL 以一种全新的方式提供所有你期望的 Git 功能，包括日志，diff，分支，合并等，这些都可以放在你的 PostgreSQL 数据库模式和数据上。DoltgreSQL 就像 Git 和 PostgreSQL 的孩子。

在包含大量动态和不断推进的数据项目中，如何做数据的版本控制？这一问题在 Dolt 的设计初衷已经得到了探索，Dolt 最初被设计成为 [Git for Data](https://www.dolthub.com/blog/2020-03-06-so-you-want-git-for-data/)，后来变成了一个 [version controlled database](https://www.dolthub.com/blog/2021-09-17-database-version-control/)，这就是 Dolt 和 DoltgreSQL 的秘诀。

使用 DoltgreSQL 非常简单，你只需要下载最新版本的 `doltgres`，将 `doltgres` 放在你的 `PATH` 下，然后在你希望存储数据库数据的目录下运行 `doltgres`，就可以创建一个 `doltgres` 用户和一个 `doltgres` 数据库。当然，你需要确保你安装的 Postgres 版本是15或更高的版本。然后，就可以使用命令：`psql -h localhost -U doltgres` 进行连接了。

这个项目的 README 提供了详细的使用教程，让你可以很快将这个有趣的工具运用到你的项目中。这个项目当前处于开发初期阶段，热烈欢迎你的反馈，你的反馈将会直接影响项目的开发方向。如果你对使用 DoltgreSQL 有兴趣，建议你点赞这个项目库，尝试使用 DoltgreSQL，并在发现问题或功能缺失时在 GitHub 提交 Issue。

Dolt 是一个已经完成 1.0 版本的生产级的有版本控制的数据库。如果你对于使用 MySQL 客户端没有抵触感，我们建议你对所有用例都使用 Dolt。但是如果你更喜欢 PostgreSQL，DoltgreSQL 将是你的首选。





以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dolthub/doltgresql&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dolthub/doltgresql 

开源项目作者：dolthub

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dolthub/doltgresql)

关注我们，一起探索有意思的开源项目。