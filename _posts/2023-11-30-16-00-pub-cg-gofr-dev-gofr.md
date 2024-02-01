---
layout: post
title: Gofr - 简化微服务开发的编程框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在微服务开发过程中，我们常常遇到各类问题。例如，REST 默认的标准难以践行、在企业级规模上的挑战、数据库状态管理、错误管理等等。以往，我们需要手动进行配置、对各个部分进行维护和测试。但随着 `Gofr` 的出现，这一切都可以得到解决。 

今天要给大家推荐一个 GitHub 开源项目 gofr-dev/gofr，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“An opinionated Go framework for accelerated microservice development”。


![](https://github.com/gofr-dev/gofr/assets/44036979/916fe7b1-42fb-4af1-9e0b-4a7a064c243c)

###### 项目介绍

`Gofr` 是一个有见地的 Go 微服务开发框架。虽然可以使用 Gofr 编写通用应用程序，但我们主要关注的是简化微服务的开发。我们将专注于在 Kubernetes 中部署，并渴望提供开箱即用的可观察性。这个项目已经被列入 CNCF Landscape (https://landscape.cncf.io/?selected=go-fr)。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231230202758858.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231230202813747.png)

`Gofr` 的主要优势和特点包括：

1、简单的 API 语法；

2、默认 REST 标准；

3、经过企业级规模的实战测试；

4、强大的配置管理；

5、使用迁移的数据库状态管理；

6、内置中间件以及支持自定义中间件；

7、错误管理；

8、内置的数据存储、文件系统、发布/订阅；

9、支持 gRPC；

10、链式超时控制；

11、支持静态文件服务器；

12、WebSocket 支持；

13、内置防洪控制；

14、内置跟踪、度量和日志。

###### 如何使用

如果你已经有一个 go 项目支持 go mod，你可以通过调用 `go get gofr.dev` 来获取 gofr。如果你是一个新的 Go 项目从，你可以在一个空文件夹里初始化你的 go 模块，比如 `go mod init test-service`。然后创建 `main.go` 文件，输入以下内容：

```go
package main

import "gofr.dev/pkg/gofr"

func main() {
    app := gofr.New()

    app.GET("/", func(ctx *gofr.Context) (interface{}, error) {
        return "Hello World!", nil
    })

    app.Start()
}
```
接着获取所有的依赖，例如 `go get ./...`。然后启动服务器 `go run main.go`。会在默认的 8000 端口上启动服务器。

###### 项目推介

`Gofr` 的活跃开发和广泛应用都验证了其在微服务开发中的强大性能和实用性，尤其其已经得到 CNCF 的引用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gofr-dev/gofr&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/gofr-dev/gofr 

开源项目作者：gofr-dev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gofr-dev/gofr)

关注我们，一起探索有意思的开源项目。

