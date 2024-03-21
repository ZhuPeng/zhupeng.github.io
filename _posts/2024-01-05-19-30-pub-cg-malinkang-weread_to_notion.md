---
layout: post
title: 将微信读书划线同步到 Notion
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在信息时代，获取知识的途径不再局限于实体书籍，而是延伸到了各式各样的电子阅读平台，微信读书就是其中的一个重要代表。但是，对于广大喜欢在阅读过程中做笔记、划重点的读者来说，往往会遇到一个尴尬的局面——即便在微信读书上划过重点，标注过笔记，也无法有效地进行整理和管理，更不用说与自己其他的笔记工具，比如 Notion 进行同步。这就导致了我们对知识的美好消费遇到了阻碍，既不能实时复习，也无法做到灵活地跨平台调用。

今天要给大家推荐一个 GitHub 开源项目 malinkang/weread_to_notion，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“将微信读书划线同步到Notion”。


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224224224364.png)

###### 项目介绍

本项目通过 Github Action 每天定时将你在微信读书上的划线内容同步到 Notion，且提供对应预览效果。而且，由于是开源项目，你可以完全掌握它的运行逻辑，做到真正意义上的自由掌控。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224224437045.png)

###### 如何使用

使用这个项目非常简单，克隆该项目仓库，并设置好 GitHub Action 已经相关的参数即可进行同步。需要设置的参数包括微信读书 Cookie、Notion API Token 等。

以下是具体的 GitHub Action Workflow 执行代码：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224224656005.png)

###### 项目推介

对于广大 Notion 与微信读书用户来说，该项目无疑提供了极大的便利，旨在弥合知识获取与管理之间的断层。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=malinkang/weread_to_notion&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/malinkang/weread_to_notion 

开源项目作者：malinkang

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=malinkang/weread_to_notion)

关注我们，一起探索有意思的开源项目。

