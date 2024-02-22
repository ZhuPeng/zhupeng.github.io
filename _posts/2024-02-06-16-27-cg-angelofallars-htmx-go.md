---
layout: post
title: GitHub 开源项目 angelofallars/htmx-go 介绍，</> Build awesome HTMX + Go projects faster.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 angelofallars/htmx-go，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“</> Build awesome HTMX + Go projects faster.”。



![](https://github.com/angelofallars/htmx-go/assets/39676098/c1a14954-27fd-4276-8948-0800e5372b14)



背景介绍：在开发 Hypermedia 驱动应用程序的过程中，我们经常会遇到一种情况，就是需要不断的翻动 HTTP 头部信息，这对效率的提升极为不利。此外，处理客户端事件时，需要处理 JSON 序列化，对近应于事件驱动设计模式的应用开发造成了难度。不得不提的是，我们还需要为 “hx-swap” 行为进行微调。

项目介绍：这是一个名为 htmx-go 的开源项目，它是一个与 HTMX 在 Go 中协同工作的类型安全库。该项目提供了以下多项功能。1）可以很好地检查请求是否来自 HTMX，并用类型安全、声明性的语法为 HTMX 响应头部编写代码，从服务器端控制 HTMX 行为。2）有效地编写触发客户端事件的代码，而无需处理 JSON 序列化。通过这种方式，事件驱动应用程序更容易开发。3）使用 “Swap Strategy” 方法进行 “hx-swap” 行为的微调。它使用标准的 `net/http` 类型，并且提供了与 `templ` 组件的基本集成。

如何使用：你可以使用 “go get” 命令进行安装，然后导入 "htmx-go"。

```sh
go get github.com/angelofallars/htmx-go
```
```go
import "github.com/angelofallars/htmx-go"
```
你可以用它来处理 HTMX 请求和响应，同时也提供了对于 `hx-boost` 的处理。构建函数 `handler(w http.ResponseWriter, r *http.Request)` 旨在有效地处理请求和生成响应。以下是一个示例：
 ```go
func handler(w http.ResponseWriter, r *http.Request) {
	if htmx.IsHTMX(r) {
		htmx.NewResponse().
			Reswap(htmx.SwapBeforeEnd).
			Retarget("#contacts").
			AddTrigger(htmx.Trigger("enable-submit")).
			AddTrigger(htmx.TriggerDetail("display-message", "Hello world!")).
			Write(w)
	}
}
```

项目推介：htmx-go 是一个令人兴奋的项目，无论实现方式还是理念都颇具新意。它强调类型的安全，方便了开发者的使用。同时，项目的开发活跃度与更新速度都体现了其活力和成长潜力。因此，我强烈推荐所有使用 Go 开发的朋友们去试一试这个项目，你一定会被它所吸引。如果你认为它很棒，也请考虑赞助这个项目的作者！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=angelofallars/htmx-go&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/angelofallars/htmx-go 

开源项目作者：angelofallars

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=angelofallars/htmx-go)

关注我们，一起探索有意思的开源项目。

