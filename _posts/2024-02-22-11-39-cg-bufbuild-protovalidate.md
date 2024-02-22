---
layout: post
title: GitHub 开源项目 bufbuild/protovalidate 介绍，Protocol Buffer Validation - Go, Java, Python, and C++ Beta Releases!
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 bufbuild/protovalidate，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Protocol Buffer Validation - Go, Java, Python, and C++ Beta Releases!”。



![The Buf logo](https://raw.githubusercontent.com/bufbuild/protovalidate/master/./.github/buf-logo.svg)



背景介绍：现代软件开发环境中，保证数据的完整性和一致性是一个重要的问题，尤其是跨网络甚至不同语言环境下的通信。谷歌的 Protocol Buffer 提供了一种跨平台、跨语言的通信协议，然而在默认情况下，它不会对数据进行任何形式的验证，这就要求开发人员在客户端和服务器端都进行相应的数据验证工作，这无疑增加了开发的复杂度。

项目介绍：`protovalidate` 是一款基于谷歌 Common Expression Language (CEL) 的 Protobuf 消息验证库。该项目旨在帮助开发者保护网络数据的一致性和完整性，而无需生成额外的代码。与其前身 `protoc-gen-validate` 相比，` protovalidate `在设计上有着更多的优点。它和 `protoc-gen-validate` 的区别和优越性可以在我们的博客中找到具体的说明。由 `protovalidate` 所构建的项目包括 API 定义、文档、迁移工具、示例文件以及一致性测试工具等。现在，有 Go、C++、Java 及 Python 的实现已经成为了 beta 版本。

如何使用：在你的 Protobuf 消息中定义约束首先需要将 `buf/validate/validate.proto` 导入你的 `.proto` 文件。然后在 `buf` 或 `protoc` 中添加对 `protovalidate` 的依赖。具体的代码示例如下：

```protobuf
syntax = "proto3";
package my.package;
import "buf/validate/validate.proto"; // 导入protovalidate
```

关于如何实施验证约束，这里有几个例子。例子中的所有规则直接在 `proto` 文件中定义：

例子1：对一个 User 消息，我们可以执行约束，要求用户的名字的最短长度。

```protobuf
syntax = "proto3";
import "buf/validate/validate.proto";
message User {
  // User's name, must be at least 1 character long.
  string name = 1 [(buf.validate.field).string.min_len = 1];
}
```

对于更高级或自定义的约束，`protovalidate` 支持使用 CEL 表达式，以在字段间获取信息。

例子2：对于 Product 价格，我们可以要求显示价格的字符串中要包含货币符号，如 "$" 或 "£"，并确保价格为正。

```protobuf
syntax = "proto3";
import "buf/validate/validate.proto";
message Product {
  string price = 1 [(buf.validate.field).cel = {
    id: "product.price",
    message: "Price must be positive and include a valid currency symbol ($ or £)",
    expression: "(this.startsWith('$') || this.startsWith('£')) && double(this.substring(1)) > 0"
  }];
}
```

项目推介：如果你正在使用 Protocol Buffer 并且想要确保数据的完整性和一致性，那么 `protovalidate` 无疑是一个不二之选。它是 [`bufbuild`](https://github.com/bufbuild) 组织中的一个项目，该组织一直为 Protocol Buffer 的使用提供了很多有用的工具。此外，`protovalidate` 支持多种语言，并且有持续更新的趋势，你不仅可以现在就使用，还可以期待它未来的发展。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=bufbuild/protovalidate&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/bufbuild/protovalidate 

开源项目作者：bufbuild

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=bufbuild/protovalidate)

关注我们，一起探索有意思的开源项目。

