---
layout: post
title: 支持无感水平扩展的 MySQL 集群
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的互联网技术环境中，数据日益膨胀，企业和开发者们面临的一个显著问题是如何有效地扩展数据库（比如 MySQL）以应对业务增长的需求。传统的垂直扩展方法（即升级服务器硬件）成本高昂且有其物理极限，而水平扩展（增加更多服务器）的复杂性让很多团队望而却步。具体来说，水平扩展常常涉及到数据库分片的问题，这不仅需要对现有架构进行大幅度修改，而且还需要应用代码能够智能地处理分布在多个分片上的数据。这些工作通常是耗时且容易出错的，特别是数据库分片、迁移和扩容等操作，都需要精密的计划和执行。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-e2799b274ed8116e9a291329acd2859b.png)

今天要给大家推荐一个 GitHub 开源项目 vitess，该项目在 GitHub 有超过 18.8k Star。

![](https://stats.deeptrain.net/repo/vitessio/vitess/?theme=light)

一句话介绍该项目：Vitess is a database clustering system for horizontal scaling of MySQL.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234246235.png)

###### 项目介绍

Vitess 是一个专为 MySQL 设计的数据库集群系统，支持通过广义分片进行水平扩展。Vitess 能够封装分片路由逻辑，使应用代码及数据库查询对数据的分布方式透明无感。最重要的是，Vitess 支持在数据需求增长时进行分片的分裂和合并操作，并能在几秒内完成原子切换，大大降低了管理和扩展分布式数据库的复杂度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234316698.png)

自 2011 年起，Vitess 就成为了 YouTube 数据库架构的核心组成部分，并已扩展至数以万计的 MySQL 节点。透过访问 [vitess.io](https://vitess.io)，可以了解更多关于 Vitess 的信息。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234403629.png)

###### 如何使用

安装方式支持 Kubernetes 和本地安装。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234535447.png)

使用 Kubernetes 可以使用如下命令快速安装对应的 Operator。

```shell
git clone https://github.com/vitessio/vitess
cd vitess/examples/operator
git checkout release-21.0
kubectl apply -f operator.yaml

```

然后即可快速启动一个数据库集群：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234737689.png)

然后你就可以像直接使用 MySQL 一样使用这个数据库了。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234853523.png)

###### 项目推介

Vitess 不仅在 YouTube 得到广泛应用，还吸引了包括 Slack、Square、GitHub 等多家知名公司的关注和使用。项目的持续活跃状态，以及由 Cloud Native Computing Foundation (CNCF) 进行管理，都说明了其在业界的权威性和可靠性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215234953293.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=vitessio/vitess&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/vitessio/vitess

开源项目作者：vitessio

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=vitessio/vitess)

关注我们，一起探索有意思的开源项目。

