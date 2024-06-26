---
layout: post
title: 无锁高性能缓存库推荐
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在高并发的分布式系统中，如何提高性能、提高响应速度是我们长期面临且头疼的问题。许多开发者和团队采取缓存策略来改善这种状况，那到底什么样的缓存机制才能真正地帮助我们实现这个目标呢？Go 语言中的缓存库大多是基于 map 和互斥锁实现的，这种方式在并发高的场景下容易产生大量的争抢锁情况，而其在 eviction policy 的实现也往往难以与其他语言中优秀的缓存库如 Java 的 Caffeine 相比拼。另外，像 Dgraph labs 的项目 Ristretto 虽然比同等产品快了 30%，但是其命中率却相当不理想。这就使得开发者在选择缓存库的时候陷入了困境，他们渴望有一个简单易用、命中率高且不牺牲性能的缓存库。

今天要给大家推荐一个 GitHub 开源项目 Otter，该项目在 GitHub 有超过 1.1k Star，一句话介绍该项目：A high performance lockless cache for Go. Many times faster than Ristretto and friends.


![](https://raw.githubusercontent.com/maypok86/otter/master/./assets/logo.png)

![](https://raw.githubusercontent.com/maypok86/otter/master/assets/results/reads=100,writes=0.png)

![](https://raw.githubusercontent.com/maypok86/otter/master/assets/results/reads=75,writes=25.png)

![](https://raw.githubusercontent.com/maypok86/otter/master/assets/results/reads=50,writes=50.png)

###### 项目介绍

Otter 是一个用 Go 编写的高性能无锁缓存库，它的速度比 Ristretto 快很多。Otter 的设计理念是实现一个最快最简单易用还有高命中率的缓存库。它基于一系列论文，例如关于尽可能消除锁争用的 BP-Wrapper 框架，以及关于提高内存键值数据库驱逐效率的 Bucket-Based Expiration Algorithm 等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240409235418032.png)

Otter 有以下几个突出特性：简洁的 API、自动配置、支持泛型、过期值自动删除、支持基于成本的驱逐策略以及更高的吞吐率和命中率。

![](https://raw.githubusercontent.com/maypok86/otter/master/assets/results/reads=0,writes=100.png)

###### 如何使用

使用 Go1.19+ 版本，通过以下命令来安装。

```bash
go get -u github.com/maypok86/otter
```

Otter 采用构建器模式，允许您方便地使用不同的参数创建缓存实例。

代码使用示例如下：

```go
package main

import (
    "fmt"
    "time"

    "github.com/maypok86/otter"
)

func main() {
    cache, err := otter.MustBuilder[string, string](10_000).
        CollectStats().
        Cost(func(key string, value string) uint32 {
            return 1
        }).
        WithTTL(time.Hour).
        Build()
    if err != nil {
        panic(err)
    }

    cache.Set("key", "value")
    value, ok := cache.Get("key")
    if !ok {
        panic("not found key")
    }
    fmt.Println(value)
    cache.Delete("key")
    cache.Close()
}
```

###### 项目推介

Otter 是目前性能最好的 Go 缓存库，速度上远比 Ristretto 快，且有突出的优点。

![](https://raw.githubusercontent.com/maypok86/otter/master/assets/results/reads=25,writes=75.png)

比如适应并发高场景，简洁的 API 方便使用，自动配置减少复杂操作步骤，高命中率和吞吐率。尤其是它的新型 S3-FIFO 算法，在命中率上展现非常优秀的效果，让你的程序无缝对接，并实现性能上的提升。所以，如果你正在寻求在高并发环境中更好软件性能，那么 Otter 无疑值得一试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=maypok86/otter&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/maypok86/otter 

开源项目作者：maypok86

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=maypok86/otter)

关注我们，一起探索有意思的开源项目。

