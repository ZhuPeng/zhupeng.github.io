---
layout: post
title: GitHub 开源项目 KurtBestor/Hitomi-Downloader 介绍，:cake: Desktop utility to download images/videos/music/text from various websites, and more.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 KurtBestor/Hitomi-Downloader，该项目在 GitHub 有超过 19.0k Star，一句话介绍该项目：:cake: Desktop utility to download images/videos/music/text from various websites, and more.




![](https://raw.githubusercontent.com/KurtBestor/Hitomi-Downloader/master/imgs/card_crop.png)

![](https://raw.githubusercontent.com/KurtBestor/Hitomi-Downloader/master/imgs/how_to_download.gif)



在当今的数字时代，互联网上充满了大量有价值的图片、音视频、文本等各类资源。然而，我们常常会遇到抓取这些资源的困难，需要在不同的网站上使用各种复杂的抓取工具，且不同工具界面操作各异、方位相当零碎。希望能有一个全能一体的、安装简便的、支持多线程、且用户界面友好化的应用，则就是开源项目 Hitomi-Downloader 在解决的痛点。

Hitomi-Downloader 是一款跨平台的全能下载工具。该项目方便用户从各种网站上抓取图片、音频、视频、文本等资源。它的功能强大，设计细致，包括但不限于 24 线程的下载加速、速度限制、用户脚本支持、BitTorrent & Magnet 支持、M3U8 & MPD 格式视频支持、剪贴板监控等功能，甚至还支持黑夜模式，并且便携式的设计让你随时随地待用。最重要的是，Hitomi-Downloader 支持超过 50 多个网站资源的抓取，包括 YouTube、bilibili、pixiv、Instagram 等等。

安装和使用 Hitomi-Downloader 非常简单。你只需要访问项目的 [GitHub页面](https://github.com/KurtBestor/Hitomi-Downloader)，点击最新版本的下载链接进行下载安装即可。为了让您更好地理解项目的功能和操作，以下是一段简单的使用示例：

```
# 导入必要的模块
from hitomi_downloader import HitomiDownloader

# 创建抓取对象，输入需要抓取的网址链接
downloader = HitomiDownloader("https://www.example.com")

# 启动抓取过程
downloader.start()

# 控制下载速度，单位为 KB/s
downloader.set_speed_limit(1000)

# 若提前停止下载，下载进度可以保存在本地，下次可以继续前舍弃的进度，不须从头开始
downloader.save_progress("progress.hdp")
downloader.load_progress("progress.hdp")
```

根据项目 README 中提供的信息，Hitomi-Downloader 是一个活跃的开源项目，作者 KurtBestor 更新频繁且维护周全。无论你是开发者还是终端用户，我都强烈推荐你尝试使用 Hitomi-Downloader，它可以极大的提升你的资源获取效率且操作简易。让我们去 GitHub 支持并关注这个优秀的项目吧！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=KurtBestor/Hitomi-Downloader&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/KurtBestor/Hitomi-Downloader 

开源项目作者：KurtBestor

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=KurtBestor/Hitomi-Downloader)

关注我们，一起探索有意思的开源项目。

