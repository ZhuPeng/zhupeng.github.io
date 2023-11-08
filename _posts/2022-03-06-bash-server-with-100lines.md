---
layout: post
title: 只有 100 行的 Web Server 项目，非常值得学习
tags: Bash Web
---

大家好。

100 行代码可以干些什么？如果只是简单批处理一些任务，100 行还是可以干很多的东西的，尤其使用 Python 这种相对高级的语言。但是如果要使用 Bash 这样的语言呢？本身抽象并没有那么高，而且用 Bash 来开发一个 Web Server，真的可以吗？

![image-20220306214918056](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220306214918056.png)

今天要推荐的开源项目 Bash-web-server，一个用纯 Bash 写的 Web Server，而且代码只有 100 多行，没有使用 socat、netcat 等已经有相对完善的网络处理工具。

既然只有 100 多行（实际代码行数，加上注释和空行是 331 行），那我就不多废话了，直接上才艺，Show me your code。

![image-20220306215853471](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220306215853471.png)

![image-20220306220110894](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220306220110894.png)

![image-20220306220138864](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220306220138864.png)

虽然代码不多，但是要真正读懂它，还是需要你对 Bash 有一定的理解，所以说这个开源项目是一个非常好的 Bash 学习材料。 

而且这个项目目前还在迭代，看后续的 TODO 计划中，还要增加 Basic 认证和 Session 的处理，未来可期啊。

![image-20220306220710318](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220306220710318.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dzove855/Bash-web-server
