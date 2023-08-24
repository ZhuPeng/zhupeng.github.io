---
layout: post
title: OneAPI - 大模型 API Token 管理系统，支持超多模型
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在使用各种大模型进行开发时，我们常常需要管理和分发各种 API key，这个过程通常比较繁琐，而且容易出现各种问题，例如 key 泄露、使用不当等。为了解决这些问题，开发者 songquanpeng 开发了一个名为 OneAPI 的开源项目，它是一个 OpenAI 接口管理 & 分发系统，支持多种大模型，可以用于二次分发管理 key，仅单可执行文件，已打包好 Docker 镜像，一键部署，开箱即用。

GitHub 开源项目 one-api 有超过 3.1k Star，以下是对应的管理界面：
![](https://user-images.githubusercontent.com/39998050/233837954-ae6683aa-5c4f-429f-a949-6645a83c9490.png)
![](https://user-images.githubusercontent.com/39998050/233837971-dab488b7-6d96-43af-b640-a168e8d1c9bf.png)

###### 项目介绍

OneAPI 支持多种大模型，包括 OpenAI ChatGPT 系列模型、Anthropic Claude 系列模型、Google PaLM2 系列模型、百度文心一言系列模型、阿里通义千问系列模型、讯飞星火认知大模型和智谱 ChatGLM 系列模型。它还支持配置镜像以及众多第三方代理服务，例如 OpenAI-SB、API2D、OhMyGPT、AI Proxy、CloseAI 和自定义渠道，可以通过负载均衡的方式访问多个渠道。此外，OneAPI 还支持 stream 模式，可以通过流式传输实现打字机效果。它支持多机部署，并且支持令牌管理和兑换码管理，可以设置令牌的过期时间和额度，支持批量生成和导出兑换码，可使用兑换码为账户进行充值。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230819214027051.png)

###### 如何使用

OneAPI 是一个非常易于使用的开源项目，它已经打包好 Docker 镜像，可以一键部署，开箱即用。如果你想手动安装，可以参考项目 README 中的安装指南。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230819215006351.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230819215026775.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=songquanpeng/one-api&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/songquanpeng/one-api 

开源项目作者：songquanpeng

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=songquanpeng/one-api)

关注我们，一起探索有意思的开源项目。

