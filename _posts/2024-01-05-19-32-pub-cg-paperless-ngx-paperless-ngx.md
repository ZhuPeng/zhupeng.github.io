---
layout: post
title: 无纸化办公工具，支持文档扫描、索引和归档
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常生活、学习和工作中，我们难免要面对大量的纸质文件和资料，这些文件可能包含了重要的信息，需要妥善保管。然而，纸质文件易遗失、易损坏，且查询和管理都需要极大的精力和时间，这无疑是一项颇有挑战的任务。

今天要给大家推荐一个 GitHub 开源项目 paperless-ngx/paperless-ngx，该项目在 GitHub 有超过 14.5k Star，用一句话介绍该项目就是：“A community-supported supercharged version of paperless: scan, index and archive all your physical documents”。

![](https://github.com/paperless-ngx/paperless-ngx/raw/main/resources/logo/web/png/Black%20logo%20-%20no%20background.png)

###### 项目介绍

 `paperless-ngx` 项目是一款让你拥有无纸化办公生活的工具。它是原始的 `Paperless` 和 `Paperless-ng` 项目的官方继任者，致力于更好地扫描、索引和归档所有的实体文件，使其变为可搜索的在线存档，从而达到减少纸张使用的目的，更重要的是让你可以从极其繁琐的文件管理中解脱出来。

`paperless-ngx` 具有众多特色功能，如 OCR 识别、全文搜索、多种文件类型支持等等。

![](https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/docs/assets/screenshots/documents-smallcards.png)

###### 如何使用

项目用 docker-compose 进行部署，使用起来非常便捷。相关的安装脚本如下：

```bash
bash -c "$(curl -L https://raw.githubusercontent.com/paperless-ngx/paperless-ngx/main/install-paperless-ngx.sh)"
```
如果你手上已经安装了依赖软件，并且自己设定了 apache 和数据库服务器，你可以参考官方文档自行部署。同时，从 `Paperless-ng` 迁移到 `paperless-ngx` 也十分简单，只需要换一下 docker 镜像即可。

###### 项目推介

`paperless-ngx` 项目的开发活跃，项目质量得到了保证，而且它得到了不少的用户支持和赞誉。另外 `paperless-ngx` 提供了多语言支持，你还可以加入他们的翻译团队，帮助这个项目开发出更完善且适合你自身使用的版本。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224225656335.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=paperless-ngx/paperless-ngx&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/paperless-ngx/paperless-ngx 

开源项目作者：paperless-ngx

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=paperless-ngx/paperless-ngx)

关注我们，一起探索有意思的开源项目。

