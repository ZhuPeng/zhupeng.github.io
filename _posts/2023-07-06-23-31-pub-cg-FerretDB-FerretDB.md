---
layout: post
title: FerretDB：一个真正的开源 MongoDB 替代品
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的开发过程中，我们经常遇到使用 MongoDB 的问题。MongoDB 曾经是一项令人惊叹的技术，让我们开发人员能够比使用关系型数据库更快地构建应用程序。然而，随着时间的推移，MongoDB 放弃了它的开源本质，将许可证更改为 SSPL，这使得许多开源项目和早期商业项目无法使用它。大多数 MongoDB 用户并不需要 MongoDB 提供的高级功能，但他们需要一个易于使用的开源文档数据库解决方案。为了填补这个空白，FerretDB 应运而生。

FerretDB 在 GitHub 有超过 7.3k Star，用一句话介绍该项目就是：“A truly Open Source MongoDB alternative”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230813195921355.png)

###### 项目介绍

FerretDB 将 MongoDB 6.0+ 的协议查询转换为 SQL，使用 PostgreSQL 或 SQLite 作为数据库引擎。它旨在成为 MongoDB 的事实开源替代品。FerretDB 兼容 MongoDB 驱动程序和流行的 MongoDB 工具，在许多情况下可以作为 MongoDB 6.0+ 的即插即用替代品。它不断添加功能以进一步提高兼容性和性能。FerretDB 欢迎所有贡献者，你可以在我们的公共路线图、与 MongoDB 的已知差异列表以及贡献指南中获取更多信息。

###### 如何使用

要使用 FerretDB，请按照以下步骤进行安装：

1、使用以下命令以 PostgreSQL 后端启动 FerretDB：

```
docker run -d --rm --name ferretdb -p 27017:27017 ghcr.io/ferretdb/all-in-one
```
或者，使用以下命令以 SQLite 后端启动 FerretDB：
```
docker run -d --rm --name ferretdb -p 27017:27017 \
  -v ./data:/data/ -e FERRETDB_HANDLER=sqlite -e FERRETDB_SQLITE_URL=file:/data/ \
  ghcr.io/ferretdb/all-in-one
```
请注意，这些命令启动的容器中包含了 FerretDB、PostgreSQL 和 MongoDB Shell，方便进行快速测试和实验。然而，这些命令并不适用于生产环境，因为容器在关闭时会丢失所有数据。要了解不会出现这些问题的指令，请参阅项目的 Docker 快速入门指南。

2、当容器运行时，你可以通过以下方式使用 FerretDB：

* 使用任何支持 MongoDB 的客户端应用程序，使用 MongoDB URI `mongodb://127.0.0.1:27017/` 进行连接。

- 使用 MongoDB Shell 进行连接，只需运行 `mongosh` 命令。如果你没有在本地安装，可以使用如下 Docker 命令

```bash
docker exec -it ferretdb mongosh
```

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=FerretDB/FerretDB&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/FerretDB/FerretDB 

开源项目作者：FerretDB

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=FerretDB/FerretDB)

关注我们，一起探索有意思的开源项目。

