---
layout: post
title: GitHub 开源项目 MightyMoud/sidekick 介绍，Bare metal to production ready in mins; your own fly server on your VPS.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 MightyMoud/sidekick，该项目在 GitHub 有超过 6.4k Star。

![](https://stats.deeptrain.net/repo/MightyMoud/sidekick/?theme=light)

一句话介绍该项目：Bare metal to production ready in mins; your own fly server on your VPS.




![](https://emoji.aranja.com/static/emoji-data/img-apple-160/1f91c-1f3fb.png)

![](https://emoji.aranja.com/static/emoji-data/img-apple-160/1f91b-1f3fb.png)

![](https://raw.githubusercontent.com/MightyMoud/sidekick/master//demo/imgs/hero.png)

![](https://raw.githubusercontent.com/MightyMoud/sidekick/master//demo/imgs/init.png)

![](https://raw.githubusercontent.com/MightyMoud/sidekick/master//demo/imgs/launch.png)

![](https://raw.githubusercontent.com/MightyMoud/sidekick/master//demo/imgs/deploy.png)

![](https://raw.githubusercontent.com/MightyMoud/sidekick/master//demo/imgs/preview.png)


###### 项目介绍

### 背景介绍

在当今这个快速迭代的数字时代，软件开发和部署的需求日益增长。无论是个人开发者还是小型企业，都希望能够快速、高效地将应用部署到生产环境中。然而，从裸金属服务器到生产就绪的过程往往既复杂又耗时，尤其是对于那些缺乏专业 DevOps 团队支持的小规模项目来说。问题在于要安装和配置多个工具（如 Docker、Traefik 等）、处理 SSL 证书、实现零停机部署和高可用性等，这一切都使得应用部署变成了一个头疼的问题。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-b0cb737fbfa41e907aaf8a4df27bf9c1.png)

项目介绍

 **Sidekick** 是一个旨在将这一过程简化为分钟级任务的开源项目。通过只需一个命令，就能快速将您的 VPS（虚拟私人服务器）从裸金属转变为生产就绪状态，令人联想到 fly.io 但在您自己的 VPS 上实施。项目的主要卖点包括：一键 VPS 设置、从 Dockerfile 部署任意应用、零停机部署、高可用性和负载均衡、零配置 SSL 证书、内置支持 SOPS 加密等等。Sidekick 致力于降低托管边项目的复杂性，通过其出色的设计，即便是价格低廉的 VPS 实例（例如每月 8 美元的 DigitalOcean 实例），也能承受大量流量。

### 如何使用

安装 **Sidekick** 十分简单，如果是 MacOS 用户，可以通过 `brew` 进行安装：

```bash
brew install sidekick
```

使用起来也非常直接。一旦您拥有运行 Ubuntu LTS 的 VPS（推荐使用 DigitalOcean 或 Hetzner，但只要有公网 IP 地址即可），您只需进行如下几步：

1. **VPS 设置**

   运行 `sidekick init` 命令，并按照提示输入 VPS 的 IP 地址和用于设置 SSL 证书的邮箱地址。该命令将自动配置您的 VPS，安装必要的软件，并执行一系列的安全最佳实践。

2. **启动新应用**

   确保应用文件夹中有一个可用的 `Dockerfile`，然后运行 `sidekick launch`。该命令将引导您完成应用的部署过程，包括将应用容器化并且部署到您的 VPS 上。

3. **部署新版本**

   应用部署后，更新应用版本非常简单。只需执行 `sidekick deploy`，Sidekick 将处理剩余的事情，确保零停机更新应用。

### 项目推介

**Sidekick** 是一个面向那些寻求快速、无痛部署应用到生产环境的开发者和小型企业的理想解决方案。该项目是由一位具有深厚开源贡献背景的开发者创建，其简单但功能强大的特点已经吸引了一群忠实的用户群体。通过结合 Docker、Traefik 和 SOPS 的最佳实践，它有效地解决了小至个人项目，大至需要高可用性部署的企业应用的问题，展现了其强大的功能和极致的便捷性。无论您是一位独立开发者，还是正在寻找一个能够让团队快速上手并且降低运维负担的解决方案，**Sidekick**

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=MightyMoud/sidekick&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/MightyMoud/sidekick 

开源项目作者：MightyMoud

开源协议：GNU General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=MightyMoud/sidekick)

关注我们，一起探索有意思的开源项目。

