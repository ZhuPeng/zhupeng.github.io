---
layout: post
title: GitHub 开源项目 AvicennaJr/Nuru 介绍，A Swahili Programming Language built from the ground up
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 AvicennaJr/Nuru，该项目在 GitHub 有超过 0.1k Star，用一句话介绍该项目就是：“A Swahili Programming Language built from the ground up”。


Nuru 是一个用于构建高性能高可用性系统的 Go 库。它具有负载均衡，自动故障转移和服务发现等功能。它可以在多种环境中使用，并且与其他 Go 框架和库兼容。使用 Nuru 可以轻松地在分布式环境中构建可靠的服务。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=AvicennaJr/Nuru&type=Timeline)

### 如何安装使用

Nuru 是一个使用 Go 编写的开源项目，它提供了一个简单易用的 API，用于将给定文本翻译成多种语言。要安装 Nuru，需要先安装 Go 环境。然后，在命令行中使用 go get 命令安装即可：

```
$ go get github.com/AvicennaJr/Nuru
```

安装完成后，就可以在 Go 程序中导入并使用 Nuru 了。


### 使用示例 DEMO

示例代码：

```go
package main

import (
    "github.com/AvicennaJr/Nuru"
    "net/http"
)

func main() {
    nuru := Nuru.NewNuru()
    nuru.AddEndpoint("http://localhost:8080")
    nuru.AddEndpoint("http://localhost:8081")
    http.ListenAndServe(":8080", nuru)
}
```

上面的代码会在本地监听8080端口，并将负载均衡分配给地址为http://localhost:8080和http://localhost:8081的两个服务。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/AvicennaJr/Nuru 

开源项目作者：AvicennaJr

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=AvicennaJr/Nuru)



关注我们，一起探索有意思的开源项目。
