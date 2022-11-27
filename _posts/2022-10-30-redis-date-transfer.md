---
layout: post
title: 阿里巴巴开源力作，Redis 数据迁移工具
tags: 数据库
---

大家好。

今天要推荐一个阿里巴巴开源工具 redis-shake，一个 Redis 的数据迁移和清洗工具，工具使用起来比较简单，也经历过大厂的认证，正确性和稳定性都有保障。

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_redis.alibaba.png)
redis-shake 常见于生产环境中将 Redis 单机实例迁移到集群实例或者需要无缝将一个小规格 Redis 实例迁移到另一个大规格 Redis 实例。

redis-shake 支持迁移单实例、集群等，也支持将数据备份或者迁移到阿里云。经过迭代，目前  redis-shake 有两个版本。

![image-20221030160643574](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20221030160643574.png)

从 GitHub 下载二进制或者自己从代码编译都行，redis-shake 使用 Go 语言开发，整体代码也比较简单易懂，感兴趣的小伙伴也可以自行查阅。除此之外，如果要使用数据过滤的功能，可以使用 Lua 语言进行自定义，保证了工具的灵活性。

![image-20221030162119996](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20221030162119996.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/alibaba/RedisShake

开源项目作者：https://github.com/alibaba