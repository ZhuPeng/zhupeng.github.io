---
layout: post
title: GitHub 开源项目 volatiletech/sqlboiler 介绍，Generate a Go ORM tailored to your database schema.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 volatiletech/sqlboiler，该项目在 GitHub 有超过 6.7k Star。

![](https://stats.deeptrain.net/repo/volatiletech/sqlboiler/?theme=light)

一句话介绍该项目：Generate a Go ORM tailored to your database schema.




![sqlboiler logo](https://i.imgur.com/lMXUTPE.png)

![](http://i.imgur.com/SltE8UQ.png)

![](http://i.imgur.com/lzvM5jJ.png)

![](http://i.imgur.com/SS0zNd2.png)

![](http://i.imgur.com/Kk0IM0J.png)

![](http://i.imgur.com/1IFtpdP.png)

![](http://i.imgur.com/t6Usecx.png)

![](http://i.imgur.com/98DOzcr.png)

![](http://i.imgur.com/NSp5r4Q.png)

![](http://i.imgur.com/dEGlOgI.png)


###### 项目介绍

面对快速发展的技术时代，软件开发中的数据持久化是一个核心问题。在处理数据存储时，我们经常需要将数据库中的表和列映射到代码中的结构体和属性，这一过程通常既繁琐又容易出错。传统的 ORM (对象关系映射) 工具虽然提供了一定程度的帮助，但它们往往面临着性能问题、限制灵活性以及对数据库变化的反应不够迅速等挑战。针对 Go 开发环境，这个问题尤为突出，因为 Go 社区内对 ORM 的支持相对较弱，大多数现有的 ORM 框架主要关注代码优先，而非数据库优先，这导致了对于已存在数据库的支持不足。

**SQLBoiler** 应运而生，正是为了解决这些痛点。这是一个开源的 Go ORM 生成工具，其设计理念是“数据库优先”，专门针对您的数据库架构生成 ORM。与常见的“代码优先”ORMs（例如 gorm/gorp）不同，SQLBoiler 要求您首先创建您的数据库模式。这意味着，开发者可以利用如 [sql-migrate](https://github.com/rubenv/sql-migrate) 等迁移工具管理数据库的生命周期，之后通过 SQLBoiler 自动生成与数据库结构高度一致且类型安全的模型代码。

SQLBoiler 彻底解决了开发过程中的重复性代码问题，从根本上增强了 Go 语言处理数据库交互的能力。它具有以下突出特点：

- **完全自动生成模型**：SQLBoiler 能生成完整的模型代码，极大提高开发效率。
- **高性能**：生成的代码执行效率高，且进行了智能缓存处理，与手写 `sql.DB` 代码的性能相当。
- **强类型查询**：支持强类型查询，避免了类型转换的麻烦，使得代码更加安全和清晰。
- **支持钩子函数**：在创建、查询、更新、删除、upsert 时，都可以设置前后钩子，增加了编码的灵活性。
- **关系/关联管理**：将数据库中的关系作为一等公民对待，支持模型间的相关联查询，包括递归的贪婪加载。
- **自定义结构标签**：可以自定义生成模型的结构标签，增加了 ORM 的灵活性。

### 如何使用

使用 SQLBoiler 非常简单。首先，您需要通过 Go 包管理工具安装 SQLBoiler：

```bash
go get -u github.com/volatiletech/sqlboiler/v4
```

接着，您需要为您的数据库创建一个配置文件 `sqlboiler.toml`，指定数据库类型及其连接信息。完成配置后，运行以下命令以根据您的数据库架构生成对应的 Go 模型代码：

```bash
sqlboiler [driver]
```

在这里 `[driver]` 是您使用的数据库驱动的名称，例如 `mysql`、`psql` 等。

生成的 Go 代码将自动包含 CRUD （创建、读取、更新、删除）操作的方法，因此您可以立即开始以类型安全的方式使用这些模型进行数据库交互。

### 项目推介

SQLBoiler 的项目状态非常活跃，具有广泛的社区支持和持续的维护更新。这个项目是由 Go 领域内知名的开发者推动的，得到了许多知名公司和组织的采用，他们借助 SQLBoiler 加速了自己项目的开发进程，并且有效地

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=volatiletech/sqlboiler&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/volatiletech/sqlboiler 

开源项目作者：volatiletech

开源协议：BSD 3-Clause "New" or "Revised" License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=volatiletech/sqlboiler)

关注我们，一起探索有意思的开源项目。

