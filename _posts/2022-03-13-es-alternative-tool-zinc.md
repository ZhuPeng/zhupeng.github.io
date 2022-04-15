---
layout: post
title: 轻量级 Elasticsearch 替代开源搜索引擎
tags: 搜索
---

大家好。

Elasticsearch 真的好用，但是 Elasticsearch 安装和配置也是真的繁琐，后续的一些维护也有一定成本。另外一个 Elasticsearch 的不足就是服务运行起来需要的计算资源较多，对于普通的用户来说是有点浪费的。

今天要推荐的开源工具 Zinc，是一个轻量级的 Elasticsearch 替代工具，拥有完全兼容 Elasticsearch 的 APIs，同时自带 UI 用来替代 Elasticsearch 系列的 Kibana。

Zinc 使用 Go 开发，只需要一个二进制包就能直接启动使用，在安装和使用都比 Elasticsearch 要简单很多，同时资源的消耗也比 Elasticsearch 低得多。以下是官方介绍视频：

https://www.youtube.com/watch?v=aZXtuVjt1ow

Zinc 功能上现在基本上是开箱即用了。

![image-20220313201744825](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220313201744825.png)

未来 Zinc 会在高可用、高性能上做相应的增强。

![image-20220313201818410](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220313201818410.png)

以下是一些具体的使用 DEMO，自带 UI 不用单独安装类似 Kibana 的应用是一大便利。

搜索界面：

![](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_search_screen.jpeg)

![](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_zinc_search_screen_paris.jpeg)

用户管理界面：

![](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_zinc_users_screen.jpeg)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/prabhatsharma/zinc
