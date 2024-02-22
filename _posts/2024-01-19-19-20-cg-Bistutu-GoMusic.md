---
layout: post
title: GitHub 开源项目 Bistutu/GoMusic 介绍，迁移网易云/QQ音乐歌单至 Apple/Youtube/Spotify Music
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Bistutu/GoMusic，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“迁移网易云/QQ音乐歌单至 Apple/Youtube/Spotify Music”。


![](https://raw.githubusercontent.com/Bistutu/GoMusic/master/misc/images/0.png)
![](https://raw.githubusercontent.com/Bistutu/GoMusic/master/misc/images/1.png)
![](https://raw.githubusercontent.com/Bistutu/GoMusic/master/misc/images/praise.jpeg)



背景介绍：
在数字音乐平台林立的今天，我们会面临一个十分痛苦的尴尬现象——向其他音乐平台迁移自己的歌单。考虑到每个平台都有自己的独家资源、特色推荐以及用户体验，这都使得我们不可避免的会使用多个平台。这就导致我们的喜爱歌曲、精心策划的音乐都散落在各个平台，给我们带来极大的不便。

项目介绍：
GoMusic 是一个使用 Golang + Gin 开发的后端项目，其前端使用 Vue + ElementUI 编写。此项目主要解决的问题正是我们每日会碰到的音乐平台间歌单的迁移问题，其目前主要支持网易云/QQ音乐歌单迁移至 Apple/Youtube/Spotify Music。

如何使用：
使用 GoMusic 相较简单：
1. 输入你在网易云 / QQ音乐中的歌单链接，如：http://163cn.tv/zoIxm3
2. 复制查询结果
3. 打开 **[TunemyMusic](https://www.tunemymusic.com/zh-CN/transfer)** 网站
4. 选择歌单来源“任意文本”，将刚刚复制的歌单粘贴进去，选择 Apple/Youtube/Spotify Music 作为目的地，确认迁移

要启动 GoMusic 程序你需要：
- 安装 Golang
- 将程序克隆至本地
- 编译并运行

```shell
git clone https://github.com/Bistutu/GoMusic.git
cd GoMusic
go build &&./GoMusic
```

项目推介：
目前 GoMusic 来源于 GitHub 平台，开源且开发活跃，作者 Bistutu 不仅有丰富的开源项目经验，而且响应用户的问题反馈也十分热心。此项目应有力的解决了跨平台歌单迁移的问题，让我们免去了人工搜索、转移的麻烦，并且操作简单，使用方便。想要了解更多关于这个项目的信息，你可以访问 GitHub 或是直接访问其主页：https://music.unmeta.cn （注：其支持简体中文、English、한국어 三种语言版本）。正当这个项目日益火热之时，你的 Star 将极大地激励作者的更新热情，让我们为它点赞吧！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Bistutu/GoMusic&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Bistutu/GoMusic 

开源项目作者：Bistutu

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Bistutu/GoMusic)

关注我们，一起探索有意思的开源项目。

