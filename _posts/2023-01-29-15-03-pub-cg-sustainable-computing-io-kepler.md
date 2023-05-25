---
layout: post
title: 使用 eBPF 实现的自动 CPU 能耗监控的系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 sustainable-computing-io/kepler，该项目在 GitHub 有超过 300 Star，用一句话介绍该项目就是：“Kepler (Kubernetes-based Efficient Power Level Exporter) uses eBPF to probe energy related system stats and exports as Prometheus metrics”，使用 eBPF 实现的自动 CPU 能耗监控的系统。

之前也有介绍 eBPF 是什么，这里再介绍一次。

> eBPF 是一项革命性的技术，可以在 Linux 内核中运行沙盒程序，而无需更改内核源代码或加载内核模块。通过使 Linux 内核可编程，基础架构软件可以利用现有的层，从而使它们更加智能和功能丰富，而无需继续为系统增加额外的复杂性层。
>
> eBPF 导致了网络，安全性，应用程序配置/跟踪和性能故障排除等领域的新一代工具的开发，这些工具不再依赖现有的内核功能，而是在不影响执行效率或安全性的情况下主动重新编程运行时行为。 

得益于 eBPF 技术，我们可以不改动应用代码，并监控应用相关的热点流量数据，并自动生成相应的 metrics 并暴露给 Prometheus 进行采集，从而做到了自动化监控应用的目标，无需前置的事件打点。

以下是 kepler 的系统架构图。

![](https://raw.githubusercontent.com/sustainable-computing-io/kepler/master/doc/kepler-arch.png)

对应生成的监控图表，相应的会计算各个 Pod、Node 等的能耗数据。

![](https://raw.githubusercontent.com/sustainable-computing-io/kepler/master/doc/dashboard.png)


以下是该项目 Sta	r 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sustainable-computing-io/kepler&type=Timeline)

### 如何安装使用

使用 Kepler 前需要满足以下要求：Kernel 4.18+、可访问的 Kubernetes 集群、kubectl v1.21.0+。然后可以使用 Helm Chart 进行安装使用，以下是对于的命令：

```bash
cd kepler-helm-chart
helm install kepler . --values values.yaml  --create-namespace  --namespace <namespace>
```

同时也是可以进行源码的安装的。

```bash
make build-manifest OPTS="<deployment options>"
# minimum deployment: 
# > make build-manifest
# deployment with sidecar on openshift: 
# > make build-manifest OPTS="ESTIMATOR_SIDECAR_DEPLOY OPENSHIFT_DEPLOY"


kubectl apply -f _output/generated-manifest/deployment.yaml
```

安装好后还需要根据官方文档进行相应的配置，详情参考：https://sustainable-computing.io/installation/kepler/


更多项目详情请查看如下链接。

开源项目地址：https://github.com/sustainable-computing-io/kepler 

开源项目作者：sustainable-computing-io

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sustainable-computing-io/kepler)



关注我们，一起探索有意思的开源项目。
