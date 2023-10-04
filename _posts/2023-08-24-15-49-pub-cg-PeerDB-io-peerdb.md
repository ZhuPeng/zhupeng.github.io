---
layout: post
title: PeerDB - 一个专为 Postgres 设计的数据迁移平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数据处理过程中，我们经常需要将数据从一个数据库迁移到另一个数据库。然而，这个过程通常非常耗时，特别是当数据量很大时。此外，现有的数据工具通常忽略了 Postgres 用户的需求，这使得 Postgres 用户需要自己构建定制的管道来满足自己的需求。因此，我们需要一个专门为 Postgres 用户提供简单可靠的数据迁移解决方案的开源项目。

PeerDB 项目在 GitHub 差不多 1000 Star，用一句话介绍该项目就是：“Postgres first ETL/ELT, enabling 10x faster data movement in and out of Postgres”。

![](https://raw.githubusercontent.com/PeerDB-io/peerdb/master/images/banner.jpg)

###### 项目介绍

PeerDB 是一个 Postgres-first 数据迁移平台，它可以快速简单地将数据移动到从 Postgres 中。它使用简单的 SQL 命令来同步、转换和查询数据。PeerDB 实现了多个 Postgres 本地和基础设施优化，使得数据在 PostgreSQL 中的移动速度提高了 10 倍。

PeerDB 可以用于以下任何用例：

1、从 PostgreSQL 实时捕获更改数据。

2、在数据存储之间实时流式传输查询结果。

3、联合查询工作负载-通过一个公共的SQL接口查询多个数据存储。

以下是一个使用 DEMO：

![](https://raw.githubusercontent.com/PeerDB-io/peerdb/master/images/peerdb-demo.gif)

PeerDB 的主要设计点如下：

- Postgres-first方法：PeerDB 是一个专门为 Postgres 用户设计的 ETL/ELT 工具。它实现了多个 Postgres 本地和基础设施优化，以提供快速、可靠和功能丰富的数据移动体验。
- 可靠性：PeerDB 具有故障容错机制，包括状态管理、自动重试、处理幂等性和一致性等。可配置的批处理和并行处理可以防止内存不足和崩溃。
- 功能丰富：PeerDB 支持大型（TOAST）列的高效同步。它支持多种流式传输模式-基于日志的（CDC）流式传输、基于查询的流式传输等。它提供了丰富的数据类型映射，并计划在目标数据存储上尽可能支持Postgres支持的每种可能的数据类型（包括自定义类型）。

###### 如何使用

您可以使用以下步骤来开始使用 PeerDB：

```bash
git clone --recursive git@github.com:PeerDB-io/peerdb.git
cd peerdb

# Run docker containers: peerdb-server, postgres as catalog, temporal
export COMPOSE_PROJECT_NAME=peerdb-stack
docker compose up

# connect to peerdb and query away
psql "port=9900 host=localhost password=peerdb"
```

###### 项目推介

PeerDB 是一个非常优秀的开源项目，它专门为 Postgres 用户提供了简单可靠的数据迁移解决方案。PeerDB 实现了多个Postgres本地和基础设施优化，使得数据在 PostgreSQL 中的移动速度提高了 10 倍。PeerDB 的开发活跃，如果您是 Postgres 用户，PeerDB 绝对是您不可错过的一个工具。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=PeerDB-io/peerdb&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/PeerDB-io/peerdb 

开源项目作者：PeerDB-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=PeerDB-io/peerdb)

关注我们，一起探索有意思的开源项目。

