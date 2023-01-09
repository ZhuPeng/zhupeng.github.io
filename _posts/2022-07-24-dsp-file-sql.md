---
layout: post
title: SQL 万能本地文件分析工具
tags: SQL
---

大家好。

SQL 简单好学，应该没有人不懂吧，据我了解不少非技术的工作，也是要具备使用 SQL 的能力。而对于非技术的人来说，平常经常接触到的文件类型是 Excel、JSON、CSV 等，而要做一些复杂的分析，非常依赖使用的软件工具，如果软件不支持，很多的分析是做不了，而且很多时候由于需要打开的文件太大，一些软件工具根本打不开。

今天要推荐一个 SQL 工具 dsq，能够对本地的 Excel、JSON、CSV 等文件进行分析，然后通过 SQL 语法来对数据进行筛选和分析，简直太棒了，这样的话结合其他工具，也能做一些自动化的分析和处理工具。

以下就是一个很简单的使用示例：

![image-20220724222148398](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220724222148398.png)

以上使用真的比在软件上面操作要方便太多了，而且是可以后续重复使用的，对于非技术的人来说，自动化就是如此的简单，能够提高不少工作效率。

除此之外，dsq 还支持不少更为复杂的操作，比如正则、缓存等。

同时目前市面上也有不少类似的工具，项目作者做了非常细致的调研和评估，dsq 目前来看是功能最为全面的，而且性能也非常的极致。

![image-20220724222418225](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220724222418225.png)

![image-20220724222459886](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220724222459886.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/multiprocessio/dsq

开源项目作者：[multiprocessio](https://github.com/multiprocessio)