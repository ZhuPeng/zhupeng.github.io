大家好，又见面了，我是 GitHub 精选君！

整洁架构后端应用实践

今天要给大家推荐一个 GitHub 开源项目 amitshekhariitbhu/go-backend-clean-architecture，该项目在 GitHub 有超过 1.2k Star，用一句话介绍该项目就是：“A Go (Golang) Backend Clean Architecture project with Gin, MongoDB, JWT Authentication Middleware, Test, and Docker.”。

![Go Backend Clean Architecture](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_go-backend-clean-architecture.png)

go-backend-clean-architecture 是一个使用 Go 语言编写的后端整洁架构项目。它提供了一种简单而有效的方法来构建可扩展和可维护的后端应用程序。该项目遵循 Uncle Bob 的整洁架构原则，并提供了结构化的目录结构，便于开发人员进行维护和扩展。

以下是项目的架构图。

![Go Backend Clean Architecture Diagram](/Users/zhupeng/Work/git/zhupeng.github.io/images/go-backend-arch-diagram.png)

Server 接收到 API 请求后会按如下处理：

![Public API Request Flow](/Users/zhupeng/Work/git/zhupeng.github.io/images/go-arch-public-api-request-flow.png)

同时可以根据需要在 Router 和 Controller 之前增加 Middleware 和 认证。

![Private API Request Flow](/Users/zhupeng/Work/git/zhupeng.github.io/images/go-arch-private-api-request-flow.png)

使用整洁架构的原则开发应用程序，后续可以规避很多维护上的问题，同时代码的可读性也有很大的提升，对于在使用 Go 开发的同学来说，非常推荐大家了解一下。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/amitshekhariitbhu/go-backend-clean-architecture

开源项目作者：go-backend-clean-architecture

