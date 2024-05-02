---
layout: post
title: Nunu - 一个用于构建 Go 应用程序的脚手架工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们日常的开发工作中，构建 Go 应用程序可能会遇到一些问题，比如如何有效地组织代码，如何选择合适的库，如何保证应用的性能和安全性等。这些问题需要我们花费大量的时间和精力去解决。

![](https://img0.baidu.com/it/u=3633899761,2974414879&fm=253&fmt=auto&app=138&f=JPEG?w=443&h=293)

今天要给大家推荐一个 GitHub 开源项目 go-nunu/nunu，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“A CLI tool for building Go applications.”。

![](https://raw.githubusercontent.com/go-nunu/nunu/main/.github/assets/banner.png)

###### 项目介绍

Nunu 是一个用于构建 Go 应用程序的脚手架工具，它的名字来源于英雄联盟中的一个游戏角色，一个骑在雪人肩膀上的小男孩。就像 Nunu 一样，这个项目也站在巨人的肩膀上，它结合了 Go 生态系统中的流行库，使您能够快速构建高效且可靠的应用程序。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240425231844970.png)

Nunu 的主要特点包括：

1、低学习曲线和定制性：Nunu 封装了 Gophers 熟悉的流行库，允许您轻松定制应用程序以满足特定需求。

2、高性能和可扩展性：Nunu 旨在具有高性能和可扩展性。它使用最新的技术和最佳实践，以确保您的应用程序可以处理高流量和大量数据。

3、安全性和可靠性：Nunu 使用稳定和可靠的第三方库，以确保您的应用程序的安全性和可靠性。

4、模块化和可扩展性：Nunu 设计为模块化和可扩展。您可以通过使用第三方库或编写自己的模块轻松添加新功能。

5、完整的文档和测试：Nunu 提供了全面的文档和测试。它提供了大量的文档和示例，帮助您快速开始。它还包括一个测试套件，以确保您的应用程序按预期工作。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240425231820157.png)

以下是 Nunu 的项目结构：

![](https://raw.githubusercontent.com/go-nunu/nunu/main/.github/assets/layout.png)

###### 如何使用

Nunu 的使用非常简单，只需使用 go install 安装即可。然后通过命令行工具创建一个新的项目。在项目中，您可以根据自己的需求定制应用程序，例如添加新的功能或修改现有的功能。

![](https://raw.githubusercontent.com/go-nunu/nunu/main/.github/assets/screenshot.jpg)

具体使用流程参考如下：

1、创建项目

```bash
nunu new projectName
```

2、创建组件

```bash
nunu create handler user
nunu create service user
nunu create repository user
nunu create model user
```

3、运行项目

```bash
nunu run
```

###### 项目推介

Nunu 是一个很早期还没有得到广泛关注的项目。如果您是一位 Go 开发者，极度关注开发上的效率，建议关注该项目并参与进来共同建设。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-nunu/nunu&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-nunu/nunu 

开源项目作者：go-nunu

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-nunu/nunu)

关注我们，一起探索有意思的开源项目。

