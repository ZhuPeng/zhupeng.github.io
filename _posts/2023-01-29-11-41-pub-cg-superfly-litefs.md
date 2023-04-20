---
layout: post
title: 支撑 SQLite 数据库的跨多机复制的 FUSE 文件系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 superfly/litefs，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“FUSE-based file system for replicating SQLite databases across a cluster of machines”，支撑 SQLite 数据库的跨多机复制的 FUSE 文件系统。

litefs 是一个开源的分布式文件系统。它通过探测数据库的事务的边界，从而按事务级别来记录并复制数据库的变更。litefs 整体架构主要由三部分组成：FUSE 文件系统、Leader 选举、HTTP 服务。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230325215038055.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=superfly/litefs&type=Timeline)

### 如何安装使用

litefs 的安装和使用都比较复杂，建议根据官方文档进行操作，参考如下链接：

https://fly.io/docs/litefs/getting-started/

litefs 目前还是 beta 版本，并不推荐在生产环境内使用。虽然 litefs 目前还有一些问题，但是 litefs 的成功意味着分布式应用的程序开发会更简单，当然 SQLite 本身是一个优秀的工具，在此基础上会变得更好。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/superfly/litefs 

开源项目作者：superfly

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=superfly/litefs)



关注我们，一起探索有意思的开源项目。
