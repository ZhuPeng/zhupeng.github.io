---
layout: post
title: GitHub 开源项目 navidrome/navidrome 介绍，🎧☁️ Modern Music Server and Streamer compatible with Subsonic/Airsonic
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 navidrome/navidrome，该项目在 GitHub 有超过 11.2k Star。

![](https://stats.deeptrain.net/repo/navidrome/navidrome/?theme=light)

一句话介绍该项目：🎧☁️ Modern Music Server and Streamer compatible with Subsonic/Airsonic




![PikaPods](https://www.pikapods.com/static/run-button.svg)

![](https://raw.githubusercontent.com/navidrome/navidrome/master/resources/logo-192x192.png)

![](https://raw.githubusercontent.com/navidrome/navidrome/master/.github/screenshots/ss-mobile-login.png)

![](https://raw.githubusercontent.com/navidrome/navidrome/master/.github/screenshots/ss-mobile-player.png)

![](https://raw.githubusercontent.com/navidrome/navidrome/master/.github/screenshots/ss-mobile-album-view.png)

![](https://raw.githubusercontent.com/navidrome/navidrome/master/.github/screenshots/ss-desktop-player.png)


###### 项目介绍

### Navidrome：您的个人化音乐云服务

**背景介绍：**

在数字音乐愈发普及的时代，每个人的音乐库都在迅速扩大。随之而来的问题是，我们如何有效管理并享受这些音乐资源？尽管市面上有如 Spotify、Apple Music 等流行的音乐流媒体服务，但它们可能无法完全覆盖每个人的个性化需求，比如播放特定的格式文件或是对本地音乐库进行流媒体传输。同时，对于致力于精心整理音乐元数据的乐迷来说，这些服务在个性化展示方面也许并不尽如人意。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-90eee02cd898d00f6aeaa346632dff3d.png)

项目介绍：**

Navidrome 应运而生，提供了一个现代化、兼容 Subsonic/Airsonic 的音乐服务器和流媒体解决方案。它是一个开源的基于网络的音乐收藏服务器和流媒体服务，使您能够通过任何浏览器或移动设备自由聆听音乐收藏。这就像拥有了个人的 Spotify！它支持处理庞大的音乐收藏，几乎支持所有可用的音频格式，能够读取并使用您精心策划的所有元数据。此外，Navidrome 特别优化了对合集和多碟辑的支持，是多用户环境中的理想选择，每位用户都有自己的播放计数、播放列表、收藏等，且资源占用极低。

**如何使用：**

Navidrome 的安装过程十分简单。您可以访问项目的官方网站（[Navidrome 安装指南](https://www.navidrome.org/docs/installation/)），了解如何通过 Docker、预构建的二进制文件或源代码来安装 Navidrome。安装完成后，Navidrome 会自动监控您的音乐库中的变更，导入新文件并刷新元数据，您即可开始享用您的个人音乐流媒体服务。

```bash
# 举个例子，以下是使用 Docker 启动 Navidrome 的命令
docker run -d --name navidrome \
    -p 4533:4533 \
    -v /path/to/your/music/folder:/music \
    -v /path/for/navidrome/data:/data \
    deluan/navidrome
```

**项目推介：**

Navidrome 自开源以来，受到了广大音乐爱好者和技术社区的高度评价。它不仅提供了适用于所有主要平台的现成二进制文件（包括树莓派），而且资源占用极低，使其成为持家及小型服务器的理想选择。项目致力于持续更新和改进，拥有活跃的社区支持，并且提供实时演示，让潜在用户能够轻松体验其强大功能。无论是从技术实现还是用户反馈来看，Navidrome 都证明了其作为个人音乐云服务的巨大潜力和价值。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=navidrome/navidrome&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/navidrome/navidrome 

开源项目作者：navidrome

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=navidrome/navidrome)

关注我们，一起探索有意思的开源项目。

