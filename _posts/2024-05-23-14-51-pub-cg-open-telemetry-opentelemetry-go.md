---
layout: post
title: 构建高性能可观测应用的利器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代软件开发生命周期中，可观测性（Observability）成为确保应用健康、高性能的一个关键因素。它帮助开发者理解软件在生产环境中的表现，以及系统之间是如何交互的。随着微服务架构的流行，系统之间的交互变得更加复杂，传统的日志、监控等手段已不能全面覆盖可观测性需求，这就需要更先进的工具来捕获、分析和管理数据。然而，构建这样一个流程往往需要大量的工作，并且要求开发者有相对深厚的专业知识。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-ecbc2819fc8cafa43322053ecf6e9421.png)

今天要给大家推荐一个 GitHub 开源项目 opentelemetry-go，该项目在 GitHub 有超过 4.9k Star。

![](https://stats.deeptrain.net/repo/open-telemetry/opentelemetry-go/?theme=light)

一句话介绍该项目：OpenTelemetry Go API and SDK

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601231121789.png)


###### 项目介绍

**OpenTelemetry-Go** 是 [OpenTelemetry](https://opentelemetry.io/) 的 [Go](https://golang.org/) 实现版本，旨在提供一套简单而强大的 API 以直接测量你的软件性能和行为，并将这些数据发送到可观测性平台。现阶段， **OpenTelemetry-Go** 对 **Traces（追踪）** 和 **Metrics（度量）** 提供稳定支持，对 **Logs（日志）** 提供 Beta 阶段的支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601231227170.png)

该项目兼顾了简单性与可扩展性，即使是没有深厚技术背景的开发者也能轻松上手，并快速集成到现有的 Go 应用中。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601231209064.png)

###### 如何使用

首先需要安装 Go SDK。可以通过访问 [opentelemetry.io 文档](https://opentelemetry.io/docs/languages/go/getting-started/)来获取开始指南。以下是对如何安装和简单使用的总结：

1、添加 **OpenTelemetry-Go** 依赖到你的 Go 项目中。

2、选择和配置合适的 Exporter（导出器），以将数据发送到你选择的观测平台。

3、通过官方或第三方 instrumentation 库，或直接使用 API 来对你的应用进行插桩。

代码示例如下：

```go
package main

import (
    "context"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/resource"
    semconv "go.opentelemetry.io/otel/semconv/v1.7.0"
    "go.opentelemetry.io/otel/sdk/trace"
)

func main() {
    ctx := context.Background()

    exporter, err := otlptrace.New(ctx, otlptracegrpc.NewClient())
    if err != nil { // handle error
    }

    // Create Tracer provider
    tp := trace.NewTracerProvider(
        trace.WithBatcher(exporter),
        trace.WithResource(resource.NewSchemaless(semconv.ServiceNameKey.String("your-service-name"))),
    )
    otel.SetTracerProvider(tp)

    // Start by your app code
}
```

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=open-telemetry/opentelemetry-go&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/open-telemetry/opentelemetry-go 

开源项目作者：open-telemetry

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=open-telemetry/opentelemetry-go)

关注我们，一起探索有意思的开源项目。

