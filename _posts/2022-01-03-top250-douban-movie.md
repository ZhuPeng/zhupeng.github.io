---
layout: post
title: 牛逼，豆瓣 TOP250 电影榜单播放链接收集
tags: 其他
---

大家好。

马上要过年放假了，工作搬砖的也能享受一波长假了，假期怎么能少得了刷剧看电影呢。

今天要推荐的一个开源项目，维护了 TOP250 豆瓣电影的榜单，并且将对应电影的播放链接收集起来了，可以在要看的时候非常方便的播放，太和我胃口了，毕竟现在我已经不喜欢提前将电影下载到硬盘里面。

![image-20220103203032871](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220103203032871.png)

如果榜单有变化的话，作者也配置了 GitHub Actions，使用爬虫自动获取豆瓣的 TOP250 电影榜单，并更新到 GitHub 仓库里面。GitHub Actions 之前介绍过不少了，除了能够做持续集成，其实不少的开源项目用来做一些自动化的工作，比如像这个项目一样，自动更新代码仓库的 README。以下是更新豆瓣 TOP250 榜单的 GitHub Actions 配置。

![image-20220103203949563](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220103203949563.png)

而电影的播放链接看上去是作者自己维护的，但是其实也是可以用爬虫来自动维护的，也可能作者还没有开源这部分。如果你知道更全的电影播放链接，也可以补充到这个开源项目中哦。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Mayandev/where-is-douban250
