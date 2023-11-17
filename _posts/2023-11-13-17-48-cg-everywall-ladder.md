---
layout: post
title: GitHub 开源项目 everywall/ladder 介绍，Selfhosted alternative to 12ft.io. and 1ft.io bypass paywalls with a proxy ladder and remove CORS headers from any URL
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 everywall/ladder，该项目在 GitHub 有超过 2.1k Star，用一句话介绍该项目就是：“Selfhosted alternative to 12ft.io. and 1ft.io bypass paywalls with a proxy ladder and remove CORS headers from any URL”。


![](https://raw.githubusercontent.com/everywall/ladder/master/assets/pigeon.svg)



背景介绍：
随着网络技术的发展，越来越多的媒体机构都选择使用付费墙来获取收益。这虽然从一定程度上满足了媒体机构的财务需求，但同时也限制了公众获取信息的权利。尤其是公众对知识的需求和获取，这可能被一部分付费墙所阻挡。突破这一难题需要寻求一种创新的方法，既可以保证媒体的可持续性，也可以尽可能保障公众的知识获取权。

项目介绍：
Ladder 是一个网络代理项目，它可以帮助用户绕过付费墙，是 [1ft.io](https://1ft.io) 和 [12ft.io](https://12ft.io) 的自托管版本。主要的功能有：突破付费墙，从响应、资源、图像等中移除 CORS 标头，进行域名基的规则设置/代码修改响应，使网站可浏览，API、获取 RAW HTML、自定义用户代理、自定义 X-Forwarded-For IP 等等。支持 Docker 容器、Linux 二进制、Mac OS 二进制、Windows 二进制，并且无需记忆繁琐的日志和配置，同时也不进行追踪。

如何使用：
安装非常方便，可以直接在 [这里](https://github.com/everywall/ladder/releases/latest) 下载二进制文件，解压后运行二进制 `./ladder`就可以了。如果你做的是 Docker 容器，可以使用下面的命令进行安装：
```bash
docker run -p 8080:8080 -d --name ladder ghcr.io/everywall/ladder:latest
```
使用方法也非常简单。在浏览器中打开默认链接 http://localhost:8080，输入 URL 地址，然后按下回车键就可以了。你也可以直接在代理 URL 的后面添加 URL，如：http://localhost:8080/https://www.example.com。如果你喜欢使用命令行，可以使用下面的命令：
```bash
curl -X GET "http://localhost:8080/api/https://www.example.com"
```

项目推荐：
Ladder 开源项目目前活跃度非常高，其作者对项目的维护也非常积极，持续不断的进行更新改进，这对于一个开源项目来说是非常重要的。虽然 Ladder 还在持续进行开发中，但它已经提供了丰富的特性和强大的功能，得到了广大用户的一致好评，因此我推荐大家也可以试试看这个项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=everywall/ladder&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/everywall/ladder 

开源项目作者：everywall

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=everywall/ladder)

关注我们，一起探索有意思的开源项目。

