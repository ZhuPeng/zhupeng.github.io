---
layout: post
title: GitHub 开源项目 twmb/franz-go 介绍，franz-go contains a feature complete, pure Go library for interacting with Kafka from 0.8.0 through 3.8+. Producing, consuming, transacting, administrating, etc.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 twmb/franz-go，该项目在 GitHub 有超过 1.9k Star。

![](https://stats.deeptrain.net/repo/twmb/franz-go/?theme=light)

一句话介绍该项目：franz-go contains a feature complete, pure Go library for interacting with Kafka from 0.8.0 through 3.8+. Producing, consuming, transacting, administrating, etc.





###### 项目介绍

### 背景介绍

在现代软件开发和数据处理中，消息队列技术是不可或缺的一部分，特别是在处理大规模数据流处理和异步通信时。Apache Kafka，作为一个分布式流处理平台，广泛用于构建实时数据管道和流应用程序。它具有高吞吐量、可扩展、容错等特点，成为了许多公司技术栈中的重要组成部分。然而，与 Kafka 交互通常需要用到客户端库，而这些库在不同编程语言中的实现和支持程度各异。对于使用 Go 语言的开发者来说，一个高效、功能全面同时又易于使用的 Kafka 客户端库是他们迫切需要的解决方案。franz-go 就是为解决这一需求而生的项目。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-6dab25d4d68057b4707c9f78d768f8fb.png)

项目介绍

**franz-go** 是一个完整的 Apache Kafka 客户端，使用纯 Go 语言编写。它支持从 Apache Kafka v0.8.0 版本开始的 **每一个 Kafka 功能**，包括但不限于事务处理、正则表达式主题消费、最新的分区策略、数据丢失检测、最近副本获取等。对于存在的客户端 Kafka 改进提案（KIP），franz-go 都尝试提供支持。

此库尝试在与 Kafka 交互时提供直观的 API 设计，并高效实现 Kafka 期望的行为（如处理超时等）。功能特性包括完整的客户端支持（Kafka >= 0.8.0 通过 v3.8+）、全方位 Exactly-Once-Semantics（EOS）、幂等性和事务性生产者、简单（传统）消费者、带有各种负载均衡策略的组消费者、所有压缩类型支持、SSL/TLS、所有 SASL 认证机制支持、低级别管理功能以及高级别管理包等。

### 如何使用

安装 franz-go 可以直接使用 Go 的包管理工具：

```
go get github.com/twmb/franz-go
```

简单的生产和消费消息示例：

```go
seeds := []string{"localhost:9092"}
cl, err := kgo.NewClient(
	kgo.SeedBrokers(seeds...),
	kgo.ConsumerGroup("my-group-identifier"),
	kgo.ConsumeTopics("foo"),
)
if err != nil {
	panic(err)
}
defer cl.Close()

ctx := context.Background()

// 生产消息
var wg sync.WaitGroup
wg.Add(1)
record := &kgo.Record{Topic: "foo", Value: []byte("bar")}
cl.Produce(ctx, record, func(_ *kgo.Record, err error) {
	defer wg.Done()
	if err != nil {
		fmt.Printf("record had a produce error: %v\n", err)
	}
})
wg.Wait()

// 消费消息
for {
	fetches := cl.PollFetches(ctx)
	// 错误处理省略...
	iter := fetches.RecordIter()
	for !iter.Done() {
		record := iter.Next()
		fmt.Println(string(record.Value), "from an iterator!")
	}
}
```

### 项目推介

franz-go 是一个活跃开发且广受好评的项目。它不仅提供高性能的 Kafka 客户端实现，还具有几乎全面的 Kafka 特性支持。此外，franz-go 还考虑现代 Go 语言的开发习惯，提供了符合习惯的 API 和 idiomatic Go code。它已被多家知名公司采用于生产环境，诸如 Redpanda、Confluent Platform 以及 Amazon MSK 等 Kafka 兼容的代理商，均可以无缝集成使用 franz-go。对于寻找高效、可靠 Kafka 客户端库的 Go 开发者来说，franz-go 是一个不可多得的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=twmb/franz-go&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/twmb/franz-go 

开源项目作者：twmb

开源协议：BSD 3-Clause "New" or "Revised" License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=twmb/franz-go)

关注我们，一起探索有意思的开源项目。

