---
layout: post
title: GitHub 开源项目 prometheus/client_golang 介绍，Prometheus instrumentation library for Go applications
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 prometheus/client_golang，该项目在 GitHub 有超过 5.3k Star。

![](https://stats.deeptrain.net/repo/prometheus/client_golang/?theme=light)

一句话介绍该项目：Prometheus instrumentation library for Go applications





###### 项目介绍

### 背景介绍

在今天快速演变的软件开发领域，性能监控和指标收集对于保持应用的高效运行至关重要。开发者和运维团队需要实时监控他们的应用和服务，以便快速发现并解决可能影响用户体验的问题。然而，创建一个既强大又灵活的监控系统可能很复杂，特别是需要与现有的技术堆栈无缝集成时。针对这一挑战，许多开发者倾向于使用成熟的开源解决方案来减少开发和维护的负担。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-02e0d3812a6878659ccf1c4fcdb0e15c.png)

项目介绍

[Prometheus](http://prometheus.io) 是一个广受欢迎的开源监控和警报工具集，而 [Prometheus Go 客户端库](https://github.com/prometheus/client_golang)（`client_golang`）是专为 Go 应用提供的指标收集的解决方案。这个库分为两部分：一部分用于应用代码的指标采集，另一部分提供了与 Prometheus HTTP API 交互的客户端。这意味着 Go 开发者可以容易地在他们的应用中实现数据采集，并上传到 Prometheus 服务器进行分析和监控。

该库要求使用 Go1.21 或更高版本，确保了与 Go 最新版本的兼容性。同时，虽然该项目遵循[语义化版本号](https://semver.org/)，但需要注意 API 客户端 (`prometheus/client_golang/api/…`) 目前还处于实验阶段，其破坏性改变不会触发新的主版本释放。

### 如何使用

要开始使用 `client_golang`，您首先需要将它作为依赖项集成到您的 Go 项目中。通过以下 Go 命令，可以轻松做到这一点：

```shell
go get github.com/prometheus/client_golang/prometheus
```

接下来，您可以开始在您的应用中创建和注册指标。以下是一个简单的例子，展示了如何创建一个计数器并在每次请求处理时递增该计数器：

```go
package main

import (
	"net/http"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	requestsCounter := prometheus.NewCounter(
		prometheus.CounterOpts{
			Name: "myapp_requests_total",
			Help: "Total number of processed requests.",
		},
	)
	prometheus.MustRegister(requestsCounter)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		requestsCounter.Inc()
		// 处理请求的业务逻辑
	})
	http.Handle("/metrics", promhttp.Handler())
	http.ListenAndServe(":8080", nil)
}
```

这段代码会在你的应用中创建一个 `/metrics` 路径，该路径通过 Prometheus 标准暴露了应用的指标，可以被 Prometheus 服务采集。

### 项目推介

`client_golang` 不仅得到了广泛的社区支持，而且其稳定性和功能性都经受了众多 Go 项目的考验。凭借其详尽的文档、活跃的开发社区以及对最新 Go 版本的支持，它成为了 Go 应用监控的首选库。不管你是刚接触 Prometheus 还是寻找一个可靠的 Go 集成方案，`client_golang` 都是一个不容错过的选择。

无论是在小型项目还是在大型企业级应用中，`client_golang` 都能帮助开发者和运维团队提高应用性能的可视性，优化监控效率。加入到正在使用这个库的全球

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=prometheus/client_golang&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/prometheus/client_golang 

开源项目作者：prometheus

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=prometheus/client_golang)

关注我们，一起探索有意思的开源项目。

