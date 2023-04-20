---
layout: post
title: 一个基础设施即代码（IaC）的 AI 代码生成器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 gofireflyio/aiac，该项目在 GitHub 有超过 1.1k Star，用一句话介绍该项目就是：“Artificial Intelligence Infrastructure-as-Code Generator.”，一个基础设施即代码（IaC）的 AI 代码生成器。

![](https://raw.githubusercontent.com/gofireflyio/aiac/master/logo-header.svg#gh-light-mode-only)

![](https://raw.githubusercontent.com/gofireflyio/aiac/master/demo.gif)

aiac 是一个命令行工具，借助 OpenAI 的 API 来生成 IaC 的代码模版、配置等，只需要描述你要做什么，aiac 会智能生成对应的 IaC 代码，能够提升写代码和配置的效率。

以下是 aiac 目前支持的场景举例，更多的使用场景你只需要发挥你的想象，会有惊喜的。

![image-20230319182645202](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/image-20230319182645202.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gofireflyio/aiac&type=Timeline)

### 如何安装使用

aiac 项目可以通过以下步骤进行安装：

1、brew 安装

```bash
brew install gofireflyio/aiac/aiac
```

2、在 docker 环境下使用

```bash
docker pull ghcr.io/gofireflyio/aiac
```

3、Go 或者源码编译安装

```bash
go install github.com/gofireflyio/aiac/v2@latest

git clone https://github.com/gofireflyio/aiac.git
go build
```

注意：在使用 aiac 库之前，需要先注册 OpenAI 并获取 API key，然后在代码中设置。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/gofireflyio/aiac 

开源项目作者：gofireflyio

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gofireflyio/aiac)



关注我们，一起探索有意思的开源项目。
