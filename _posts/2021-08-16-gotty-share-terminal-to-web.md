---
layout: post
title: 实用工具推荐，命令行终端网页分享工具
tags: Go 相关
---

大家好。

今天给大家推荐一个比较实用的小工具，GoTTY 可以将远程服务器执行的命令变成一个 Web 应用，可以将执行命令的输出在网页中进行展示，同时也支持在网页中进行交互。我们先来看个例子，在网页中展示远程服务器的 TOP 执行结果。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/cover.gotty.gif)

GoTTY 使用 Go 进行开发，所以在安装和使用上都非常的简单，各大操作系统都直接支持。以下是两种安装方法：

```bash
# Homebrew 安装
brew install sorenisanerd/gotty/gotty
# Go 原生安装，可获取最新开发的版本进行体验
go get github.com/sorenisanerd/gotty
```

使用方法很简单，使用 gotty + 需要执行的命令即可在在网页 ip:8080 查看到命令的输出。另外还支持在网页上进行命令交互，只需增加 -w 参数。另外还支持很多其他功能的参数大家可以详细研究一下。

![image-20210816002702455](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210816002702455.png)

小编经过几分钟的体验之后，觉得 GoTTY 使用起来真的太方便了，从自身的使用场景来看，GoTTY 可以用来做很多的事情，比如监控实时显示机器的命令执行情况、Web 编辑器方便更改远程服务器的文件等。在编辑的场景下，GoTTY 也支持了很多安全上的功能，保证使用上的安全。整体来看，GoTTY 是一个非常不错且简洁好用的工具，非常推荐。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/sorenisanerd/gotty
