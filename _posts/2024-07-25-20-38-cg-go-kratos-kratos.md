---
layout: post
title: 云原生时代的微服务治理框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在云原生时代下，微服务架构成为了软件开发领域的主流模式，它通过将复杂的单体应用分解为可独立开发、部署和维护的更小服务单元，以实现更灵活、可扩展和可维护的软件系统。尽管微服务架构带来了许多益处，但同时也引入了诸多挑战，如服务间的通信、数据的一致性、服务的发现与注册、负载均衡以及容错等问题。这些挑战需要借助专门的框架和工具才能有效解决。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-9d6b0ed00ea59caf683b318eefbe7683.png)

今天要给大家推荐一个 GitHub 开源项目 kratos，该项目在 GitHub 有超过 22.9k Star。

![](https://stats.deeptrain.net/repo/go-kratos/kratos/?theme=light)

一句话介绍该项目：Your ultimate Go microservices framework for the cloud-native era.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801215631610.png)


###### 项目介绍

Kratos 是一个基于 Go 语言实现的面向微服务的治理框架，它旨在帮助开发者快速构建出无懈可击的应用服务。受到希腊神话故事中克拉托斯（成为战神的凡人）的启发，Kratos 为云原生时代的 Go 微服务框架提供了一系列强大的功能和灵活的工具。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801215723994.png)

它具有以下核心特点：

1、通过 Protobuf 定义的 HTTP/gRPC 通信协议，使用统一的元数据传输方法

2、强大的中间件设计，支持追踪（OpenTelemetry）、指标（默认为 Prometheus）、恢复等功能

3、可以通过插件与各种中心化注册中心相连接的注册接口

4、标准日志接口，方便第三方日志库集成，通过 *Fluentd* 收集日志

5、自动支持基于 Accept 和 Content-Type 选择的内容编码

6、支持多数据源的配置和动态配置（使用原子操作）

7、自动生成 Swagger API 文档，并通过添加 Swagger 插件启动 Swagger UI 端点

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801215933504.png)

###### 如何使用

通过以下方式创建一个 Kratos 运行环境：

1、使用 docker 创建环境：

```shell
docker run -it --rm -p 8000:8000 --workdir /workspace golang
```

2、安装必需的工具并创建一个新的 Kratos 应用：

```shell
apt-get update && apt-get -y install protobuf-compiler
export GOPROXY=https://goproxy.io,direct
go install github.com/go-kratos/kratos/cmd/kratos/v2@latest && kratos upgrade
```

3、创建一个新的 HelloWorld 应用并运行它：

```shell
kratos new helloworld
cd helloworld/ && go mod tidy
kratos run
```
访问 `http://localhost:8000/helloworld/kratos`，即可看到运行中的 Kratos 应用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801220049428.png)

###### 项目推介

Kratos 自从发布以来，已经在许多知名公司和项目中被采用，得到了广泛的认可与好评。它不仅是 Go 语言微服务领域的开拓者之一，更因其强大的功能、高效的性能和简洁的设计而深受开发者的喜爱。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240801220208403.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-kratos/kratos&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-kratos/kratos 

开源项目作者：go-kratos

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-kratos/kratos)

关注我们，一起探索有意思的开源项目。

