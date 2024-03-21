---
layout: post
title: 有效追踪和检测 Go 代码中的潜在 panic
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

测试工作中，你是否遇到过在生产中突然出现 nil 空值 panic（程序崩溃）的问题？这些问题出现的时间点往往是在编译之后而非之前，给我们的开发工作带来了极大的不便。如果我们能在编译时期就发现这些潜在的问题，那将更为理想。

今天要给大家推荐一个 GitHub 开源项目 uber-go/nilaway，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“Static Analysis tool to detect potential Nil panics in Go code”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306224914777.png)

###### 项目介绍

NilAway 融合了尖端的静态分析技术，能够有效追踪和检测到潜在的 nil 空值 panic，并提供帮助开发者更方便修复问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306224951628.png)

相比于标准的 [nilness 分析器](https://pkg.go.dev/golang.org/x/tools/go/analysis/passes/nilness)，NilAway 具有以下三大优点：

1、**全自动**：NilAway 内嵌一个推理引擎，不需要开发者提供额外的代码注释或者信息

2、**快捷**：NilAway 的速度快，适应性强，适合大型代码库使用，在启用 NilAway 时，观察到构建时间的增加不超过5%。同时后续会不断对其进行优化，以降低 its footprint

3、**实用**：NilAway 并不能预防你的代码中的所有 nil panic，但在大部分我们在生产环境中遇到的潜在 nil panic，NilAway 都可以检测到，保持了良好的平衡在使用性和构建时间开销之间。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240306225152778.png)

###### 如何使用

安装与使用 NilAway 非常简单，你只需进行简单的几步操作：

```shell
go install go.uber.org/nilaway/cmd/nilaway@latest
```

然后运行 lint 命令：
```shell
nilaway ./...
```

NilAway 也为你提供了很多有用的示例和详尽的使用文档，可以帮助你快速上手和解决问题。

###### 项目推介

该工具由 Uber 公司开发并持续维护。这是一个具有巨大潜力的项目，不论你是刚入门的新手还是经验丰富的大神，都值得你一试。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=uber-go/nilaway&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/uber-go/nilaway 

开源项目作者：uber-go

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=uber-go/nilaway)

关注我们，一起探索有意思的开源项目。

