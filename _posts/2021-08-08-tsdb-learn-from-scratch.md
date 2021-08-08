---
layout: post
title: 从零开始学习系列之时间序列数据库
tags: Go 相关
---

大家好。

监控系统大家应该都用过，而监控里面记录的比较重要的数据就是某个时间点发生了什么，而用来存储这些数据的数据库，用专业术语讲就是时间序列数据库（Time Series Database，缩写简称 TSDB）。以下是一个更官方的解释：

> 时间序列数据库主要用于指处理带时间标签（按照时间的顺序变化，即时间序列化）的数据，带时间标签的数据也称为时间序列数据。是新型的非关系型数据库，在大数据时代有着十分重要的意义。

Prometheus、InfluxDB、M3、TimescaleDB 都是时下流行的 TSDB。时序数据的压缩算法很大程度上决定了 TSDB 的性能，以上几个项目的实现都参考了 Facebook 2015 年发表的论文《Gorilla: A fast, scalable, in-memory time series database》中提到的差值算法。

今天要推荐的开源项目 mandodb 是一个最小化的 TSDB 实现，从概念上来讲它还算不上是一个完整的 TSDB，因为它：

- 没有实现自己的查询引擎（实现难度大）
- 缺少磁盘归档文件 Compact 操作（天气好的话会实现）
- 没有 WAL 作为灾备保证高可用（心情好的话会实现）

但是 mandodb 的意图是希望完整介绍如何从零开始实现一个小型的 TSDB，希望能给大家带来更多的启发。

mandodb 使用 Go 实现，同时作者也针对 mandodb 提供了如下详尽的用法介绍、设计方案介绍等，其中还包含了对差值算法的讲解，是非常不错的学习资料呢。

![image-20210808211425086](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210808211425086.png)

开源作者的整体文档行文非常的风趣幽默，同时细节讲解也非常的详细，如果你对时间序列数据库感兴趣，推荐你了解一下这个项目，Star 一波绝对不亏。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/chenjiandongx/mandodb
