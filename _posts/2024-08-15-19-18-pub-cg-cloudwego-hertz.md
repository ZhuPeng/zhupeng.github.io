---
layout: post
title: 字节跳动背书专为 Go 语言设计的 HTTP 框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在微服务架构的开发过程中，开发人员面临的一个核心挑战是如何快速、高效地开发出既可靠又高性能的服务。随着 Go 语言因其出色的性能和简洁的语法成为微服务开发的热门选择，对应的高性能 HTTP 框架需求随之增加。开发人员需要一个既能提供高性能，又能支持强大扩展性并且易于使用的框架来构建微服务，同时还要考虑到协议的多样性和网络层的灵活切换能力等多维度需求。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-d0c9d1ff18b92cb0855e4db1a5c54e00.png)

今天要给大家推荐一个 GitHub 开源项目 hertz，该项目在 GitHub 有超过 5.1k Star。

![](https://stats.deeptrain.net/repo/cloudwego/hertz/?theme=light)

一句话介绍该项目：Go HTTP framework with high-performance and strong-extensibility for building micro-services.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825200550011.png)


###### 项目介绍

**Hertz** 是一个专为 Go 语言设计的 HTTP 框架，它通过强调高可用性、高性能和高扩展性来帮助开发人员构建微服务。与其他开源框架如 **fasthttp**、**gin**、**echo** 等相比较，**Hertz** 结合了字节跳动内部的需求，并已在该公司内部被广泛使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825200646484.png)

**主要特性包括：**

1、高可用性：**Hertz** 在迭代过程中积极听取用户意见，不断打磨框架，提供更好的用户体验。

2、高性能：默认使用自研的高性能网络库 **Netpoll**，在特定场景下相较 Go Net 有明显的 QPS 和时延优势。

3、高扩展性：采用分层设计，提供更多接口和默认扩展实现，支持用户自行扩展。

4、多协议支持：原生支持 HTTP/1.1、HTTP/2、HTTP/3、ALPN 等协议，并且支持自定义协议解析逻辑。

5、网络层切换能力：能够根据需要在 **Netpoll** 和 **Go Net** 之间切换。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825200913645.png)

###### 如何使用

**安装 Hertz** 可通过以下命令进行：

```shell
go get -u github.com/cloudwego/hertz
```

**快速开始示例**：

```go
package main

import (
    "context"
    "github.com/cloudwego/hertz/pkg/app"
    "github.com/cloudwego/hertz/pkg/app/server"
)

func main() {
    h := server.Default(server.WithHostPorts(":8080"))
    h.GET("/hello", func(c context.Context, ctx *app.RequestContext) {
        ctx.String(200, "Hello, Hertz!")
    })
    h.Spin()
}
```
该示例创建了一个监听在 8080 端口的 HTTP 服务器，当访问 "/hello" 路由时，返回 "Hello, Hertz!" 字符串。

###### 项目推介

**Hertz** 由字节跳动背书，并在其内部广泛使用，这本身就是一个强有力的信任标志。随着越来越多的微服务选用 Go 语言，**Hertz** 凭借其高性能、高扩展性和易用性，成为了开发高要求微服务的首选框架。无论是小团队还是大企业，**Hertz** 都能够满足不同规模项目的需求，确保开发效率和服务质量。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240825200956421.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cloudwego/hertz&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cloudwego/hertz 

开源项目作者：cloudwego

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cloudwego/hertz)

关注我们，一起探索有意思的开源项目。

