---
layout: post
title: FlyDB - 一款平衡性能和存储成本键值（KV）存储引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的数据驱动时代，我们经常会遇到需要快速、高效地存储和检索键值对数据的需求。然而，许多现有的存储解决方案，如 Redis，虽然在性能上表现出色，但在存储成本上可能较高。这就需要我们寻找一种能够平衡性能和存储成本的解决方案。

今天要给大家推荐一个 GitHub 开源项目 ByteStorage/FlyDB，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“The high-performance kv storage engine based on bitcask paper made in golang”。

![](https://raw.githubusercontent.com/ByteStorage/FlyDB/master/./assets/FlyDB-logo.png)

###### 项目介绍

FlyDB 是一个基于高效的 bitcask 模型的高性能键值（KV）存储引擎，它旨在作为某些情况下内存键值存储（如 Redis）的替代品，以达到平衡性能和存储成本的目标。FlyDB 通过优化资源分配和使用成本效益高的存储媒介，以及智能管理数据，确保了操作效率的同时，最大程度地降低了存储成本。它为需要平衡性能和存储成本的场景提供了可靠的解决方案。

以下是 FlyDB 的性能测试数据，测试方式为随机写入和读取 50 万次数据：

BTree 索引：

![](https://raw.githubusercontent.com/ByteStorage/FlyDB/master/./assets/v1.0.4-btree)

ARTree 索引：

![](https://raw.githubusercontent.com/ByteStorage/FlyDB/master/./assets/v1.0.4--art)

###### 如何使用

你可以使用 Go 命令行工具安装 FlyDB：

```bash
go get github.com/ByteStorage/FlyDB@v1.1.0
```

或者从 github 克隆这个项目：

```bash
git clone https://github.com/ByteStorage/FlyDB.git
```

以下是一个简单的使用示例：

```go
package main

import (
	"fmt"
	"github.com/ByteStorage/FlyDB/flydb"
	"github.com/ByteStorage/FlyDB/config"
)

func main() {
    options := config.DefaultOptions
		options.DirPath = "/tmp/flydb"
		db, _ := flydb.NewFlyDB(options)

    err := db.Put([]byte("name"), []byte("flydb-example"))
    if err != nil {
        fmt.Println("Put Error => ", err)
    }
		
  	val, err := db.Get([]byte("name"))
		if err != nil {
		  	fmt.Println("Get Error => ", err)
		}
    fmt.Println("name value => ", string(val)
                    	
    err := db.Delete([]byte("name"))
    if err != nil {
        fmt.Println("Delete Error => ", err)
    }
}
```

###### 项目推介

FlyDB 的性能测试结果显示，其读写大规模数据的性能表现优秀。在对 50 万条随机数据的测试中，其 PUT 和 GET 的性能均表现出色。此外，与市场上其他用 golang 编写的 kv 数据库进行的基准测试结果比较，FlyDB V1.0.4 的读写性能测试结果超过了大多数开源 kv 数据库。因此，无论你是开发者还是企业，如果你在寻找一种能够平衡性能和存储成本的高效存储解决方案，FlyDB 都是一个值得考虑的选择。

以下是横向与其他数据库的测试对比：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231013220647596.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ByteStorage/FlyDB&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ByteStorage/FlyDB 

开源项目作者：ByteStorage

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ByteStorage/FlyDB)

关注我们，一起探索有意思的开源项目。