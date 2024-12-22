---
layout: post
title: 简单可靠高效的分布式任务系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在系统访问量逐渐增大，高并发、分布式系统成为了企业技术架构升级的必由之路。在这样的背景下，异步任务队列扮演着至关重要的角色，它能有效地分摊服务器负载，提高系统的可扩展性与用户体验。然而，设计一个既简单又可靠、高效的分布式任务队列系统是一项挑战。开发者们需要考虑任务的调度、执行、失败重试、任务去重、超时控制等一系列细节问题，而这些通常需要大量的技术积累和开发成本。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0d290a28832b0ecf8f511feae8755368.png)

今天要给大家推荐一个 GitHub 开源项目 asynq，该项目在 GitHub 有超过 10.2k Star。

![](https://stats.deeptrain.net/repo/hibiken/asynq/?theme=light)

一句话介绍该项目：Simple, reliable, and efficient distributed task queue in Go

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215235327981.png)

###### 项目介绍

Asynq 是一个用 Go 编写的简单、可靠、高效的分布式任务队列系统。该项目以 Redis 作为后端，支持高并发处理与横向扩展，解决了传统任务队列系统复杂部署和难以管理的问题。

![](https://user-images.githubusercontent.com/11155743/116358505-656f5f80-a806-11eb-9c16-94e49dab0f99.jpg)

Asynq 能够保证至少一次的任务执行，支持任务调度、失败重试、自动恢复、权重和严格优先级队列、任务超时和取消、任务聚合等丰富的功能。此外，Asynq 提供了任务去重功能，避免相同任务的多次执行，极大地提高了任务处理的效率和可靠性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241215235533973.png)

###### 如何使用

通过以下命令安装 Asynq：

```sh
go get -u github.com/hibiken/asynq
```

下面是使用 Asynq 创建和处理异步任务的简单示例：

```go
package main

import (
    "context"
    "log"
    "github.com/hibiken/asynq"
    "your_project/tasks" // assume you are already create tasks package
)

func main() {
    r := &asynq.RedisClientOpt{Addr: "localhost:6379"}
    client := asynq.NewClient(r)
    defer client.Close()

    task, err := tasks.NewEmailDeliveryTask(123, "template_id")
    if err != nil {
        log.Fatalf("failed to create task: %v", err)
    }

    if _, err := client.Enqueue(task); err != nil {
        log.Fatalf("failed to enqueue task: %v", err)
    }

    log.Println("Task enqueued successfully")
}
```

对应系统还带有一个默认的任务的监控页面：

![](https://user-images.githubusercontent.com/11155743/114697016-07327f00-9d26-11eb-808c-0ac841dc888e.png)

###### 项目推介

Asynq 为使用 Go 语言开发高性能异步任务处理系统提供了强有力的支持，具有丰富的特性并支持各种高级用例，如任务调度、重试机制、任务去重等，满足了不同场景下的需求。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=hibiken/asynq&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/hibiken/asynq 

开源项目作者：hibiken

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=hibiken/asynq)

关注我们，一起探索有意思的开源项目。

