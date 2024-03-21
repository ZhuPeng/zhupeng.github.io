---
layout: post
title: 运行速度快可靠的后台任务执行系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在计算机编程和服务器管理领域中，我们经常面临需要处理大量后台运行任务的问题。当我们的应用程序需要执行一些耗时较长、可能失败的操作时，如电子邮件通知、数据同步、日志更新等，我们通常会把这些任务放在后台运行，以便它们不会阻塞主线程，影响用户的体验。然而，编写这样的后台任务并非易事，我们需要确保它们能够快速而可靠地运行，而且必须能够处理各种可能的故障。这就需要我们有一个强大、可靠且高效的后台任务运行环境，那应该如何更好的解决？

今天要给大家推荐一个 GitHub 开源项目 riverqueue/river，该项目在 GitHub 有超过 1.6k Star，用一句话介绍该项目就是：Fast and reliable background jobs in Go。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240303233544444.png)

###### 项目介绍

River 是使用 Go 语言编写的一个开源项目，主要解决的就是后台任务管理的问题。它在运行速度和可靠性方面都有出色表现。River 项目具有以下主要功能：

1、可以通过进程管理来控制任务的运行。你只需要将函数或指令发送给 River，它就可以创建一个新的进程来执行这个任务。

2、提供现成的 API，开发者可以直接调用 River 的方法来创建后台任务，非常方便。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240303233702379.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240303233717421.png)

###### 如何使用

首先需要有一个 PostgreSQL 数据库，以及相应的数据库驱动。然后通过以下命令，你可以快速安装 River：

```shell
go get github.com/riverqueue/river
go get github.com/riverqueue/river/riverdriver/riverpgxv5
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240303233851806.png)

创建新的任务提交到 River 调度执行，只需要如下代码：

```go
_, err = riverClient.InsertTx(ctx, tx, SortArgs{
    Strings: []string{
        "whale", "tiger", "bear",
    },
}, nil)

if err != nil {
    panic(err)
}
```


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=riverqueue/river&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/riverqueue/river 

开源项目作者：riverqueue

开源协议：Mozilla Public License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=riverqueue/river)

关注我们，一起探索有意思的开源项目。

