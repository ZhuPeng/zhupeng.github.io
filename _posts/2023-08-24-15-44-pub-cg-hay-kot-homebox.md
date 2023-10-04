---
layout: post
title: Homebox - 一个为家庭用户打造的库存和组织系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 hay-kot/homebox，该项目在 GitHub 有超过 1.4k Star，用一句话介绍该项目就是：“Homebox is the inventory and organization system built for the Home User”。


![](https://raw.githubusercontent.com/hay-kot/homebox/master//docs/docs/assets/img/lilbox.svg)

###### 项目介绍

Homebox 是一个为家庭用户打造的库存和组织系统。在我们的日常生活中，我们经常会遇到需要管理和组织家庭物品的问题，这些物品可能包括食品、药品、家庭用品等等。Homebox 就是为了解决这些问题而设计的。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230831222105921.png)

Homebox 项目提供了一个简单易用的库存管理系统，可以帮助用户轻松地记录和管理家庭物品。该系统具有多种功能，包括添加、编辑、删除、搜索和分类等。此外，Homebox 还提供了一个用户友好的界面，使用户可以轻松地浏览和管理他们的库存。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230831222239436.png)

Homebox 的主要设计要点包括：易用性、可扩展性和可定制性。该项目使用了现代化的技术栈，包括 React、Node.js 和Docker 等。这使得 Homebox 可以轻松地部署和扩展，同时还可以根据用户的需求进行定制。

如果你想使用Homebox，你可以通过 Docker Compose 进行安装和部署。此外，该项目还提供了详细的文档和演示，以帮助用户更好地了解和使用该系统。

使用网站可以直接试用：https://homebox.fly.dev/

或者使用如下命令进行本地安装：

```bash
# If using the rootless image, ensure data 
# folder has correct permissions
mkdir -p /path/to/data/folder
chown 65532:65532 -R /path/to/data/folder
docker run -d \
  --name homebox \
  --restart unless-stopped \
  --publish 3100:7745 \
  --env TZ=Europe/Bucharest \
  --volume /path/to/data/folder/:/data \
  ghcr.io/hay-kot/homebox:latest
# ghcr.io/hay-kot/homebox:latest-rootless
```

如果你是一个家庭用户，需要一个简单易用的库存管理系统，那么 Homebox 绝对是一个值得尝试的项目。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=hay-kot/homebox&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/hay-kot/homebox 

开源项目作者：hay-kot

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=hay-kot/homebox)

关注我们，一起探索有意思的开源项目。

