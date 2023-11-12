---
layout: post
title: obligator - 专为自托管者设计且简单的 OpenID Connect (OIDC) 服务工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常的开发和运维工作中，我们经常会遇到需要自建 OpenID Connect (OIDC) 服务的需求。然而，市面上的开源 OIDC 服务器虽然众多，但往往不能满足我们对于特定功能组合的需求，比如简单的部署和管理、支持匿名 OAuth2 客户端认证、支持多域名同时认证、无密码邮箱登录等等。这些问题的存在，使得我们在实际操作中经常感到困扰。

今天要给大家推荐一个 GitHub 开源项目 anderspitman/obligator，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Simple and opinionated OpenID Connect server designed for self-hosters”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029200158880.png)

###### 项目介绍

obligator 是一个相对简单且有自己独特见解的 OpenID Connect (OIDC) 服务提供者服务器，专为自托管者设计。它的设计理念是基于电子邮件构建身份，虽然电子邮件并不完美，但它是我们现在拥有的全球唯一的联邦身份。因此，obligator 的目的是尽可能简单地验证用户控制电子邮件地址，并将此信息传达给用户试图登录的应用程序。验证可以直接通过 SMTP 完成，也可以委托给上游 OIDC 或一些纯 OAuth2 提供商。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029200244218.png)

###### 如何使用

obligator 的使用非常简单，你可以通过 docker 来快速启动它，只需要创建一个目录，将配置文件复制到该目录，然后运行 docker 命令即可。如果你不想使用 docker，也可以从发布页面下载静态可执行文件。

```bash
mkdir obligator_docker/
cp obligator_storage.json obligator_docker/

docker run --user $(id -u):$(id -g) --rm -it -v $PWD/obligator_docker:/data -v $PWD/obligator_docker:/api -p 1616:1616 anderspitman/obligator:latest -storage-dir /data -api-socket-dir /api -root-uri example.com -port 1616
```

###### 项目推介

虽然 obligator 目前还处于预发布测试阶段，但它的设计理念和功能特性都非常值得我们关注和试用。如果你是一个自托管者，需要自建 OIDC 服务，那么 obligator 无疑是一个非常好的选择。同时，项目作者也非常欢迎大家对项目进行测试和反馈，特别是对于安全性方面的反馈。让我们一起期待 obligator 的正式版本的发布！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=anderspitman/obligator&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anderspitman/obligator 

开源项目作者：anderspitman

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=anderspitman/obligator)

关注我们，一起探索有意思的开源项目。

