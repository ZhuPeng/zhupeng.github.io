---
layout: post
title: SQL-first 的 Golang ORM
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的软件开发过程中，数据处理一直是一个核心环节，尤其是与数据库的交互。Golang 作为一种高效、静态类型的编程语言，在云原生、微服务等领域深受欢迎。然而，直接使用 Golang 进行数据库操作往往涉及繁琐的代码编写，包括构建 SQL 查询、结果的映射等，增加了开发复杂性和出错几率。

今天要给大家推荐一个 GitHub 开源项目 bun，该项目在 GitHub 有超过 3.4k Star。

![](https://stats.deeptrain.net/repo/uptrace/bun/?theme=light)

一句话介绍该项目：SQL-first Golang ORM

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240619231119129.png)


###### 项目介绍

**Bun** 是一个 SQL-first 的 Golang ORM（对象关系映射），支持 PostgreSQL、MySQL（包括 MariaDB）、MSSQL 和 SQLite。它提供了 ORM 类似的体验，同时又不失去 SQL 的灵活性。**Bun** 主要特点包括支持结构体、映射、标量及其切片的操作；批量插入、更新和删除；数据迁移、软删除等功能。这些特性使得 **Bun** 成为 Golang 开发者处理数据库操作的强有力工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240619231201739.png)

###### 如何使用

首先需要通过 `go get` 命令安装：

```shell
go get github.com/uptrace/bun
```

接着，可以编写如下代码来执行复杂查询并映射结果：

```go
db := bun.NewDB(...)

regionalSales := db.NewSelect().
    ColumnExpr("region").
    ColumnExpr("SUM(amount) AS total_sales").
    TableExpr("orders").
    GroupExpr("region")

var items []map[string]interface{}
err := db.NewSelect().
    With("regional_sales", regionalSales).
    ColumnExpr("region").
    ColumnExpr("product").
    ColumnExpr("SUM(quantity) AS product_units").
    TableExpr("orders").
    GroupExpr("region").
    GroupExpr("product").
    Scan(ctx, &items)
```

通过上述示例，可以看到 **Bun** 如何通过优雅的代码设计来简化复杂查询和结果映射过程，显著提高开发效率。

###### 项目推介

**Bun** 并不孤立于开发生态，它由著名的开源公司 uptrace 提供支持，同时也被多个知名项目采用，例如：在线协作工具 scrumlr.io、分布式追踪和指标平台 uptrace、Kubernetes 访问管理器 paralus 等。这不仅证明了 **Bun** 的实用性，也表示它拥有一个活跃的开发生态和社区支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240619231544313.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=uptrace/bun&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/uptrace/bun 

开源项目作者：uptrace

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=uptrace/bun)

关注我们，一起探索有意思的开源项目。

