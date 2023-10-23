---
layout: post
title: SQLedge - 一个可以在边缘设备上运行的数据同步解决方案
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代的数据驱动的世界中，我们经常会遇到需要在不同的数据库之间复制和同步数据的需求。特别是在边缘计算的场景下，我们需要将数据从中心数据库（如 Postgres）复制到边缘设备上的轻量级数据库（如 SQLite）。然而，这种数据同步的过程可能会遇到各种问题，比如数据一致性问题、网络延迟问题、数据转换问题等。

今天要给大家推荐一个 GitHub 开源项目 zknill/sqledge，该项目在 GitHub 有超过 896 Star，用一句话介绍该项目就是：“Replicate postgres to SQLite on the edge”。


![](https://github.com/zknill/sqledge/blob/main/etc/sqledge.png?raw=true)

###### 项目介绍

SQLedge 使用 Postgres 的逻辑复制功能，将源 Postgres 数据库中的更改实时流式传输到可以在边缘运行的 SQLite 数据库。SQLedge 从其本地 SQLite 数据库提供读取服务，并将写入操作转发到它正在复制的上游 Postgres 服务器。这使得你可以在边缘运行你的应用，并且可以本地、快速、最终一致地访问你的数据，速度和一致性兼得。

###### 如何使用

首先，你需要在 Postgres 数据库中创建一个数据库和一个用户，然后运行示例代码，连接到 Postgres 代理服务器，创建表并插入数据。然后，你可以连接到本地的 SQLite 数据库，查看表结构和数据。所有的配置信息都是从环境变量中读取的，完整的列表可以在 pkg/config/config.go 文件中找到。详细步骤参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230910214515023.png)

###### 项目推介

SQLedge 项目目前处于 alpha 状态，但已经具备了基本的功能，可以满足大部分的数据同步需求。它的设计理念是简洁和高效，通过使用 Postgres 的逻辑复制和 SQLite 的轻量级特性，实现了在边缘设备上的数据同步。此外，SQLedge 项目的代码质量高，易于理解和修改，非常适合开源社区的开发者参与和贡献。如果你正在寻找一个可以在边缘设备上运行的数据同步解决方案，SQLedge 项目绝对值得你一试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=zknill/sqledge&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/zknill/sqledge 

开源项目作者：zknill

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=zknill/sqledge)

关注我们，一起探索有意思的开源项目。

