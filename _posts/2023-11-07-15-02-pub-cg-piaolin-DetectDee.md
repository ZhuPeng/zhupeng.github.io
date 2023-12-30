---
layout: post
title: DetectDee 通过多种方式（用户名、电子邮件或电话）帮助用户搜索社交网络上的账户
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现今社交媒体盛行的时代，人们经常需要查找某个人在不同社交网络上的账户。然而，由于网络平台众多且分散，手动搜索成为一项繁琐且耗时的工作。此外，对于网络安全从业人员而言，了解账户在不同社交媒体上的存在与否也是一项重要的任务。

今天要给大家推荐一个 GitHub 开源项目 piaolin/DetectDee，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“DetectDee: Hunt down social media accounts by username, email or phone across social networks.”。

![](https://s2.loli.net/2023/05/28/gpxRJqvWr21Ifmh.gif)

###### 项目介绍

DetectDee 旨在通过多种方式（用户名、电子邮件或电话）帮助用户搜索目标在社交网络上的账户。该项目具有以下特点：

1、包括网络安全从业人员经常使用的网站。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231129223935485.png)

2、精确的线程控制和自定义请求头，用于防止 Web 应用程序防火墙（WAF）的识别。

3、可扩展、简单易用的模板，使用户能够对项目进行灵活定制。

4、整合了社交网络站点的移动版界面，使用户能够方便地在移动设备上使用。

###### 如何使用

以下是使用 DetectDee 项目的安装和使用方法：

1、下载推荐方式：https://github.com/piaolin/DetectDee/releases 

2、源码编译方式：

```shell
git clone https://github.com/piaolin/DetectDee.git
cd DetectDee
go mod tidy
go run .
```

可直接使用命令 DetectDee，使用示例参考如下：
- 搜索单个用户：
  ```shell
  ./DetectDee detect -n piaolin
  ```
- 搜索多个用户：
  ```shell
  ./DetectDee detect -n piaolin,blue
  ```
- 搜索邮件地址：
  ```shell
  ./DetectDee detect -e mail@gmail.com,test@163.com
  ```
- 搜索电话号码：
  ```shell
  ./DetectDee detect -p 15822575984,13188524682
  ```
- 显示 Google 搜索结果：
  ```shell
  ./DetectDee detect -n piaolin,blue -g
  ```
- 在指定站点搜索：
  ```shell
  ./DetectDee detect -n piaolin -s github,v2ex
  ```

![](https://s2.loli.net/2023/05/13/OWRDnU98TyCdceN.jpg)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=piaolin/DetectDee&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/piaolin/DetectDee 

开源项目作者：piaolin

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=piaolin/DetectDee)

关注我们，一起探索有意思的开源项目。

