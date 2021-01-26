---
layout: post
title: 命令行录屏工具
tags: 其他
---

经常在微信写文章的，会注意到微信对图片的大小有严格的控制，尤其对于 gif 类的图片来说，经常由于图片过大而出现上传不了。我们在这方面碰到过很多的问题，开始的解决方案是压缩、压缩，但是有时候压缩了还是上传不了。实在没办法只能在 gif 的图片里面找几张有代表性的，单独发图片放弃 gif 的动态效果。

为了解决这个问题，我们只能自己上手录制 gif 来控制质量和大小，第一步就是自己找几个录屏工具学习一下。

* termtosvg

非常方便，但是录屏的文件是 svg 格式的，微信不支持，如果不是在微信展示的话，生成的动图还是不错的。

> 项目地址：<https://github.com/nbedos/termtosvg>



* asciinema

将终端的操作记录成 JSON 格式，然后使用 JavaScript 解析，配合CSS展示，看起来像是视频播放器。
实际上就是文本，相比GIF和视频文件体积非常之小（时长2分50秒的录屏只有325KB），无需缓冲播放，
也可以方便的分享给别人或嵌入到网页中。微信也不支持~



* ttygif

安装方式

```shell

# MacOS 
brew install ttygif
  
# Other
git clone https://github.com/icholy/ttygif.git
cd ttygif
make
sudo make install
```

使用方式

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/tty.gif)

上面是我录的，主要原因还是我的环境被我玩坏了，年久失修。而项目中展示录屏 Demo 连微信都上传不了😭，截图大家看一下吧。

![image-20190515215639393](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/ttyfig-demo.png)

> 项目地址：https://github.com/icholy/ttygif



* terminalizer

安装方式：`npm install -g terminalizer`

官方效果还是很不错的，但是我败在了网速了，连 npm 安装都没完成：

![image-20190515221055847](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/download-slow.png)

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/install-dl.gif)

> 项目地址：<https://github.com/faressoft/terminalizer>

看一下上面的录屏工具其实都不那么完美，欢迎留言说一说你们是如何解决这样的问题的，或者可以推荐一些你们常用的工具。