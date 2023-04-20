---
layout: post
title: 并发编程也可以如此简单
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 sourcegraph/conc，该项目在 GitHub 有超过 2.7k Star，用一句话介绍该项目：“Better structured concurrency for go.”。

sourcegraph/conc 是一个用于在 Go 语言中实现并发编程的库。它提供了一组简单的工具，可以帮助开发人员在 Go 中编写高效、可扩展、易于理解的并发代码。

其中包括一组内置的通道模式，可以帮助开发人员在 Go 中编写经典的并发模式，例如生产者-消费者模式、工作池模式等。该库还提供了一组有用的函数，可以帮助开发人员实现常见的并发操作，例如通道同步、信号量、锁等。

总之，sourcegraph/conc 是一个优秀的选择，可以帮助 Go 开发人员在并发环境中更快、更安全地完成工作。

conc 的设计目的是让 Go 编程更优雅，更不容易出现 Goroutine 泄露、更容易处理 Panic、使得并发编程的代码更易度。

![image-20230109135210077](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/image-20230109135210077.png)



### 如何安装使用

要安装 sourcegraph/conc 项目，你需要先安装 Go 环境。如果你还没有安装 Go，请参考 Go 官网上的安装指南（https://golang.org/doc/install）。

一旦你安装了 Go 环境，你就可以使用 `go get` 命令安装 sourcegraph/conc 库：

```bash
go get github.com/sourcegraph/conc
```

这样，sourcegraph/conc 库就会被安装到你的 Go 环境的默认工作空间中。

你还可以通过在 Go 代码中使用 `import` 语句来使用 sourcegraph/conc 库：

```go
import "github.com/sourcegraph/conc"
```

然后你就可以在你的 Go 代码中使用 sourcegraph/conc 库中提供的功能了。



### 使用示例 DEMO

下面是一个使用 sourcegraph/conc 库实现生产者-消费者模式的示例代码：

```go
package main

import (
	"fmt"
	"github.com/sourcegraph/conc"
)

// 生产者函数，它将数字 1 到 5 放入到通道中
func producer(ch chan<- int) {
	for i := 1; i <= 5; i++ {
		ch <- i
	}
	close(ch)
}

// 消费者函数，它从通道中读取数字并输出
func consumer(ch <-chan int) {
	for num := range ch {
		fmt.Println(num)
	}
}

func main() {
	// 使用 conc.NewChan 创建一个带缓冲的通道
	ch := conc.NewChan(5)

	// 使用 conc.Go 并行地执行生产者和消费者函数
	conc.Go(func() { producer(ch) })
	conc.Go(func() { consumer(ch) })

	// 等待所有并发任务完成
	conc.Wait()
}
```

在这个示例中，我们使用 `conc.NewChan` 函数创建了一个带缓冲的通道，然后使用 `conc.Go` 函数并行地执行了生产者和消费者函数。最后，我们使用 `conc.Wait` 函数等待所有并发任务完成。

运行这个程序，你将会看到输出了数字 1 到 5，表示生产者成功地将这些数字放入了通道，而消费者成功地从通道中读取了这些数字。



更多项目详情请查看如下链接。

开源项目地址：https://github.com/sourcegraph/conc

开源项目作者：sourcegraph

关注我们，一起探索有意思的开源项目。
