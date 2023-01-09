---
layout: post
title: GitHub 开源洞察，一个更好的 GitHub Trending 替代
tags: GitHub
---

大家好。

前段时间 GitHub 官宣要下线 Trending 页面，多少有点遗憾。虽然 GitHub Trending 有一些不好的地方，但是不得不说，很多人每天都会访问 GitHub Trending 页面来找一些有意思的开源项目，其中我们就是 Trending 的重度用户。虽然现在 Trending 页面还能访问，但是也不好说什么时候还会再下线，毕竟 GitHub 说了算。

今天要推荐另外一个有同等功能的网站，Open Source Software（OSS），该网站通过实时分析 GitHub 上的相关事件，并通过 TiDB 提供了可实时查看和分析 GitHub 趋势的能力，也就是 GitHub 洞察。

![image-20221114211647938](https://raw.githubusercontent.com/ZhuPeng/pic/master/blog/compress_image-20221114211647938.png)

首页提供了一个简洁的搜索输入框，可以输入开发者名字或者仓库名来洞察分析其趋势。往下滑就是我刚说的 Trending Repos 了，是不是和 GitHub Trending 有几分相似。

![image-20221114211815369](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20221114211815369.png)

除此之外，还提供了一个根据不同领域进行聚合的仓库列表，包括静态网站生成器、开源数据库等等。

![image-20221114211912933](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20221114211912933.png)

如果你是一个技术控，该网站还提供了一个实时的数据看板，不得不说技术范十足。

![image-20221114212155420](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20221114212155420.png)

除了以上介绍的之外，OSS 网站还有很多的其他功能，包括博客会介绍他们是如何构建 OSS 的，以及相应的 API 介绍，可以使用 Trending API 方便集成到你的网页应用上。

更多详情请查看如下链接：https://ossinsight.io/
