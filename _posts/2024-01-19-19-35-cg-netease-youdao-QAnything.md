---
layout: post
title: 网易有道开源的本地化知识库问答系统，支持 PDF、Word 等自由检索
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常生活和工作中，我们时常面临大量本地信息资料（PDF、Doc 等）需要关联理解和处理。频繁地切换区分文件格式，加上需要跨语言理解的环境下，如何找到一个准确、快速、可靠地处理文件的解决方案恍若眼前一道难题。这个问题非常现实，也非常复杂，我们需要一个强大且可靠的工具来解决这个问题。

今天要给大家推荐一个 GitHub 开源项目 netease-youdao/QAnything，该项目在 GitHub 有超过 1.7k Star，一句话介绍该项目：Question and Answer based on Anything.

![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/images/qanything_logo.png)

###### 项目介绍

`QAnything`(**Q**uestion and **A**nswer based on **Anything**) 是一个本地化的知识库问答系统，可以支持大量的文件格式和数据库，并允许离线安装和使用。在 `QAnything` 的帮助下，你只需要简单地操作本地储存的文件，无论文件格式如何，都能收到精确、快捷、可靠的答案。

这个项目的主要功能包括：

- 数据安全，支持断网环境下的安装和使用
- 支持跨语言问答，可根据文档的语言自由切换中英文答案
- 支持大规模数据问答，使用二阶段检索排名，解决大规模数据检索降级问题
- 高性能生产级系统，可直接部署在企业环境下
- 用户友好，无需复杂配置，一键安装部署，开箱即用
- 多知识库问答支持，支持选择多个知识库进行问答

以下是系统的架构：

![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/images/qanything_arch.png)

###### 如何使用

在你开始使用 `QAnything` 之前，你需要先满足一些先决条件，比如：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240310222736786.png)

之后就可以参考如下方式下载安装了：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240310222813301.png)

在安装完毕后，可以直接浏览器使用，也可以使用 QAnything 提供的 API 对你的本地文件进行操作。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240310222842955.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240310223017837.png)

###### 项目推介

`QAnything` 项目是由网易有道出品，目前开发活跃。此项目的优势在于其能处理大量不同格式的数据，包括 PDF，Word, PPT ，Eml，TXT，图片等。同时也支持中英文对照，无论问答和文档的语言是什么，都可以自由切换。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=netease-youdao/QAnything&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/netease-youdao/QAnything 

开源项目作者：netease-youdao

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=netease-youdao/QAnything)

关注我们，一起探索有意思的开源项目。

