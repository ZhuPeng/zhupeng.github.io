---
layout: post
title: 让 Go 语言的 ORM 更加亲近开发者
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代软件开发中，对象关系映射（ORM）框架是连接应用程序与数据库的重要工具，尤其是在使用 Go 语言开发大型应用时。传统的数据操作方式要求开发者撰写大量的 SQL 语句和手动处理数据转换，这不仅耗时耗力，还容易引入错误。此外，随着应用规模的扩大，数据库操作的复杂性上升，对 ORM 框架的需求也日益增长。开发者需要一个功能齐全、易于使用且高效的 ORM 框架，以简化数据库操作，提高开发效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-c19c889b10d6f91c127a6c1d44b74ffc.png)

今天要给大家推荐一个 GitHub 开源项目 gorm，该项目在 GitHub 有超过 36.2k Star。

![](https://stats.deeptrain.net/repo/go-gorm/gorm/?theme=light)

一句话介绍该项目：The fantastic ORM library for Golang, aims to be developer friendly

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240815211814552.png)

###### 项目介绍

GORM 是为 Go 语言设计的一款优秀的 ORM 库，旨在为开发者提供友好的操作体验。它是一个全功能的 ORM 库，支持大多数关联类型如一对一、一对多、多对多、多态关联和单表继承。GORM 还提供了丰富的特性，比如事务处理、嵌套事务、Hooks（在创建、保存、更新、删除、查找前后的操作）、预加载、批量插入等等，几乎满足了现代 Web 应用对数据库操作的所有需求。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240815211846254.png)

除了基本的 ORM 功能，GORM 还特别注重开发者的体验，提供了强大的链式操作，支持自动迁移、详细的日志记录、灵活的插件 API 等，使得它既灵活又强大。无论是单一数据库的场景还是需要读写分离、多数据库支持的复杂场景，GORM 都能够轻松应对。

###### 如何使用

要开始使用 GORM，您首先需要使用 `go get` 来安装它：

```bash
go get -u gorm.io/gorm
```

下面是一个简单的示例，展示如何使用 GORM 进行数据库操作：

```go
package main

import (
  "gorm.io/driver/sqlite"
  "gorm.io/gorm"
)

type Product struct {
  gorm.Model
  Code  string
  Price uint
}

func main() {
  db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
  if err != nil {
    panic("failed to connect database")
  }

  db.AutoMigrate(&Product{})

  db.Create(&Product{Code: "D42", Price: 100})

  var product Product
  db.First(&product, 1) 
  db.First(&product, "code = ?", "D42") 

  db.Model(&product).Update("Price", 200)

  db.Delete(&product)
}
```
###### 项目推介

GORM 自 2013 年以来，一直在不断更新和完善，得益于其活跃的社区和众多贡献者的支持。它是目前 Go 语言社区推荐和广泛使用的 ORM 框架之一。不仅仅因为它强大的功能和灵活性，更因为它始终坚持开发者友好的设计理念。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-gorm/gorm&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-gorm/gorm 

开源项目作者：go-gorm

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-gorm/gorm)

关注我们，一起探索有意思的开源项目。

