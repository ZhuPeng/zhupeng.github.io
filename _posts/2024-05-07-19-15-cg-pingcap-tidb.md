---
layout: post
title: 一个开源的、云原生的、分布式 SQL 数据库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数字化时代，数据量呈现出爆炸性增长，企业和开发者面对的是如何高效、灵活地处理和分析这些数据的挑战。常规的数据库系统在处理超大规模数据、实时分析和高并发请求时面临性能瓶颈，尤其是在云环境和分布式应用场景下。同时，业务快速迭代要求数据库系统不仅要保证数据的强一致性和高可用性，还需要能够无缝扩展，支持复杂的事务和分析型查询，这就使得传统的数据库解决方案难以满足现代应用的需求。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-70b805ef460bf353dc6ebe4c7de0fcbb.png)

今天要给大家推荐一个 GitHub 开源项目 tidb，该项目在 GitHub 有超过 36.2k Star，一句话介绍该项目：TiDB is an open-source, cloud-native, distributed, MySQL-Compatible database for elastic scale and real-time analytics. 

![](https://raw.githubusercontent.com/pingcap/tidb/master/docs/tidb-logo-with-text.png)

###### 项目介绍

TiDB 是一个开源的、云原生的、分布式 SQL 数据库，旨在支持混合事务和分析处理（HTAP）工作负载。它与 MySQL 兼容，具备水平扩展、强一致性和高可用性的特点。TiDB 为用户提供了灵活、无缝的数据处理能力，特别适合需要处理海量数据、要求实时分析及高并发访问的场景。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240511230238516.png)

1、主要特性：TiDB 支持自动分片、数据强一致性保证、分布式事务处理，在不牺牲性能的前提下实现数据的高度可用。

2、架构设计：TiDB 采用了分布式架构，包括 TiDB 节点负责 SQL 层处理，TiKV 节点处理存储，以及 PD 节点确保集群的稳定运行和数据均衡。

![](https://raw.githubusercontent.com/pingcap/tidb/master/./docs/tidb-architecture.png)

3、MySQL 兼容性：对 MySQL 生态圈有很好的兼容性，用户可以非常容易地迁移现有的应用到 TiDB，而不需要改动代码。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240511230249108.png)

###### 如何使用

有如下几种使用方式：

1、TiDB Cloud：完全托管的 TiDB 服务版本，支持 AWS 和 GCP。用户可以通过访问 [TiDB Cloud 官网](https://tidbcloud.com/free-trial) 进行免费试用。

```bash
# Visit TiDB Cloud
https://tidbcloud.com/free-trial
```

2、本地快速开始：用户可以通过访问 [TiDB 快速开始指南](https://docs.pingcap.com/tidb/stable/quick-start-with-tidb) 来在本地部署和使用 TiDB。

```bash
# local install quick start
https://docs.pingcap.com/tidb/stable/quick-start-with-tidb
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240511230447908.png)

###### 项目推介

TiDB 由 PingCAP 发起并维护，是一个活跃的开源项目，拥有强大的社区支持。该项目不仅吸引了世界各地的贡献者，还得到了包括华为、银联等在内的众多知名公司的使用和认可，其高效和稳定已经在生产环境中得到了验证。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pingcap/tidb&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pingcap/tidb 

开源项目作者：pingcap

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pingcap/tidb)

关注我们，一起探索有意思的开源项目。

