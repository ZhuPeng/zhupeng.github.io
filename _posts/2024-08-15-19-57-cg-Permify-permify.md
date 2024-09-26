---
layout: post
title: 让精细权限管理变得简单
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

当构建复杂的应用程序时，开发者常常面临着实现精细、可伸缩的权限控制系统的挑战。不仅如此，随着业务发展，权限系统需要能够快速适应新的需求变化，而传统的权限系统往往难以满足这些要求。团队可能需要花费数月时间来构建和调整权限系统，这不仅耗费时间和资源，而且还可能影响到产品的迭代速度和市场响应。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-33835e85a60b121571602bc3d5dcdfc4.png)

今天要给大家推荐一个 GitHub 开源项目 permify，该项目在 GitHub 有超过 2.9k Star。

![](https://stats.deeptrain.net/repo/Permify/permify/?theme=light)

一句话介绍该项目：An open-source authorization as a service inspired by Google Zanzibar, designed to build and manage fine-grained and scalable authorization systems for any application.


![permify-centralized](https://github.com/user-attachments/assets/e1c22244-1fa4-4bc3-8b7a-bdfb97610c5f)


###### 项目介绍

Permify 是一个灵感来源于 Google Zanzibar 的开源授权服务项目，它旨在帮助开发者快速构建和管理细粒度、可扩展的权限系统，适用于任何应用程序。它通过抽象化的权限逻辑和一个特定的领域语言，让权限管理变得更加简单、安全且易于适应变化。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911223404170.png)

Permify 支持资源特定、层级式、上下文相关的权限和策略，兼容 RBAC、ReBAC 和 ABAC，让开发者能在几分钟到几天内部署起来，而不是花费数月。此外，Permify 提供了基于 Google Zanzibar 的高效基础设施，能够实现高达 10 毫秒的访问检查响应时间。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911223415732.png)

###### 如何使用

Permify 提供了 Docker 快速启动选项。通过简单的 Docker 命令就可以在本地启动：

```shell
docker run -p 3476:3476 -p 3478:3478  ghcr.io/permify/permify
```
你可以通过 GET 请求来测试服务是否启动：
```shell
localhost:3476/healthz
```
具体使用请参考文档、API 和 SDK 示例。

###### 项目推介

Permify 是由一群热心的开发者维护的活跃项目，其中不乏业界知名人士。它的设计灵感来源于 Google 的全球授权系统 Zanzibar，意味着它继承了被验证有效的设计原则和架构。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240911223635334.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Permify/permify&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Permify/permify 

开源项目作者：Permify

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Permify/permify)

关注我们，一起探索有意思的开源项目。

