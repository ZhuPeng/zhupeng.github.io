---
layout: post
title: Go 语言超快安全轻量级的 Actor 引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在编写高并发的分布式系统时，常常会遇到许多挑战，如如何优化系统性能、如何降低系统应用延迟、怎样在遇到错误和故障时保证系统的稳健性等问题。为了克服这些挑战，卡尔·惠特在 1973 年引入了 Actor 模型。Actor 模型是一种计算模型，最基本的构建单位是 Actor，每一个 Actor 独立运行，通过发送接收消息与其他 Actor 交互，这种方式可以使系统具有高度的并发性和分布性。

今天要给大家推荐一个 GitHub 开源项目 hollywood，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目：Blazingly fast and light-weight Actor engine written in Golang.


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240122212439503.png)

###### 项目介绍

 Hollywood 是一个基于 Golang 的超快安全轻量级的 Actor 引擎项目。它是为快速和低延迟的应用程序（如游戏服务器，广告代理商，交易引擎等）而构建的，能在一秒内处理超过 1000 万的消息。Hollywood 的主要特性包括消息在 Actor 失败时的可靠传输 (缓冲机制)、忘却式或请求响应式消息传送，采用高性能的 dRPC 作为运输层、优化的 proto 缓冲区（没有反射）、轻量级和高度可定制、集群支持等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240122212639927.png)

###### 如何使用

如果你想要安装 Hollywood， 只需要执行以下简单指令。

```bash
go get github.com/anthdm/hollywood/...
```

为了更好的理解如何使用 Hollywood ，以下是一个示例：

创建一条 Hello world 消息。你可以先新建一个 actor 简单终端打印消息，然后通过 Hollywood 的引擎 API 发送你的消息给 actor。以下是示例代码：

```go
type helloer struct{}

func newHelloer() actor.Receiver {
	return &helloer{}
}

type message struct {}

func (h *helloer) Receive(ctx *actor.Context) {
	switch msg := ctx.Message().(type) {
	case actor.Initialized:
		fmt.Println("helloer has initialized")
	case actor.Started:
		fmt.Println("helloer has started")
	case actor.Stopped:
		fmt.Println("helloer has stopped")
	case *message:
		fmt.Println("hello world", msg.data)
	}
}

func main() {
  engine, err := actor.NewEngine(actor.NewEngineConfig())
  pid := engine.Spawn(newHelloer, "hello")

  engine.Send(pid, "hello world!")
}
```

###### 项目推介

Hollywood 也是一个非常轻量级的工具，它独特的 Actor 模型设计解决了并发和分布式系统中的常见问题，Hollywood 有良好的代码质量，并且提供了强大、灵活且简单的 API。Hollywood 虽然是一个新项目，但是已经有公司中生产环境中使用。如果你是在构建并发和分布式系统，Hollywood 是一个值得你关注的重要工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240122213209400.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=anthdm/hollywood&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anthdm/hollywood 

开源项目作者：anthdm

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=anthdm/hollywood)

关注我们，一起探索有意思的开源项目。

