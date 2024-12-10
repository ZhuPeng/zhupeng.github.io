---
layout: post
title: 云原生的分布式 SQL 数据库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着应用数据量的增长，企业对数据库的需求已远远超越了传统数据库的处理能力。特别是对于需要高可用性、强一致性、分布式事务支持以及横向扩展能力的场景，传统的关系数据库往往难以胜任。这些核心痛点不仅涉及到数据存储的性能和效率，还涉及到数据的实时处理、故障的自动恢复等多个维度的需求，尤其是在云计算环境中，这些问题显得尤为突出。面对这样的挑战，我们急需一种全新的数据库解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-2ac3aec619211add503259d0da3dce41.png)

今天要给大家推荐一个 GitHub 开源项目 cockroachdb，该项目在 GitHub 有超过 30.2k Star。

![](https://stats.deeptrain.net/repo/cockroachdb/cockroach/?theme=light)

一句话介绍该项目：CockroachDB — the cloud native, distributed SQL database designed for high availability, effortless scale, and control over data placement.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241109174009849.png)

###### 项目介绍

CockroachDB 是一个云原生的分布式 SQL 数据库，旨在为构建、扩展和管理现代、数据密集型应用程序提供解决方案。它基于事务性和强一致性的键值存储构建，能够实现水平扩展，即使在磁盘、机器、机架乃至数据中心发生故障的情况下，也能以最小的延迟中断和无需人工干预自动恢复。CockroachDB 支持强一致性的 ACID 事务，并提供了熟悉的 SQL API 用于结构化、操作和查询数据。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241109174043339.png)

主要特点包括：  

1、横向自动扩展

2、容错与自动故障恢复

3、强一致性的分布式事务

4、PostgreSQL 兼容

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241109174122051.png)

###### 如何使用

可以通过预构建的可执行文件进行安装，或者从源代码构建。安装指南详见：[Install CockroachDB](https://www.cockroachlabs.com/docs/stable/install-cockroachdb.html)。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241109174248538.png)

安装完成后，你可以启动一个临时的本地内存集群，并进行交互式的 SQL 查询。

```shell
cockroach demo

> SELECT ST_IsValid(ST_MakePoint(1,2));
```

为了进一步学习 CockroachDB SQL，你可以参考官方文档：[CockroachDB SQL](https://www.cockroachlabs.com/docs/stable/learn-cockroachdb-sql.html)。

###### 项目推介

CockroachDB 自发布以来，已经得到了广泛的关注和应用。其不仅因为其先进的设计和实现，在技术社区中获得了良好的口碑，同时也因为其开源的社区非常活跃，持续有新的贡献者加入。它被许多知名公司用于生产环境，有效地解决了他们在数据管理、处理和扩展方面的挑战。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241109174638437.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cockroachdb/cockroach&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cockroachdb/cockroach 

开源项目作者：cockroachdb

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cockroachdb/cockroach)

关注我们，一起探索有意思的开源项目。

