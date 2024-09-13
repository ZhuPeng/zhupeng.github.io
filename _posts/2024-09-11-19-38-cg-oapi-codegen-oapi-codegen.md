---
layout: post
title: GitHub 开源项目 oapi-codegen/oapi-codegen 介绍，Generate Go client and server boilerplate from OpenAPI 3 specifications
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 oapi-codegen/oapi-codegen，该项目在 GitHub 有超过 6.0k Star。

![](https://stats.deeptrain.net/repo/oapi-codegen/oapi-codegen/?theme=light)

一句话介绍该项目：Generate Go client and server boilerplate from OpenAPI 3 specifications




![](https://raw.githubusercontent.com/oapi-codegen/oapi-codegen/master/.github/sponsors/devzero-dark.svg)

![](https://raw.githubusercontent.com/oapi-codegen/oapi-codegen/master/.github/sponsors/speakeasy-dark.svg)

![](https://raw.githubusercontent.com/oapi-codegen/oapi-codegen/master/.github/sponsors/elastic-dark.svg)


###### 项目介绍

背景介绍：
在数字化转型的浪潮中，越来越多的服务和应用倚重于标准化的 API 来实现跨系统、跨平台的数据交换和集成。OpenAPI（原 Swagger）规范因其能够标准化描述 RESTful API 而广受欢迎，但随之而来的问题是，遵循 OpenAPI 规范定义并实现客户端与服务端代码往往需要消耗大量的时间与精力，尤其是在类型安全的语言如 Go 中，这种重复且繁琐的工作不仅容易引发错误，也极大地拖慢了开发进度。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1991d48440f4289c8be0ab20c8de04c5.png)

项目介绍：
`oapi-codegen` 项目正是针对上述问题提出的解决方案。它是一个命令行工具及库，旨在将 OpenAPI 3 规范自动转化为 Go 代码，包括服务端实现、API 客户端以及 HTTP 模型等。这意味着开发者可以省去大量编写样板代码的工作，专注于编写业务逻辑，提升开发效率。`oapi-codegen` 遵循 Go 的惯用命名和设计，尽可能生成简单直观的代码，并且支持 OpenAPI 3.x 的广泛特性。通过与 Go 的类型系统相结合，`oapi-codegen` 弥补了类型安全语言在自动代码生成方面的不足。总之，`oapi-codegen` 不仅减轻了开发者的负担，也使得基于 OpenAPI 的项目实施更加风险可控。

如何使用：
首先，使用如下命令安装 `oapi-codegen`：

```sh
$ go install github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@latest
```

然后，假设你已经有了 OpenAPI 规范定义的 `api.yaml` 文件，可以通过如下命令生成所需的代码：

```sh
$ oapi-codegen --config=config.yaml ../../api.yaml
```

以上命令通过指定配置文件和 `api.yaml` 的路径来生成代码，配置文件中可以定义生成代码的各种设置和选项。

项目推介：
作为一个活跃发展的开源项目，`oapi-codegen` 不断吸引着众多的关注和贡献。自项目迁移到了自己的组织以后，其开发更为活跃，且连续发布了多个版本，不断地增加新特性和改进。其遵循 Go 的惯用设计、生成代码的简洁性以及对 OpenAPI 3.x 广泛特性的支持，使得 `oapi-codegen` 成为 Go 开发者实现 OpenAPI 规范自动化的首选工具。此外，项目的文档详细，上手简单，即使是对 OpenAPI 或 Go 新手也能迅速掌握使用方法。综上所述，无论是对于大型企业还是个人开发者，`oapi-codegen` 都是极具价值的工具，值得尝试和使用。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=oapi-codegen/oapi-codegen&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/oapi-codegen/oapi-codegen 

开源项目作者：oapi-codegen

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=oapi-codegen/oapi-codegen)

关注我们，一起探索有意思的开源项目。

