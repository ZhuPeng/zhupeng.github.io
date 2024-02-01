---
layout: post
title: 微信聊天记录提取与报告生成利器
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常生活中，我们经常会遇到一些由于微信消息记录过多，导致无法快速找到一些重要信息的问题。此外，由于微信的储存方式，消息记录可能会在手机更换或者软件卸载之后丢失，让一些珍贵的、有价值的历史消息无法保存和回顾。再者，对于一些喜欢数据分析和自我反思的朋友们来说，微信聊天记录也是一个重要的信息来源，但微信并未提供类似统计功能，使得我们无法分析自己的社交行为。

今天要给大家推荐一个 GitHub 开源项目 WeChatMsg，该项目在 GitHub 有超过 16.6k Star，用一句话介绍该项目就是：“提取微信聊天记录，将其导出成 HTML、Word、CSV 文档永久保存，对聊天记录进行分析生成年度聊天报告”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240124223006592.png)

###### 项目介绍

WeChatMsg 不仅可以帮助我们提取微信中的聊天记录，让聊天记录永久保存，而且支持将聊天记录文件导出为 HTML，Word，CSV 等多种格式，全方位满足我们对文件归档的需求。最重要的是，这款工具还可以基于抽取的聊天记录进行数据分析，生成年度聊天报告，使得我们可以在年末回顾一下特殊的一年中自己在社交活动上的一些数据和变化情况。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240124223145701.png)

以下是生成的一些示例的报告：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240124223226228.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240124223235855.png)

###### 如何使用

使用 WeChatMsg 的步骤如下：

1、克隆或者下载这个项目到本地

```sh
git clone https://github.com/LC044/WeChatMsg
```
2、在本地的文件夹中安装依赖

```sh
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
3、获取微信聊天记录，并运行主程序选择导出格式

首先要登录微信将聊天记录备份到电脑的本地目录，参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240124223429415.png)

```sh
python main.py
```

注意: 运行时需要手机的操作支持，以获取微信的登录权限，更多详细信息可参考项目 README 介绍。

###### 项目推介

该工具在 GitHub上已经获得了大量的 Star，而且项目最近一段时间更新非常的频繁。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240124223637216.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=LC044/WeChatMsg&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/LC044/WeChatMsg 

开源项目作者：LC044

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=LC044/WeChatMsg)

关注我们，一起探索有意思的开源项目。

