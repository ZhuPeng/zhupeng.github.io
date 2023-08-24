---
layout: post
title: GitHub 开源项目 PeerDB-io/peerdb 介绍，Postgres first ETL/ELT, enabling 10x faster data movement in and out of Postgres 🐘 🚀
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 PeerDB-io/peerdb，该项目在 GitHub 有超过 955 Star，用一句话介绍该项目就是：“Postgres first ETL/ELT, enabling 10x faster data movement in and out of Postgres 🐘 🚀”。


![](https://raw.githubusercontent.com/PeerDB-io/peerdb/master/images/banner.jpg)
![](https://raw.githubusercontent.com/PeerDB-io/peerdb/master/images/peerdb-demo.gif)



背景介绍：
在数据处理过程中，我们经常需要将数据从一个数据库迁移到另一个数据库。然而，这个过程通常非常耗时，特别是当数据量很大时。此外，现有的数据工具通常忽略了Postgres用户的需求，这使得Postgres用户需要自己构建定制的管道来满足自己的需求。因此，我们需要一个专门为Postgres用户提供简单可靠的数据迁移解决方案的开源项目。

项目介绍：
PeerDB是一个Postgres-first数据迁移平台，它可以快速简单地将数据移动到和从Postgres中。它使用简单的SQL命令来同步、转换和查询数据。PeerDB实现了多个Postgres本地和基础设施优化，使得数据在PostgreSQL中的移动速度提高了10倍。

PeerDB可以用于以下任何用例：
1. 从PostgreSQL实时捕获更改数据。
2. 在数据存储之间实时流式传输查询结果。
3. 联合查询工作负载-通过一个公共的SQL接口查询多个数据存储。

PeerDB的主要功能包括：
- Postgres-first方法：PeerDB是一个专门为Postgres用户设计的ETL/ELT工具。它实现了多个Postgres本地和基础设施优化，以提供快速、可靠和功能丰富的数据移动体验。
- 可靠性：PeerDB具有故障容错机制，包括状态管理、自动重试、处理幂等性和一致性等。可配置的批处理和并行处理可以防止内存不足和崩溃。
- 功能丰富：PeerDB支持大型（TOAST）列的高效同步。它支持多种流式传输模式-基于日志的（CDC）流式传输、基于查询的流式传输等。它提供了丰富的数据类型映射，并计划在目标数据存储上尽可能支持Postgres支持的每种可能的数据类型（包括自定义类型）。

如何使用：
您可以使用以下步骤来开始使用PeerDB：
1. 克隆代码：git clone --recursive git@github.com:PeerDB-io/peerdb.git
2. 运行docker容器：peerdb-server、postgres作为目录、时间序列
3. 连接到PeerDB并查询：psql "port=9900 host=localhost password=peerdb"
您可以按照5分钟快速入门指南来了解PeerDB的使用方法，即实时在存储之间流式传输数据。

项目推介：
PeerDB是一个非常优秀的开源项目，它专门为Postgres用户提供了简单可靠的数据迁移解决方案。PeerDB实现了多个Postgres本地和基础设施优化，使得数据在PostgreSQL中的移动速度提高了10倍。PeerDB的开发活跃，已经有很多知名用户和公司在使用它。如果您是Postgres用户，PeerDB绝对是您不可错过的一个工具。






以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=PeerDB-io/peerdb&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/PeerDB-io/peerdb 

开源项目作者：PeerDB-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=PeerDB-io/peerdb)

关注我们，一起探索有意思的开源项目。

