---
layout: post
title: GitHub 开源项目 zeromicro/go-zero 介绍，A cloud-native Go microservices framework with cli tool for productivity.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 zeromicro/go-zero，该项目在 GitHub 有超过 28.7k Star。

![](https://stats.deeptrain.net/repo/zeromicro/go-zero/?theme=light)

一句话介绍该项目：A cloud-native Go microservices framework with cli tool for productivity.




![Resilience](https://raw.githubusercontent.com/zeromicro/zero-doc/main/doc/images/resilience-en.png)

![benchmark](https://raw.githubusercontent.com/zeromicro/zero-doc/main/doc/images/benchmark.png)

![](https://raw.githubusercontent.com/zeromicro/zero-doc/main/doc/images/go-zero.png)

![](https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=334030&theme=light)

![](https://raw.githubusercontent.com/zeromicro/zero-doc/main/doc/images/architecture-en.png)

![](https://user-images.githubusercontent.com/1918356/171880372-5010d846-e8b1-4942-8fe2-e2bbb584f762.png)

![](https://raw.githubusercontent.com/zeromicro/zero-doc/main/doc/images/cncf-logo.svg)

![](https://raw.githubusercontent.com/zeromicro/zero-doc/main/doc/images/cncf-landscape-logo.svg)

![](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)


###### 项目介绍

### 背景介绍

在现代软件开发过程中，随着云计算和微服务架构的兴起，开发者面临着设计和实现可靠、可伸缩且易于管理的服务的挑战。微服务架构使得开发者可以将复杂应用拆分成小型、独立且易于维护的组件，但这也带来了服务稳定性、高并发处理、服务发现、负载均衡等诸多技术挑战。此外，要实现快速开发并确保代码质量，开发者还需投入大量时间编写胶水代码，处理诸如请求验证、超时控制和错误处理等问题。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-bdd1e141bd70f22a5314b1bbf7893245.png)

项目介绍

**go-zero** 是一个云原生的 Go 微服务框架，内置了大量的工程实践，旨在确保忙碌服务的稳定性。**go-zero** 的设计考虑了高并发场景下的稳定性和高可用性，同时提供了简单的 API 描述语法和代码生成工具 `goctl`，使得开发者可以轻松生成 Go、iOS、Android 等多种语言的代码，大幅提升开发效率。**go-zero** 框架集成了服务发现、负载均衡、链式超时控制、并发控制、自适应熔断和负载削减等众多微服务管理和并发工具包，帮助开发者轻松应对高并发问题，无需繁琐配置即可提升服务的稳定性和性能。

### 如何使用

首先，使用以下命令安装 **go-zero**：

```shell
go get -u github.com/zeromicro/go-zero
```

安装 `goctl` 工具：

```shell
go install github.com/zeromicro/go-zero/tools/goctl@latest
```

创建 API 文件（例如，greet.api）：

```go
type (
  Request {
    Name string `path:"name,options=[you,me]"`
  }

  Response {
    Message string `json:"message"`
  }
)

service greet-api {
  @handler GreetHandler
  get /greet/from/:name(Request) returns (Response)
}
```

然后，通过以下命令生成 Go 服务端代码：

```shell
goctl api go -api greet.api -dir greet
```

该命令将生成的服务代码，并支持立即运行。

### 项目推介

**go-zero** 已经在服务数以千万计的用户多年，它的稳定性和高性能已经得到了广泛验证和认可。不仅如此，作为一个开源项目，**go-zero** 拥有活跃的开发社区，定期更新和改进，确保了框架的先进性和可靠性。该项目由资深工程师开发，不仅在中国国内，甚至已经被多个海外项目采用。此外，**go-zero** 还被列入 CNCF（云原生计算基金会）技术景观，体现了其技术影响力和行业认可度。无论是开发新服务还是转型现有服务，**go-zero** 都是构建高质量、云原生、微服务应用的绝佳选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=zeromicro/go-zero&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/zeromicro/go-zero 

开源项目作者：zeromicro

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=zeromicro/go-zero)

关注我们，一起探索有意思的开源项目。

