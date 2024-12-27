---
layout: post
title: GitHub 开源项目 Masterminds/squirrel 介绍，Fluent SQL generation for golang
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 Masterminds/squirrel，该项目在 GitHub 有超过 7.1k Star。

![](https://stats.deeptrain.net/repo/Masterminds/squirrel/?theme=light)

一句话介绍该项目：Fluent SQL generation for golang




![Stability: Maintenance](https://masterminds.github.io/stability/maintenance.svg)


###### 项目介绍

背景介绍：
在当代的软件开发过程中，数据驱动的应用变得越来越普遍，其中 SQL 数据库的使用是不可避免的一个环节。然而，构建 SQL 查询语句往往是一个繁琐并且错误率相对较高的任务，特别是在复杂的查询场景中。传统的字符串拼接方法不仅代码难以维护，也容易引发 SQL 注入等安全问题。此外，随着应用规模的扩展，对 SQL 查询的构建提出了更高的要求，如代码的可读性、可维护性以及安全性。因此，开发者迫切需要一个能够简化 SQL 查询构建过程的工具，以提高开发效率和保障代码的质量。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1a81d0a55876f0573da6404b8c25862e.png)

项目介绍：
针对以上提到的问题，[Squirrel](https://github.com/Masterminds/squirrel) 应运而生。Squirrel 是一个为 Go 语言设计的流畅（Fluent）SQL 生成器，它通过提供一系列易于理解的 API，帮助开发者更加便捷地构建 SQL 查询，而无需拼接字符串。该项目不是一个 ORM（对象关系映射）工具，但能以高效、安全的方式解决 SQL 查询构建的问题。主要特点包括：

- **易用性**：Squirrel 通过链式调用的方式，使 SQL 语句的构建如同自然语言一般直观。
- **灵活性**：它支持构建几乎所有类型的 SQL 语句，并且能够灵活地构造复杂的查询条件。
- **安全性**：通过避免直接的字符串拼接，Squirrel 能有效预防 SQL 注入攻击。
- **良好的 PostgreSQL 支持**：Squirrel 特别优化了对 PostgreSQL 的支持，包括占位符格式的转换等。

如何使用：
要使用 Squirrel 构建 SQL 语句，首先需要通过 Go 的包管理工具安装：

```go
import "github.com/Masterminds/squirrel"
```

接着，你可以利用 Squirrel 提供的 API 进行 SQL 语句的构建。例如，构建一个简单的查询语句：

```go
sql, args, err := squirrel.Select("*").From("users").Where(squirrel.Eq{"name": "mike"}).ToSql()

// sql: SELECT * FROM users WHERE name = ?
```

更复杂的查询，如插入操作，也可以简单实现：

```go
sql, args, err := squirrel.
    Insert("users").Columns("name", "age").
    Values("John", 30).
    ToSql()

// sql: INSERT INTO users (name, age) VALUES (?, ?)
```

项目推介：
Squirrel 是一个已经完成且正在维护的项目，虽然作者指出不会主动添加新功能，但对于 bug 修复仍然保持开放。其流畅的接口和强大的功能使其成为 Go 语言环境下构建 SQL 查询的首选库。目前，它已被多个知名项目和公司采用，得到了社区的广泛认可。对于追求代码质量与开发效率的团队和个人而言，Squirrel 提供了一个既简单又强大的解决方案，帮助开发者避免直接拼接 SQL 语句带来的种种问题，并提升开发体验。尽管文档可能在某些方面不够完善，但其丰富的测试用例为开发者提供了另一种形式的“文档”，帮助理解和使用这个库。如果你正在使用 Go 进行数据库操作，Squirrel 绝对值得一试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Masterminds/squirrel&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Masterminds/squirrel 

开源项目作者：Masterminds

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Masterminds/squirrel)

关注我们，一起探索有意思的开源项目。

