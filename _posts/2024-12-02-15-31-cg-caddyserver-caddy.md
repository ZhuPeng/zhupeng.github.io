---
layout: post
title: GitHub 开源项目 caddyserver/caddy 介绍，Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 caddyserver/caddy，该项目在 GitHub 有超过 58.7k Star。

![](https://stats.deeptrain.net/repo/caddyserver/caddy/?theme=light)

一句话介绍该项目：Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS




![](https://user-images.githubusercontent.com/1128849/210187356-dfb7f1c5-ac2e-43aa-bb23-fc014280ae1f.svg)

![](https://user-images.githubusercontent.com/55066419/208327323-2770dc16-ec09-43a0-9035-c5b872c2ad7f.svg)

![](https://user-images.githubusercontent.com/1128849/49704830-49d37200-fbd5-11e8-8385-767e0cd033c3.png)


###### 项目介绍

### 背景介绍

在互联网日益成熟的今天，网站安全和用户体验已成为每个网站开发者和维护者的首要挑战。HTTPS 的普及不仅是提升网站安全的重要手段，还是优化用户体验、提高网站可靠性的关键。然而，部署 HTTPS 并不总是一帆风顺，从获取证书、配置服务器到维护和更新，每一步都可能遭遇技术和操作上的阻碍。此外，随着 HTTP/2 和 HTTP/3 的兴起，对服务器的性能和兼容性要求更高，这对很多开发者来说是一个不小的挑战。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-975f99f3da6171a3a716030481452eb8.png)

项目介绍

**Caddy** 是一个快速、可扩展的跨平台 HTTP/1-2-3 网络服务器，其最大特点是默认自动实现 HTTPS。Caddy 不仅简化了网站的 HTTPS 配置过程，还通过其创新的设计，提供了易于理解的配置文件（Caddyfile）、动态配置、自动化证书管理等特性，极大地降低了网站安全部署的门槛。它支持 HTTP/1.1、HTTP/2 和 HTTP/3，保证了网站的高性能和未来兼容性。除此之外，Caddy 通过其高度模块化的架构，支持各种插件扩展，无论是在性能、安全还是功能方面，都能满足开发者的需求。

### 如何使用

首先，您可以通过 [GitHub Releases](https://github.com/caddyserver/caddy/releases) 方便地下载 Caddy 的可执行文件，并将其放置在系统的 PATH 中以方便使用。

安装后，您可以创建一个简单的 Caddyfile 来配置您的网站：

```plaintext
example.com {
    root * /var/www
    file_server
}
```

运行 Caddy：

```bash
caddy run
```

Caddy 将自动处理 HTTPS 的证书获取和续订，您的网站将通过 HTTPS 安全访问。更详细的安装和使用说明，请参考官方文档 [Caddy 安装文档](https://caddyserver.com/docs/install)。

### 项目推介

Caddy 已经在生产环境中服务了数万亿次请求，并成功管理了数百万个 TLS 证书，证明了其稳定、可靠的产品特性。其高度的可扩展性和对最新网络协议的支持使其成为当前和未来开发高性能、安全网站的理想选择。Caddy 由一个活跃的社区支持，定期更新和改进，保证了项目的活力和时代性。它适用于从小型个人项目到大型企业级应用的广泛用途，无论是开发新网站还是将现有网站迁移至更安全、更快的平台，Caddy 都是一个值得考虑的优秀选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=caddyserver/caddy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/caddyserver/caddy 

开源项目作者：caddyserver

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=caddyserver/caddy)

关注我们，一起探索有意思的开源项目。

