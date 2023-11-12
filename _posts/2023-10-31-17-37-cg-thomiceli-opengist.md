---
layout: post
title: Opengist - 一个开源可替代 Github Gist 的代码片段分享工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常开发工作中，经常会遇到需要分享代码片段的情况，而 Github Gist 是一个非常好的选择。然而，Github Gist 是一个闭源的服务，我们无法自行部署和定制。这就是我们需要一个开源、可自我托管的代码片段分享工具的原因。而 Opengist 正是为了解决这个问题而诞生的。

今天要给大家推荐一个 GitHub 开源项目 thomiceli/opengist，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Self-hosted pastebin powered by Git, open-source alternative to Github Gist.”。


![](https://raw.githubusercontent.com/thomiceli/opengist/a9dd531f676d01b93bb6bd70751a69382ca563b0/public/opengist.svg)

###### 项目介绍

Opengist 是一个由 Git 驱动的自我托管的代码片段分享工具。所有的代码片段都存储在一个 Git 仓库中，可以通过标准的 Git 命令或者 web 界面进行读取和修改。它与 Github Gist 类似，但是开源的，可以自我托管。

Opengist 的主要特性包括：
- 创建公开、未列出或私有的代码片段
- 通过 HTTP 或 SSH 的 Git 进行初始化 / 克隆 / 拉取 / 推送代码片段
- 修订历史记录
- 语法高亮；支持 markdown 和 CSV
- 喜欢 / Fork 代码片段
- 浏览、搜索用户的代码片段
- 下载原始文件或作为 ZIP 存档
- 通过 GitHub、Gitea 和 OpenID Connect 进行 OAuth2 登录
- 对匿名用户限制或取消限制代码片段的可见性
- 支持 Docker

以下是对应的网页示例：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231111201231994.png)

###### 如何使用

Opengist 提供了 Docker、二进制文件和源代码三种安装方式。其中，Docker 方式最为简单，只需要拉取 Docker 镜像，然后通过 docker-compose.yml 文件进行部署，即可在 6157 端口运行 Opengist。

对应的 docker-compose.yml 配置参考如下：

```yaml
version: "3"

services:
  opengist:
    image: ghcr.io/thomiceli/opengist:1
    container_name: opengist
    restart: unless-stopped
    ports:
      - "6157:6157" # HTTP port
      - "2222:2222" # SSH port, can be removed if you don't use SSH
    volumes:
      - "$HOME/.opengist:/opengist"
```

对应的二进制及源代码安装方式可参考 GitHub 页面介绍。

项目推介

Opengist 由 thomiceli 开发和维护，它是 Github Gist 的开源替代品，可以自我托管，非常适合需要自定义和控制代码片段分享工具的团队和个人使用。如果你正在寻找一个开源、可自我托管的代码片段分享工具，那么 Opengist 是一个非常好的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=thomiceli/opengist&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/thomiceli/opengist 

开源项目作者：thomiceli

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=thomiceli/opengist)

关注我们，一起探索有意思的开源项目。

