---
layout: post
title: 视频搜索会是下一个大规模流量入口？推荐一个仍在探索的视频搜索开源工具
tags: Python
---

大家好。

随着我们的生活越来越多的被视频所占据，通过视频我们可以追剧、记录生活、了解生活常识（做菜、做家务）等，可能未来的百科全书都会以视频的形式进行呈现。

前段时间字节跳动的 CEO 也公布了目前使用抖音视频搜索的月活跃用户已经超过了 5.5 亿。可见流量还是非常大的，视频搜索也许就是未来新的搜索入口。



![image-20210228224246110](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210228224246110.png)

而我们知道视频搜索相比文本的搜索是不一样的，要做好视频搜索并没有那么容易。文本信息能够直接提取，而视频中的信息需要经过图像处理技术多次处理才能获取，由于处理存在信息损耗问题，经过多次处理后会损失很多有用的信息。目前真正支持视频中内容的直接搜索仍是非常难的，尤其是商用。

今天要推荐的开源项目是一个支持通过自然语言直接搜索视频内容的小工具，目前只是概念上得到了认证。

在介绍原理之前，我们先介绍一下 OpenAI 的 CLIP 技术，它是一个机器学习的神经网络模型，能够将自然语言内容和图像进行关联。更多 CLIP 介绍参考：https://openai.com/blog/clip/ 。

![image-20210228225908758](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210228225908758.png)



而该项目就借助了 OpenAI 的 CLIP 技术，通过将视频的每一帧抽取出来，然后使用 CLIP 对每一帧进行编码。当我们使用文本搜索时，通过 CLIP 将文本进行编码，然后将每一帧的编码和文本编码进行计算，从而获取最匹配的图片作为搜索结果。



![image-20210228225408263](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210228225408263.png)

从作者的搜索效果来看非常的不错，以下是一些搜索的例子：

![image-20210228230617819](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210228230617819.png)



![image-20210228230636655](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210228230636655.png)



更多项目详情请查看如下链接。

开源项目地址：https://github.com/haltakov/natural-language-youtube-search
