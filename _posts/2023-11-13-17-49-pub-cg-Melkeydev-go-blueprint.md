---
layout: post
title: Go 开发新项目的脚手架工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在进行 Golang 项目开发时，我们常常会被初始化项目的繁琐步骤所困扰，尤其是当项目框架复杂、模块繁多的时候令人头疼，比如：搭建项目结构、设置 HTTP 服务器、集成流行的 Golang 框架等等。这些重复且机械的工作，极度消耗我们的时间与精力，使得我们无法更专注于应用程序的业务代码编写。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240820225758262.png)

今天要给大家推荐一个 GitHub 开源项目 go-blueprint，该项目在 GitHub 有超过 3.4k Star，用一句话介绍该项目就是：Go-blueprint allows users to spin up a quick Go project using a popular framework

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231216223558261.png)

###### 项目介绍

Go-blueprint 是一款 CLI 工具，可以帮助我们轻松启动新的 Golang 项目，并且有着完整的项目框架与清晰的项目结构，过程无需任何人为干预，一气呵成。同时它还能与诸多热门的 Golang 框架无缝集成，支持的框架如下：Chi、Gin、Fiber、HttpRouter、Gorilla/mux 以及 Echo。通过这个工具，我们可以把更多的精力投入到实际的业务代码开发中，而无需分心去处理其他琐事。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240827235022269.png)

以下是一个示例的使用介绍：

![](https://raw.githubusercontent.com/Melkeydev/go-blueprint/master/./public/blueprint_1.png)

###### 如何使用

通过如下方式可快速进行安装试用：

```sh
go install github.com/melkeydev/go-blueprint@latest
```

然后在新的终端运行以下命令来创建新的项目：

```sh
go-blueprint create
```

项目创建成功后，你还可以使用提供的标记来完成项目的设置，且无需与用户界面进行任何交互。

```sh
go-blueprint create --name my-project --framework gin --driver postgres
```

同时也可以使用交互界面进行使用，请输入 `go-blueprint create -h` 查看介绍。

###### 项目推介

`Go-blueprint` 是一款非常活跃的开源项目，虽是新生项目，但因其优秀的设计理念和强大的功能已经引起了大量开发者的关注。无论是搭建项目的便捷，还是框架的集成方面，都给开发者带来了极大的便利。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231216224009456.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Melkeydev/go-blueprint&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Melkeydev/go-blueprint 

开源项目作者：Melkeydev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Melkeydev/go-blueprint)

关注我们，一起探索有意思的开源项目。

