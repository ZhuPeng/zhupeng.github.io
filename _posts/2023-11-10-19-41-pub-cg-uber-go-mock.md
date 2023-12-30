---
layout: post
title: GoMock - Google 开源并由 Uber 持续维护的 Go 测试 Mock 框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在进行 Go 语言的开发过程中，我们会碰到需要实现模拟功能来对各种接口进行测试。然而，手动实现模拟接口是一个既繁琐又容易出错的过程，在一般的测试流程中，我们一般会配合使用一些 Mock 框架。那么问题来了，Go 语言中有哪些这样的框架？

今天要给大家推荐一个 GitHub 开源项目 uber-go/mock，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“GoMock is a mocking framework for the Go programming language.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203175626252.png)

###### 项目介绍

GoMock 是一个针对 Go 语言的框架，它可以方便地生成模拟接口，支持与 Go 的内置 `testing` 包进行整合，也可以在其他上下文中使用。该项目源自 Google 的 `golang/mock` 仓库，但 Google 已经不再维护这个项目，鉴于 Uber 内部对 GoMock 项目的大量使用，Uber 决定接手并继续维护该项目。GoMock 支持所有 Go 官方发布策略支持的 Go 版本，即最近的两个 Go 发行版。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203175936184.png)

###### 如何使用

安装 GoMock 的 `mockgen` 工具，只需要执行以下命令：

```bash
go install go.uber.org/mock/mockgen@latest
```

使用 `mockgen` 工具，我们既可以通过源模式从源文件生成模拟接口，也可以通过反射模式构建一个使用反射来理解接口的程序生成模拟接口。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203175720327.png)

###### 项目推介

虽然 GoMock 项目原始的维护者 Google 已经不再维护该项目，但当前的维护者 Uber 对此项目提供了强有力的维护与支持。另外，没有了这个项目，我们开发时很可能需要手动实现模拟接口，这无疑会增加我们的工作负担。因此，如果你正在使用 Go 语言进行开发，并且有模拟接口的需求，我强烈推荐你选用 GoMock 项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=uber-go/mock&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/uber-go/mock 

开源项目作者：uber-go

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=uber-go/mock)

关注我们，一起探索有意思的开源项目。

