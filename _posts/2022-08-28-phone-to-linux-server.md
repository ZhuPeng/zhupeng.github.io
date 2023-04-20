---
layout: post
title: 使用淘汰的智能手机搭建服务器
tags: 服务器
---

大家好。

大家过几年都会淘汰自己用的手机，但是近些年的智能手机其实算力还不错，只不过现在的 APP 越做越大，导致运行会有些问题。但是对于一个淘汰的安卓手机来说，用来当一个 Linux 的服务器还是绰绰有余的。一般的安卓手机都至少有 2GB ~ 4GB 的 RAM，CPU 的话一般是 4 核，甚至有的是 8 核的，所以基本可以等同于一个 AWS 上的 t2.nano 的服务器。

今天就要推荐一个博主，将自己的淘汰的摩托罗拉手机打造成一个 Linux 服务器的过程。以下是对应的过程：

1、安装 Termux APP，Termux 提供了一个在手机上使用的 Linux 的环境，可以在 Google 应用商店，或者搜索引擎搜索下载

2、设置 SSH，因为手机上输入命令比较麻烦，所以安装一个 SSH 可以让你在电脑上远程控制手机，并配置你的服务器。作者选择的 dropbear 软件，一款轻量级的 ssh 工具。以下是对应的安装配置命令：

![image-20220828150519585](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220828150519585.png)

3、设置静态的 IP，默认的 WiFi 连接都是使用 DHCP，你肯定不希望每次网络断开重连之后 IP 变化，所以设置一个静态的 IP 是很有必要的

4、安装你想要的应用软件，作者安装的是 Ruby 相关的 Web 服务器，同时安装了 Nginx。最后就实现了在安卓手机上搭建一个 Web 应用的效果。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_android-web-server.png)

整体感觉还是挺牛逼的，如果你手上有淘汰的手机，可以照着试一下，当然其实用你在用的手机尝试也是没有问题的。

更多项目详情请查看如下链接。

博客地址：https://lbrito1.github.io/blog/2020/02/repurposing-android.html

关注我们，一起探索有意思的开源项目。
