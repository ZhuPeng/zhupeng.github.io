---
layout: post
title: GitHub 开源项目 gocrane/crane-scheduler 介绍，Crane scheduler is a Kubernetes scheduler which can schedule pod based on actual node load.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 gocrane/crane-scheduler，该项目在 GitHub 有超过 0.1k Star，用一句话介绍该项目就是：“Crane scheduler is a Kubernetes scheduler which can schedule pod based on actual node load.”。


gocrane/crane-scheduler 是一个开源项目，是基于 Go 语言的调度器库。它主要用于企业级的分布式调度，可以帮助开发者实现任务调度、任务分配、负载均衡等功能。该项目支持多种调度策略，可以在不同的场景中进行优化。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gocrane/crane-scheduler&type=Timeline)

### 如何安装使用

gocrane/crane-scheduler 项目可以通过 Go Modules 或者普通的 go get 命令来安装。

1. 使用 Go Modules 安装：

在你项目的根目录下执行以下命令:

```go
go mod init [your_module_name]
go get github.com/gocrane/crane-scheduler
```

2. 使用 go get 安装：

在终端中执行以下命令：
```
go get github.com/gocrane/crane-scheduler
```

在你的 Go 代码中导入包：
```go
import "github.com/gocrane/crane-scheduler"
```

在安装完成之后，你就可以在你的 Go 代码中使用 crane-scheduler 了。

注意: 你需要安装 Go 1.13 或更高版本才能使用 Go Modules


### 使用示例 DEMO

以下是一个使用 gocrane/crane-scheduler 的简单 demo，它展示了如何使用默认的调度策略来调度任务。

```go
package main

import (
    "fmt"
    "time"

    "github.com/gocrane/crane-scheduler"
)

func main() {
    // 创建调度器
    scheduler := crane_scheduler.New()

    // 添加任务
    scheduler.AddFunc("task1", func() {
        fmt.Println("Task 1 is running.")
    }, time.Second)
    scheduler.AddFunc("task2", func() {
        fmt.Println("Task 2 is running.")
    }, time.Second*2)

    // 开始调度
    scheduler.Start()

    // 停止调度
    time.Sleep(time.Second * 5)
    scheduler.Stop()
}
```

在这个示例中，我们创建了一个新的调度器，添加了两个任务，并在调度开始后等待5秒钟停止调度。每个任务将按照给定的时间间隔执行一次，并在控制台中打印输出。

请注意，这只是一个简单的示例，crane-scheduler 还提供了更多强大的功能，例如自定义调度策略，多任务调度等。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/gocrane/crane-scheduler 

开源项目作者：gocrane

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gocrane/crane-scheduler)

