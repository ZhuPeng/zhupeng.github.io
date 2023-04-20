---
layout: post
title: 一款使用 Go 开发的简单但功能强大的博客平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 go-sonic/sonic，该项目在 GitHub 有超过 1.2k Star，用一句话介绍该项目就是：“Sonic is a blogging platform developed by Go. Simple and powerful”，一款使用 Go 开发的简单但功能强大的博客平台。

![](https://raw.githubusercontent.com/go-sonic/resources/master/logo/logo.svg)

![Default Theme](https://github.com/go-sonic/default-theme-anatole/raw/master/screenshot.png)
![Console](https://github.com/go-sonic/resources/raw/master/console-screenshot.png)

sonic 意为声速的、声音的，正如它的名字一样, sonic 致力于成为最快速的开源博客平台。以下是目前 sonic 项目支持的功能：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230311191240830.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-sonic/sonic&type=Timeline)

### 如何安装使用

sonic 项目可以通过 go get 命令安装：
```
go get -u github.com/go-sonic/sonic
```

在安装完成后，可以在 $GOPATH/src/github.com/go-sonic/sonic 目录中看到项目文件。

也可以直接下载源码并手动编译安装：
```
git clone https://github.com/go-sonic/sonic.git
cd sonic
make
```

编译完成后，会在当前目录生成 sonic 二进制文件。

在使用时，可以通过配置项来配置 sonic 的运行参数，例如监听地址、端口等。默认的端口是 8080，后台管理路径是 http://ip:port/admin。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-sonic/sonic 

开源项目作者：go-sonic

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-sonic/sonic)



关注我们，一起探索有意思的开源项目。
