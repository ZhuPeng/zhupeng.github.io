---
layout: post
title: ScratchDB - 一个简单易用可直接处理 JSON 数据的数据库系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在大数据时代，我们经常会遇到需要处理大量的 JSON 数据并进行分析查询的需求。然而，传统的数据库系统如 BigQuery、Redshift、Snowflake 等，虽然功能强大，但是使用起来可能会有一些复杂，同时也需要承担一定的成本。如果你正在寻找一个开源的、易用的、能够处理大量 JSON 数据的数据库系统，不妨看看今天的项目的推荐。

今天要给大家推荐一个 GitHub 开源项目 scratchdata/ScratchDB，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Scratch is an open-source alternative to BigQuery, Redshift, and Snowflake. Runs on Clickhouse.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104233638771.png)

###### 项目介绍

ScratchDB 是一个开源的数据库系统，它是基于 Clickhouse 构建的，可以让你输入任意的 JSON 数据，并对其进行分析查询。当有新的数据添加时，它会自动创建表和列。ScratchDB 的设计目标是提供一个简单易用、功能强大的数据分析工具，让你可以更加方便地处理和分析大量的 JSON 数据。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104233715311.png)

###### 如何使用

使用 ScratchDB 非常简单。首先，你需要克隆项目的代码库，然后启动 Clickhouse 和 localstack，参考命令如下：

```bash
$ git clone git@github.com:scratchdata/ScratchDB.git
$ cd ScratchDB

# 对应的 compose 描述服务包含 clickhouse 和 localstack
$ docker-compose up
```

接着，分别在两个单独的命令行终端中启动 insert 和 ingest 服务。

```bash
# 启动 insert 服务
$ go run . insert

# 启动 ingest 服务
$ go run . ingest
```

然后，你就可以通过 POST 请求向服务器发送 JSON 数据了。

```bash
$ curl -X POST http://localhost:3000/data \
    -H 'Content-Type: application/json' \
    -H 'X-Api-Key: local' \
    -d '{"table":"my_table","data":{"fruit": "apple"}}'
```

查询数据也非常简单，你只需要发送一个 GET 请求，就可以在 JSON 格式或者 HTML 表格格式中查看数据。

```bash
# 对应查询 my_table 中的所有数据，http://localhost:3000/query?q=select * from my_table，返回默认都是 JSON 格式；如果要使用 HTML 格式可添加参数 format=html
curl -H 'X-Api-Key: local' "http://localhost:3000/query?q=select%20*%20from%20my_table"
```

###### 项目推介

ScratchDB 有单独的博客介绍如何更好的使用 ScratchDB，同时 [Embeddables](https://www.embeddables.com/) 公司已经在使用该项目。如果你正在寻找一个开源的、易用的、能够处理大量 JSON 数据的数据库系统，那么 ScratchDB 绝对值得你尝试。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104234429384.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=scratchdata/ScratchDB&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/scratchdata/ScratchDB 

开源项目作者：scratchdata

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=scratchdata/ScratchDB)

关注我们，一起探索有意思的开源项目。

