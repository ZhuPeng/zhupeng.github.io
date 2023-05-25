---
layout: post
title: 纯 Go 编写的轻量级文档 NoSQL 数据库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ostafen/clover，该项目在 GitHub 有超过 300 Star，用一句话介绍该项目就是：“A lightweight document-oriented NoSQL database written in pure Golang.”，一个使用纯 Go 编写的轻量级基于文档的 NoSQL 数据库。

![](https://raw.githubusercontent.com/ostafen/clover/master/.github/logo.png#gh-light-mode-only)

clover 是一个轻量级的 NoSQL 数据库，由于它的代码库很小，所以设计得简单且易于维护。它的灵感来自 [tinyDB](https://github.com/msiemens/tinydb)。编写**CloverDB** 是为了使其易于维护。因此，它以简单性换取性能，并不是为了替代性能更好的数据库，如 **MongoDB**或 **MySQL**。然而，在有些项目中，运行单独的数据库服务器可能会导致过度消耗，并且，对于简单的查询，网络延迟可能是主要的性能瓶颈。对于这个场景，**cloverDB** 可能是一个更合适的替代方案。

以下是 CloverDB 的主要特点：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230401222140958.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ostafen/clover&type=Timeline)

### 如何安装使用

确保你拥有Go运行环境 (需要Go 1.13 或者更高版本)，执行如下命令进行安装：

```bash
GO111MODULE=on go get github.com/ostafen/clover
```


### 使用示例 DEMO

我们从几个典型的使用场景来介绍 CloverDB 的使用。

1、打开关闭数据库

使用方式类似于 SQLite，基于文件的的形式打开数据库，CloverDB 将数据记录存储为JSON “文档”，这些“文档“被分组在集合中。数据库由一个或多个集合组成。 

```go
import (
	"log"
	c "github.com/ostafen/clover"
)

...

db, _ := c.Open("clover-db")

// 或者，如果你不需要持久性，则像下面这样设置开启内存数据库模式
db, _ := c.Open("", c.InMemoryMode(true))

defer db.Close() // 记住当你完成时关闭数据库
```

2、插入数据

```go

db, _ := c.Open("clover-db")
db.CreateCollection("myCollection") // 创建一个名为"mycollection"的新集合

// 在集合中插入一个新文档
doc := c.NewDocument()
doc.Set("hello", "clover!")

// Insertone返回插入文档的ID，此处执行将doc插入到"myCollection"这个collection中
docId, _ := db.InsertOne("myCollection", doc)
fmt.Println(docId)
```

3、查询数据

```go
db.Query("todos").Where(c.Field("completed").Eq(true)).FindAll()

// 等效于
db.Query("todos").Where(c.Field("completed").IsTrue()).FindAll()
```

还有更多的 CloverDB 数据库的使用方式请查看官方使用文档。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/ostafen/clover 

开源项目作者：ostafen

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ostafen/clover)



关注我们，一起探索有意思的开源项目。
