---
layout: post
title: goev - 一款基于 Go 语言的高性能、轻量级、非阻塞、I/O 事件驱动的网络框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在进行 Go 语言的 TCP 网络编程时，我们通常使用标准库（go net），但是标准库的协程压力较大，因此我们需要一种更轻量级、高性能的非阻塞 I/O 事件驱动网络框架。goev 就是为此而生的。

用一句话介绍 goev 项目就是：“goev is a lightweight, concise i/o event demultiplexer implementation in Go”。

###### 项目介绍

goev 是一款基于 Go 语言的高性能、轻量级、非阻塞、I/O 事件驱动的网络框架。它从 ACE 的设计模式中汲取灵感，为 TCP网络编程项目提供了优雅而简洁的解决方案。使用 goev，您可以无缝集成您的项目，而不必担心标准库（go net）引入的协程压力。与 go net 库相比，goev 可以在同步 I/O 方面至少提高20%的性能。此外，与框架内的无锁处理相结合，它提供了更好的优化机会，从而实现更高的整体性能增益。

以下是 goev 的工作原理：

![](https://raw.githubusercontent.com/shaovie/goev/master/images/goev.png)

goev的主要特点包括：

* I/O事件驱动架构
* 轻量级和简约的反应器模式实现，允许多个反应器的灵活组合
* 面向对象的实现，更易于封装业务逻辑
* 支持异步发送，允许高级应用程序执行同步I/O操作，同时异步处理业务处理
* 轮询堆栈中的无锁操作，实现同步I/O的零拷贝数据传输
* 完美支持REUSEPORT多轮询器模式
* 内置四堆计时器实现，实现I/O和计时器事件的无锁/同步处理
* 完全本地实现的接受器/连接器，提供最大的可定制性
* 可控的底层线程数。每个连接每个协程的方法通常会导致线程数激增，但使用轮询器可以保持一致的线程数，将其保持在初始水平
* 垃圾回收（GC）友好，最小化运行时的额外堆内存使用
* 支持应用层与轮询器之间的交互，例如在轮询器协程中创建缓存，实现无锁使用（类似于runtime.mcache）
* API较少，学习成本低

以下是对 goev 的性能测试数据，在阿里云 32 核 64G 的机器上，测试得到 160 万/秒的处理速率。

![](https://raw.githubusercontent.com/shaovie/goev/master/images/bench-32v-64g.png)

###### 如何使用

您可以通过以下步骤安装goev：

```bash
go get github.com/shaovie/goev
```
如果您需要使用goev，可以参考如下示例代码，更多详细的代码可以在 GitHub 中查看。

简单的服务示例：

```Go
package main

import (
    "github.com/shaovie/goev"
)

var connReactor *goev.Reactor

type Conn struct {
	goev.IOHandle
}

func (c *Conn) OnOpen() bool {
	if err := connReactor.AddEvHandler(c, c.Fd(), goev.EvIn); err != nil {
		return false
	}
	return true
}
func (c *Conn) OnRead() bool {
	buf, n, _ := c.Read()
	if n == 0 { // Abnormal connection
		return false
	}
    // parse msg
    return true
}
func (c *Conn) OnClose() {
    c.Destroc(h) // release resource
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU()*2 - 1)
	listenReactor, err := goev.NewReactor(goev.EvPollNum(1))
	if err != nil {
		panic(err.Error())
	}
	connReactor, err := goev.NewReactor(goev.EvPollNum(runtime.NumCPU()*3/2))
	if err != nil {
		panic(err.Error())
	}
	_, err = goev.NewAcceptor(listenReactor, ":8080", func() goev.EvHandler { return new(Conn) })
	if err != nil {
		panic(err.Error())
	}

	go func() {
		if err = listenReactor.Run(); err != nil {
			panic(err.Error())
		}
	}()
    
	if err = connReactor.Run(); err != nil {
		panic(err.Error())
	}
}
```

###### 项目推介

根据测试，goev 在同步 I/O 方面的性能比 go net 库提高了至少 20%，这使得它成为一款非常值得推荐的网络框架。如果您正在寻找一款高性能、轻量级、非阻塞、I/O事件驱动的网络框架，那么 goev 绝对是您的不二选择。快来尝试一下吧！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=shaovie/goev&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/shaovie/goev 

开源项目作者：shaovie

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=shaovie/goev)

关注我们，一起探索有意思的开源项目。

