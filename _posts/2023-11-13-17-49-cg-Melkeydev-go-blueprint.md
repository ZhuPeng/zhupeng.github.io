---
layout: post
title: GitHub 开源项目 Melkeydev/go-blueprint 介绍，Go-blueprint allows users to spin up a quick Go project using a popular framework
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Melkeydev/go-blueprint，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Go-blueprint allows users to spin up a quick Go project using a popular framework”。


![Starter Image](https://raw.githubusercontent.com/Melkeydev/go-blueprint/master/./public/blueprint_1.png)
![Framework Image](https://raw.githubusercontent.com/Melkeydev/go-blueprint/master/./public/blueprint_2.png)



### 背景介绍
在进行 Golang 项目开发时，我们常常会被初始化项目的繁琐步骤所困扰，尤其是当项目框架复杂、模块繁多的时候，令人头疼，比如：搭建项目结构、设置 HTTP 服务器、集成流行的 Golang 框架等等。这些重复且机械的工作，极度消耗我们的时间与精力，使得我们无法更专注于应用程序的业务代码编写。

### 项目介绍
接下来给大家带来的是一个非常棒的开源项目 —— [Go-blueprint](https://github.com/Melkeydev/go-blueprint)，它是一款 CLI 工具，可以帮助我们轻松启动新的 Golang 项目，并且有着完整的项目框架与清晰的项目结构，过程无需任何人为干预，一气呵成。同时，它还能与诸多热门的 Golang 框架无缝集成，所支持的框架包括但不限于：Chi、Gin、Fiber、HttpRouter、Gorilla/mux 以及 Echo。此外就是，通过这个工具，我们可以把更多的精力投入到实际的业务代码开发中，而无需分心去处理其他琐事。

### 如何使用
在具体的使用上，`Go-blueprint`提供了非常多的安装方式，从而满足了各种安装需求。以下介绍两种最常用的安装方法。

下载并安装 `go-blueprint` 的最简单方式是使用 `Homebrew`：

```sh
brew install go-blueprint
```

同时，也可以通过 `Go` 命令进行安装：

```sh
go install github.com/melkeydev/go-blueprint@latest
```

然后在新的终端运行以下命令来创建新的项目：

```sh
go-blueprint create
```

项目创建成功后，你还可以使用提供的标记来完成项目的设置，且无需与用户界面进行任何交互。如：

```sh
go-blueprint create --name my-project --framework gin
```

有关所有选项和速记符，请输入 `go-blueprint create -h` 查看。

### 项目推介
`Go-blueprint` 是一款非常活跃的开源项目，虽是新生项目，但因其优秀的设计理念和强大的功能已经引起了大量开发者的关注。无论在搭建项目的便捷，还是在框架的集成方面，都给开发者带来了极大的便利。如果你恰好是一名 Golang 开发者，并且喜欢尝试新的技术、新的工具，那么 `Go-blueprint` 值得你一试！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Melkeydev/go-blueprint&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Melkeydev/go-blueprint 

开源项目作者：Melkeydev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Melkeydev/go-blueprint)

关注我们，一起探索有意思的开源项目。

