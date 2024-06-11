---
layout: post
title: GitHub 开源项目 grpc-ecosystem/grpc-gateway 介绍，gRPC to JSON proxy generator following the gRPC HTTP spec
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 grpc-ecosystem/grpc-gateway，该项目在 GitHub 有超过 17.6k Star。

![](https://stats.deeptrain.net/repo/grpc-ecosystem/grpc-gateway/?theme=light)

一句话介绍该项目：gRPC to JSON proxy generator following the gRPC HTTP spec




![](https://raw.githubusercontent.com/grpc-ecosystem/grpc-gateway/master/docs/assets/images/architecture_introduction_diagram.svg)

![](https://img.youtube.com/vi/Pq1paKC-fXk/0.jpg)


###### 项目介绍

**背景介绍：**

在现代的软件开发实践中，我们经常面临着如何同时提供 gRPC 和 RESTful HTTP API 服务的挑战。gRPC，由于其高效的通信协议和跨语言的支持，已成为微服务架构中服务间通信的首选。然而，由于各种原因（如客户端兼容性、团队熟练度或者是现有基础设施的限制），RESTful API 仍然是不可或缺的。维护两套接口不仅增加了开发和维护的工作量，而且还会导致接口不一致，从而影响到最终用户的体验。此外，对于一些特定的场景，如支持互联网公开接口或是向后兼容，提供一个传统的 HTTP+JSON API 是不可避免的。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1a052d403b47fe574309ce5b9e952557.png)

项目介绍：**

针对以上的问题，[ gRPC-Gateway ](https://github.com/grpc-ecosystem/grpc-gateway) 项目提供了一个优雅的解决方案。该项目是一个 protoc 的插件，它能够读取 protobuf 服务定义，并生成一个反向代理服务器，这个服务器可以将 RESTful HTTP API 交互转换成 gRPC 调用。这意味着你只需维护一套 gRPC API，gRPC-Gateway 就可以为你自动生成对应的 RESTful 风格的 API。特别是，通过在服务定义中添加 [`google.api.http`](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto#L46) 注解，你可以详细控制 HTTP 映射的行为，让 API 更符合 REST 风格的设计标准。

**如何使用：**

首先，你需要通过以下 Go Modules 命令安装 gRPC-Gateway ：

```sh
go get -u github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway
go get -u github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2
```

接着，在你的 `proto` 文件中定义 gRPC 服务，并使用 `google.api.http` 注解指定 HTTP 映射。例如：

```protobuf
syntax = "proto3";
package your.service.v1;
import "google/api/annotations.proto";

service YourService {
  rpc Echo(StringMessage) returns (StringMessage) {
    option (google.api.http) = {
      post: "/v1/example/echo"
      body: "*"
    };
  }
}
```

然后，使用 protoc 和 gRPC-Gateway 插件生成 gRPC 和 HTTP 代理代码：

```sh
protoc -I . \
    -I $GOPATH/src \
    -I $GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
    --go_out ./gen/go/ --go_opt paths=source_relative \
    --go-grpc_out ./gen/go/ --go-grpc_opt paths=source_relative \
    --grpc-gateway_out ./gen/go/ --grpc-gateway_opt paths=source_relative \
    your/service/v1/your_service.proto
```

最后，实现你的 gRPC 服务，启动 gRPC-Gateway 作为你的 HTTP 服务器。

**项目推介：**

自从 2018 年以来，gRPC-Gateway 已经成功地为数百万 API 请求服务，正如 [Ad Hoc](http://adhocteam.us/) 的 William Mill 引用所言："我们使用 gRPC-Gateway 来服务每天数百万的 API 请求，自那以来，我们从未遇到任何问题。" 这个项目不仅活跃，由一个强大的社区维护，而且它的设计和实现都经过了时间的检验。不仅如此，它还通过降低维护两套 API 接口的复杂性和成本，帮助了无数的开发团队和公司，使其能够集中精力提升产品的质量和用户体验。无论你是一个小团队还是在大公司里工作，如果你正在寻找一种同时提供 gRPC 和 HTTP/JSON API 的高效方式，gRPC-Gateway 绝对值得考虑。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=grpc-ecosystem/grpc-gateway&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/grpc-ecosystem/grpc-gateway 

开源项目作者：grpc-ecosystem

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=grpc-ecosystem/grpc-gateway)

关注我们，一起探索有意思的开源项目。

