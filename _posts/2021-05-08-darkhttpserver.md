---
layout: post
title: 小巧高性能低功耗的文件服务器
tags: 其他
---

大家好。

如何快速的搭建一个立马可以使用的 HTTP 或者文件服务器呢？如果你会用 Python 的话，有一个非常简单的方法：

python2

![image-20210508115010272](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210508115010272.png)

python3

![image-20210508115107026](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210508115107026.png)

通过这样的方式，你就可以在通过 curl 或者浏览器访问命令执行文件夹下面的文件。平时在各种虚拟机里面可以采用类似的方法快速的传输一些文件，只需要依赖 Python 比较简单。但是毕竟 Python 在性能和资源占用上并没有太大的优势。

今天要推荐给大家一个类似的工具 darkhttpd，使用 C 编写的文件服务器，编译后为一个二进制文件无任何依赖，同时性能高和资源占用极低，非常适合在各种嵌入式设备上使用。当然如果你对如何实现一个文件服务器感兴趣，darkhttpd 的源码也非常值得学习，整体的源码不到 3K。

以下是官方介绍支持的功能，工具小但功能全：

![image-20210508120040735](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210508120040735.png)

编译安装和使用都非常简单，同时也支持 Docker 方式启动，Docker 镜像不足 100KB，非常小巧。

![image-20210508120144101](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210508120144101.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/emikulic/darkhttpd
