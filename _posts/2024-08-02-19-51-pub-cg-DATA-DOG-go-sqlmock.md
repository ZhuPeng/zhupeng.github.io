---
layout: post
title: 针对 Go 开发的 SQL 驱动模拟库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

数据库交互是几乎所有应用程序不可或缺的一部分，开发者们常常需要对数据库进行各种操作，包括插入、更新、删除和查询等。然而，在开发过程中直接对真实数据库进行操作不仅耗时耗力，还可能带来数据一致性和安全性的风险。特别是在进行单元测试时，我们希望能在一个隔离的环境中模拟真实的数据库操作，以确保应用的稳定性和可靠性。传统方法可能涉及复杂的配置和额外的依赖，增加了项目复杂性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-b80fc6c0f20ed88683c75bbd7b623ab3.png)

今天要给大家推荐一个 GitHub 开源项目 go-sqlmock，该项目在 GitHub 有超过 6.0k Star。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240908222324103.png)

一句话介绍该项目：Sql mock driver for golang to test database interactions

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240818200350040.png)


###### 项目介绍

**sqlmock** 是一个针对 **Go 语言**开发的 SQL 驱动模拟库，旨在测试中模拟任何 SQL 驱动的行为，而无需真实的数据库连接。这有助于维护正确的测试驱动开发（TDD）工作流。该项目支持并发和多个连接，兼容 **Go1.8** 的上下文相关特性模拟和命名 SQL 参数，无需修改源代码即可使用。此外，**sqlmock** 采用严格的默认期望顺序匹配，没有第三方依赖，保障了高度的稳定性和完整性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240818200139257.png)

###### 如何使用

首先需要通过 `go get` 命令安装：

```sh
go get github.com/DATA-DOG/go-sqlmock
```

以下是一个使用 **sqlmock** 测试数据库交互的示例代码：

```go
package main

import (
    "testing"
    "github.com/DATA-DOG/go-sqlmock"
)

func TestShouldUpdateStats(t *testing.T) {
    db, mock, err := sqlmock.New()
    if err != nil {
        t.Fatalf("an error '%s' was not expected when opening a stub database connection", err)
    }
    defer db.Close()

    mock.ExpectBegin()
    mock.ExpectExec("UPDATE products").WillReturnResult(sqlmock.NewResult(1, 1))
    mock.ExpectExec("INSERT INTO product_viewers").WithArgs(2, 3).WillReturnResult(sqlmock.NewResult(1, 1))
    mock.ExpectCommit()
  
    if err := recordStats(db, 2, 3); err != nil {
        t.Errorf("error was not expected while updating stats: %s", err)
    }
  
    if err := mock.ExpectationsWereMet(); err != nil {
        t.Errorf("there were unfulfilled expectations: %s", err)
    }
}
```

此示例展示了如何初始化一个模拟数据库连接，设置期望的数据库操作，并验正所期望的操作是否全部满足。

###### 项目推介

**sqlmock** 自从发布以来，已成为许多 Go 语言开发者的首选工具，以支持他们的单元测试和集成测试。这个项目已经达到了成熟和稳定的状态，表明它能够提供一致且可靠的测试支持。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=DATA-DOG/go-sqlmock&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/DATA-DOG/go-sqlmock 

开源项目作者：DATA-DOG

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=DATA-DOG/go-sqlmock)

关注我们，一起探索有意思的开源项目。

