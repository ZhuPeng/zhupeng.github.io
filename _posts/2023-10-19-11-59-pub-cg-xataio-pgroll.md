---
layout: post
title: pgroll - 为 PostgreSQL 提供安全零宕机且可逆的数据库迁移方案
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在 PostgreSQL 数据库的日常运维中，我们常常会遇到需要进行数据库迁移的情况。然而，传统的数据库迁移方式往往需要停机，这对于需要 24 小时不间断运行的业务来说，无疑是一种巨大的困扰。另外，如果迁移过程中出现问题，往往需要花费大量的时间和精力来进行回滚，这无疑增加了运维的难度和风险。因此，如何实现零停机时间的数据库迁移，以及如何快速回滚迁移操作，成为了我们面临的核心问题。

今天要给大家推荐一个 GitHub 开源项目 xataio/pgroll，该项目在 GitHub 有超过 1.2k Star，用一句话介绍该项目就是：“PostgreSQL zero-downtime migrations made easy”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029204628153.png)

###### 项目介绍

pgroll 为 PostgreSQL 提供了安全且可逆的数据库迁移方案。pgroll 通过同时提供多个版本的数据库模式，确保在数据库模式更新的同时，客户端应用程序可以继续运行。这包括确保更改在不锁定数据库的情况下应用，以及新旧模式版本可以同时工作（即使在进行破坏性更改时！）。这消除了与模式迁移相关的风险，并大大简化了客户端应用程序的推出，同时也允许即时回滚。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029204809271.png)

整体迁移流程图参考如下：

![](https://raw.githubusercontent.com/xataio/pgroll/master/docs/img/migration-flow@2x.png)

存在 Schema 变更的迁移场景：

![](https://raw.githubusercontent.com/xataio/pgroll/master/docs/img/migration-schemas@2x.png?c=0)

###### 如何使用

pgroll 的安装非常简单，只需要运行以下命令：

    go install github.com/xataio/pgroll@latest

注意：需要 Go 1.21 或更高版本。

pgroll 的使用也非常简单，它通过创建物理表上的视图来创建虚拟模式。这允许在不影响现有客户端的情况下执行迁移所需的所有更改。pgroll 遵循扩展/收缩工作流。在迁移开始时，它将在物理模式中执行所有的添加更改（创建表，添加列等），而不会破坏它。

###### 项目推介

pgroll 不仅可以帮助我们实现零停机时间的数据库迁移，还可以在迁移过程中出现问题时，快速进行回滚。这无疑为我们的数据库运维工作提供了极大的便利。因此，我强烈推荐大家使用 pgroll 这个项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=xataio/pgroll&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/xataio/pgroll 

开源项目作者：xataio

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=xataio/pgroll)

关注我们，一起探索有意思的开源项目。

