---
layout: post
title: 易于集成到 GitHub 中的代码贡献卡片
tags: GitHub
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 anuraghazra/github-readme-stats，该项目在 GitHub 有超过 50.0k Star，用一句话介绍该项目就是：“Dynamically generated stats for your github readmes”。

anuraghazra/github-readme-stats 是一个开源项目，它可以在 GitHub 上的项目 README 文件中显示项目的各种统计信息，如贡献者、语言、星标数量等。这个项目使用简单，可以通过在 README 中添加一个图片链接来轻松实现。它对于项目状态的展示是非常有用的工具。


### 使用示例 DEMO

下面是一份在 README 文件中使用 anuraghazra/github-readme-stats 的示例图片：

![image-20230127193815989](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230127193815989.png)

图片显示的是 anuraghazra 的 GitHub 统计信息，如果要在 Markdown 上展示，对应使用如下代码。

```markdown
[![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=anuraghazra)](https://github.com/anuraghazra/github-readme-stats)
```

对应使用的 API 是  https://github-readme-stats.vercel.app/api?username=anuraghazra ，你可以替换 `anuraghazra` 为你自己的 GitHub 用户名来显示你自己的统计信息。上面的链接是官方提供的链接，在此基础上可以自己搭建服务。

除此之外，该项目还支持很多其他形式的 GitHub 的卡片信息，比如如下：

![image-20230127194154127](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230127194154127.png)

![image-20230127194205821](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230127194205821.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anuraghazra/github-readme-stats  (文末可点击阅读原文)

开源项目作者：anuraghazra

