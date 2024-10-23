---
layout: post
title: 用一杯茶的时间，搭建你的 Git 服务
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

Git 作为当前最流行的版本控制系统，被广泛使用于项目代码管理、团队合作及开源项目贡献等场景。然而，对于希望独立部署、自主管理 Git 服务的团队和个人来说，配置一个既功能全面又易于维护的 Git 服务平台往往意味着面临复杂的安装配置过程和维护难题。来自不同平台的兼容性问题、繁琐的系统依赖及配置更新成为了许多人避之不及的阻碍。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-de1770fbaada52ec0f12693cf1a0e4a9.png)

今天要给大家推荐一个 GitHub 开源项目 gitea，该项目在 GitHub 有超过 44.7k Star。

![](https://stats.deeptrain.net/repo/go-gitea/gitea/?theme=light)

一句话介绍该项目：Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241023225159529.png)

###### 项目介绍

Gitea 发音为 /ɡɪ'ti:/，像是在说 "gi-tea"，带有硬 g 的发音。Gitea 是一个开源的、轻量级、易于部署的 Git 服务，拥抱 **一站式** 软件开发服务，包含 Git 托管、代码审查、团队协作、包注册以及 CI/CD 等功能。

![](https://dl.gitea.com/screenshots/home_timeline.png)

不同于其他重量级的 Git 服务，它的宗旨是提供 **最易搭建**、**最快速度** 和 **最无痛的自托管 Git 服务搭建方式**。Gitea 采用 Go 语言编写，支持包括 Linux、macOS 和 Windows 在内的所有 Go 支持的平台和架构，从 x86 到 amd64 再到 ARM 和 PowerPC 架构均无障碍运行。自 2016 年 11 月从 [Gogs](https://gogs.io) 分叉以来，Gitea 经历了快速而持续的优化和进化。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241023225410235.png)

###### 如何使用

从源码构建 Gitea 相对简单，需要确保安装了 [Go Stable](https://go.dev/dl/) 和 [Node.js LTS](https://nodejs.org/en/download/)。构建命令如下：

```bash
TAGS="bindata" make build
# Support SQLite
TAGS="bindata sqlite sqlite_unlock_notify" make build
```

构建完成后，通过运行 `./gitea web` 启动 Gitea Web 服务。更多详细信息，请访问 [Gitea Document](https://docs.gitea.com/)。

部分系统页面截图如下：

![](https://dl.gitea.com/screenshots/user_profile.png)

![](https://dl.gitea.com/screenshots/web_editor.png)

![](https://image.ibb.co/e02dSb/6.png)

###### 项目推介

Gitea 不仅在开源社区活跃，而且得到了广泛的使用和认可。其开发活跃，持续更新，拥有一支热情的贡献者和维护者团队确保了项目的活力和进步。此外，Gitea 使用 MIT 许可证发布，这意味着它拥有极高的自由度和广泛的兼容性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241023225844465.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-gitea/gitea&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-gitea/gitea 

开源项目作者：go-gitea

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-gitea/gitea)

关注我们，一起探索有意思的开源项目。

