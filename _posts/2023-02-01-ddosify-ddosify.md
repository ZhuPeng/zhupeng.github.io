---
layout: post
title: 安装和使用都很简单的压力测试工具
tags: 工程效率&GO
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ddosify/ddosify，该项目在 GitHub 有超过 5.4k Star，用一句话介绍该项目就是：“High-performance load testing tool, written in Golang. For distributed and Geo-targeted load testing.”，使用 Golang 开发的高性能压力测试工具，专门针对分布式及地理定位相关的应用。

![](https://raw.githubusercontent.com/ddosify/ddosify/master/assets/ddosify-logo-wb.svg#gh-light-mode-only)

以下是 ddosify 项目的功能概览：

![image-20230127195420954](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230127195420954.png)

ddosify 目前支持 HTTP、HTTPS、HTTP/2 协议，可基于 JSON 对压测场景进行定制等等。

以下是 ddosify 的一个使用示例，会对网站 https://app.servdown.com 进行压力测试，默认是按 100/10s 进行测试。


![](https://raw.githubusercontent.com/ddosify/ddosify/master/assets/ddosify-quick-start.gif)

### 如何安装使用

ddosify 支持使用 Docker、包管理工具（brew、pkg 等）、curl 下载等方式进行安装。以下方式可任选其中一个：

```bash
docker run -it --rm ddosify/ddosify

brew install ddosify/tap/ddosify

curl -sSfL https://raw.githubusercontent.com/ddosify/ddosify/master/scripts/install.sh | sh

go install -v go.ddosify.com/ddosify@latest
```

安装后可以直接使用命令 ddosify 进行测试，通过不同的参数可以配置不同的测试场景，也能集成到 CI/CD 流水线中。

![image-20230127200240222](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230127200240222.png)


ddosify 安装和使用都非常的简单，是一个不错的提升项目质量的工具。更多项目详情请查看如下链接。

开源项目地址：https://github.com/ddosify/ddosify  (文末可点击阅读原文)

开源项目作者：ddosify

