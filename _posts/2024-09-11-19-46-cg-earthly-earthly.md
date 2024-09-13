---
layout: post
title: GitHub 开源项目 earthly/earthly 介绍，Super simple build framework with fast, repeatable builds and an instantly familiar syntax – like Dockerfile and Makefile had a baby.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 earthly/earthly，该项目在 GitHub 有超过 11.3k Star。

![](https://stats.deeptrain.net/repo/earthly/earthly/?theme=light)

一句话介绍该项目：Super simple build framework with fast, repeatable builds and an instantly familiar syntax – like Dockerfile and Makefile had a baby.




![](https://raw.githubusercontent.com/earthly/earthly/master/img/logo-banner-white-bg.png)

![](https://raw.githubusercontent.com/earthly/earthly/master/docs/img/get-earthly-button.png)

![](https://raw.githubusercontent.com/earthly/earthly/master/docs/img/integration-diagram-v2.png)

![](https://raw.githubusercontent.com/earthly/earthly/master/img/demo-351683.gif)

![](https://raw.githubusercontent.com/earthly/earthly/master/img/demo-351678.gif)

![](https://raw.githubusercontent.com/earthly/earthly/master/img/demo-351674.gif)

![](https://raw.githubusercontent.com/earthly/earthly/master/docs/guides/img/ref-infographic-v2.png)


###### 项目介绍

### 背景介绍

在现代软件开发中，构建过程的复杂性正日益增加。开发者面临着多种编程语言和框架的混合使用，以及需在多个环境下确保构建结果一致性的挑战。传统的构建工具，如 Makefile 和 Dockerfile，虽然各有千秋，但当涉及到跨语言支持和复杂构建逻辑时，它们往往显得力不从心。此外，构建缓存管理、依赖隔离、以及构建步骤的复用也是常见的痛点。这些问题不仅影响构建的速度和可靠性，而且还会加重开发者的维护负担。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6a7abab1269ddf2e0722ad54e8ed7e62.png)

项目介绍

**Earthly** 提供了一个既简单又强大的构建框架，旨在解决现代软件开发中遇到的构建相关挑战。它将 Dockerfile 和 Makefile 的优点结合起来，采用容器化的方式执行构建任务，确保了构建的一致性和可重复性。Earthly 的语法直观易懂，无需深入学习即可上手，同时支持所有语言、框架和构建工具，只要它们能在 Linux 上运行。此外，Earthly 针对单体仓库和多仓库都提供了良好的支持，能够自动执行并行构建和缓存管理，大大提高构建速度，并且支持构建逻辑的复用，避免重复劳动。

### 如何使用

首先，您需要安装 Earthly。对于大多数操作系统，Earthly 可以通过简单的命令行安装：

```bash
# Linux / macOS
/bin/bash -c "$(curl -fsSL https://earthly.dev/install.sh)"
```

安装完成后，您可以创建一个 `Earthfile` 定义您的构建逻辑。下面是一个简单的例子，展示了如何构建一个 Go 项目：

```Dockerfile
# Earthfile

VERSION 0.1

go:
  FROM golang:1.13-alpine3.11
  WORKDIR /usr/myapp
  COPY go.mod go.sum ./
  RUN go mod download
  COPY . .
  RUN go build -o myapp .
  SAVE ARTIFACT myapp /usr/myapp/myapp AS LOCAL myapp
```

使用 Earthly 构建项目，只需执行：

```bash
earthly +go
```

### 项目推介

Earthly 自推出以来，受到了开发社区的广泛关注和好评。它的开发活跃，持续接受社区的反馈和贡献，保持着积极的更新频率。

Earthly 的设计理念受到了众多知名技术人士的认可，并且已经被多家知名公司采用，用于提高他们的构建效率并保证构建结果的一致性。其简洁的语法和强大的功能，使其在现代软件开发的构建场景中，成为了一个不可或缺的工具。

依托于容器技术，Earthly 不仅解决了环境一致性的问题，还通过构建缓存和并发执行等高级特性，大幅缩短了构建时间。无论你是在处理一个包含多种编程语言的复杂项目，还是搜索一个能够提高团队构建效率的解决方案，Earthly 都值得一试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=earthly/earthly&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/earthly/earthly 

开源项目作者：earthly

开源协议：Mozilla Public License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=earthly/earthly)

关注我们，一起探索有意思的开源项目。

