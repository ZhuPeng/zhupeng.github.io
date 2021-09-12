---
layout: post
title: 牛逼，使用 GitHub Pages 搭建维基百科
tags: 前端
---

大家好。

维基百科大家知道吗？这个可以称之为互联网百科全书的网站，拥有数不胜数的词条，可谓“海纳百川，有容乃大”，同时维基百科是由非营利组织──维基媒体基金会负责维持。

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_wiki.demo.png)

今天要推荐的项目跟维基百科有关系，也是一项技术的概念验证，使用 GitHub Pages 搭建一个离线版本的静态维基百科。访问 http://static.wiki/zh 可以直接试用，页面右上角可以直接切换语言。

![image-20210822225402811](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210822225402811.png)

![image-20210822230950772](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210822230950772.png)

接下来我们来简单介绍一下以上技术上是如何实现的。

具体的介绍可以参考：https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/

首先这个技术是源于一个背景，作者经常会需要在网页上展示一些静态的数据，如果使用后端的话，一来比较浪费，第二有时候忘记对主机续费的话，网站就不行了，有很大的维护成本。而维护一个静态的网站就简单很多了，基于以上出发点，作者尝试依赖 GitHub Pages，同时结合 SQLite 来搭建静态网站。

核心技术要点就是将 SQLite (written in C) 编译成 WebAssembly，这样就可以使用 sql.js 读取 sqlite 的数据库文件了。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/segfall/static-wiki
