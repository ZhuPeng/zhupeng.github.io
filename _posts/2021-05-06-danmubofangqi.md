---
layout: post
title: 一个支持弹幕的网页视频播放器
tags: 前端
---

大家好。

弹幕基本上是现在视频网站的标配了，是在视频之上另一种创造，互联网上不少流行的语录都是从弹幕来的呢。如果让你自己实现一个带弹幕功能的网页视频播放器，你会怎么实现呢？

巧了，今天要给大家推荐一个非常好用的支持弹幕的网页视频播放器 NPlayer。NPlayer 是由 Typescript 加 Sass 编写，无任何第三方运行时依赖，Gzip 大小只有 21KB，兼容 IE11，支持 SSR。该播放器可高度定制，所有图标、按钮、色彩等都可以自由替换，并且提供了内置组件方便进行二次开发。它还拥有插件系统，弹幕功能就是使用插件形式提供，当然你也可以定制自己的插件。该播放器可以接入任何流媒体，如 hls、dash 和 flv 等。

安装和使用参考如下，安装使用 npm 即可：

![image-20210506211000818](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210506211000818.png)

引入使用非常的简单，最终效果也非常棒。

![image-20210506211030015](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210506211030015.png)

![img](https://nplayer.js.org/img/preview.jpg)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/woopen/nplayer
