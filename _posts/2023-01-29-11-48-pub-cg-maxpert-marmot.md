---
layout: post
title: 基于 NATS 消息系统的分布式 SQLite 引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 maxpert/marmot，该项目在 GitHub 有超过 700k Star，用一句话介绍该项目就是：“A distributed SQLite replicator built on top of NATS”，一个基于 NATS 消息系统的分布式 SQLite 复制引擎。

![](https://user-images.githubusercontent.com/22441/196061378-21f885b3-7958-4a7e-994b-09d4e86df721.png)

marmot 是一个分布式的 SQLite 的复制引擎，它的设计上是无主节点的，同时是保证最终的一致性。当你的网站是基于 SQLite 构建的，同时又面临很严重的读压力时，你可以依赖 marmot 很轻松的在多个节点间复制 SQLite 数据库，从而确保网站的可扩展性，同时又保留了使用 SQLite 的便利性。

虽然目前开源上有多个 SQLite 分布式的解决方案，比如 rqlite、dqlite、LiteFS 等。但是 marmot 相比其他解决方案有如下的不同及优势。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230401224223321.png)

总结一下就是 marmot 的无主设计确保了用户使用上的便利性，不用关心节点是否只读或者只写，任何节点都可以直接的读写，而 marmot 不是通过强一致性而是最终一致性来保证以上特性的可行性。当然也会给 marmot 带来一些限制，以下是具体的限制条件：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230401224615463.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=maxpert/marmot&type=Timeline)

### 如何安装使用

使用如下命令即可在仓库中构建 marmot：

```bash
go build -o build/marmot ./marmot.go
```

构建完成后，可以在本机即可进行对应特性的测试，比如：

```bash
nats-server --jetstream
build/marmot -config config-1.toml -verbose
build/marmot -config config-2.toml -verbose
```

其中需要确保 config-1.toml 和 config-2.toml 中配置的  SQLite DB 有相同的数据表的 schemas。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/maxpert/marmot 

开源项目作者：maxpert

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=maxpert/marmot)



关注我们，一起探索有意思的开源项目。
