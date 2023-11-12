---
layout: post
title: Buf - 采用创新方式处理 Protocol Buffers 的 CLI 工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们进行 API 开发时，常常会遇到一些问题，比如如何保证 API 的设计质量、如何检测 API 的兼容性、如何管理 Protobuf 文件等。这些问题在使用 REST/JSON 进行 API 开发时尤为突出。为了解决这些问题，今天给大家推荐一种新的工具。

该工具 Buf 在 GitHub 有超过 7.4k Star，用一句话介绍该项目就是：“A new way of working with Protocol Buffers.”。


![](https://raw.githubusercontent.com/bufbuild/buf/master/./.github/buf-logo.svg)



###### 项目介绍

Buf 是一个用于处理 Protocol Buffers 的 CLI 工具，它提供了一种新的方式来处理这些问题。它的主要功能包括：

1、管理 Buf Schema Registry (BSR) 上的 Protobuf 资产

2、执行良好的 API 设计选择和结构的 linter

3、执行源代码或线路级别兼容性的破坏性变更检测器

4、基于可配置模板调用插件的生成器

5、以及符合行业标准的 Protobuf 文件格式化器

6、此外，它还与 Buf Schema Registry 完全集成，包括完整的依赖性管理。

###### 如何使用

你可以通过 Homebrew (macOS 或 Linux) 安装 Buf：

    brew install bufbuild/buf/buf

以上命令将安装：

- buf、protoc-gen-buf-breaking 和 protoc-gen-buf-lint 二进制文件
- Bash、Fish、Powershell 和 zsh 的 shell 自动命令补全脚本

其他的安装方法，可以参考官方文档，其中包括：

- 通过 npm 安装 buf
- 在 Windows上安装 buf
- 使用 buf 的 Docker 镜像
- 通过 GitHub Releases 从二进制文件、tarball 和源代码安装
- 使用 minisign 公钥验证发布

使用如下命令可以查看 buf 的命令使用帮助：

    buf --help

整体命令包含如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231019204910793.png)

以下是 buf generate 命令的详细工作逻辑，更多其他命令可以查看官方文档。

![](https://buf.build/mdx-bundles/for-all-docs/docs/generate/overview/local-generation-RPJLHG4O.png)

###### 项目推介

Buf 的目标是替代当前以 REST/JSON 为中心的 API 开发范例，用一种基于模式的范例来定义 API。使用 IDL 定义 API 比 REST/JSON 有许多优点，而 Protobuf 是目前最稳定、最广泛采用的 IDL。Buf 选择在这个广泛信任的基础上构建，而不是从头开始创建一个新的 IDL。

尽管 Protobuf 在技术上有优点，但实际使用 Protobuf 一直比需要的更具挑战性。Buf CLI 和 BSR 是该项目努力改变这一点的基石，该项目的目标是使 Protobuf 对服务所有者和客户端都可靠易用，换句话说，创建一个现代的 Protobuf 生态系统。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=bufbuild/buf&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/bufbuild/buf 

开源项目作者：bufbuild

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=bufbuild/buf)

关注我们，一起探索有意思的开源项目。

