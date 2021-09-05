---
layout: post
title: 我不会 PS，但我有一键智能抠图
tags: 前端
---

大家好。

不知道大家会不会 PS（Photoshop），反正我是不会。有时候需要将某个图片里的人物或者元素抠出来，放在另外一个图片上，反正我是琢磨了很久依然不是很上道。作为一个程序员，懒惰是我的天性，所以我需要一个能够自动化帮我抠图的工具。

今天要推荐的就是一个智能抠图工具 backgroundremover，以下是抠图效果：

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_zhinengkoutu.png)

访问网站也可以直接试用抠图效果：https://backgroundremover.app/

backgroundremover 是作者第一个开源项目，所以作者专门写了一篇博客记录了为什么开发这个工具。详情：https://johnathannader.com/my-first-open-source-project/

作者最开始的问题是需要通过邮件发送一些图片，但是因为图片的背景中往往包含一些隐私信息，所以他试着想能不能自动把照片的背景信息自动去除。作者是一个完全的新手，为此他还专门买了两本书，并为了学习机器学习提前补了一些线性代数的知识。后来作者在 u2net 上发现了一个可用的模型，就包装成了一个网站用来自动抠图，并且发送到了 HackerNews 上，没想到如此的受欢迎，并且有人希望作者开源这个项目。因此作者就此走上了开源之路。

这个故事告诉我们，如果你也想做一个开源项目，先不用想，先去做吧。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/nadermx/backgroundremover
