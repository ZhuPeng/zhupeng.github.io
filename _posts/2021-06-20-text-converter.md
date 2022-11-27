---
layout: post
title: 支持任意文本格式互相转换的在线工具
tags: 前端
---

大家好。

文本格式真的有太多了，如果手头没有合适的工具，有时候需要转换为特定的格式就太麻烦了。

今天要推荐的是一款在线工具 AllDocs，支持非常多的文本格式转换，而且这款工具完全免费，同时保证安全。

![image-20210620221105271](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210620221105271.png)

访问 https://alldocs.app/ 即可使用，使用时选择需要转换和被转换的格式即可跳转到转换页，然后选择对应的文件即可开启转换，非常的简单。

![image-20210620221119245](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210620221119245.png)

![image-20210620221313059](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210620221306738.png)

最重要的是这款工具是开源的，意味着你可以基于这块工具开发定制你自己的在线文本格式转换小工具。

AllDocs 采用的技术栈是 PHP，同时使用了 Laravel、MySQL 和 Pandoc。通过使用 Docker 能够快速的将本地环境搭建起来。

![image-20210620221553647](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210620221553647.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ueberdosis/alldocs.app
