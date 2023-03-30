---
layout: post
title: 支持基于真实负载的 Kubernetes 调度器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 gocrane/crane-scheduler，该项目在 GitHub 有超过 100 Star，用一句话介绍该项目就是：“Crane scheduler is a Kubernetes scheduler which can schedule pod based on actual node load.”，支持基于真实负载的 Kubernetes 调度器。

crane-scheduler 是基于 Go 语言的调度器库。它主要用于企业级的分布式调度，可以帮助开发者实现任务调度、任务分配、负载均衡等功能。该项目支持多种调度策略，可以在不同的场景中进行优化。

Crane-scheduler 基于 Node-annotator 收集的 Prometheus 资源负载数据，对 Pod 进行负载均衡的调度。以下是架构图：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20230319183827884.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=gocrane/crane-scheduler&type=Timeline)

### 如何安装使用

crane-scheduler 项目可以通过如下方式安装使用。

1、确保 Kubernetes 集群安装了 Prometheus

2、配置 Prometheus 规则

主要是以下数据指标的收集：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230319184331636.png)

实际的 YAML 配置如下：

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
    name: example-record
    labels:
        prometheus: k8s
        role: alert-rules
spec:
    groups:
    - name: cpu_mem_usage_active
      interval: 30s
      rules:
      - record: cpu_usage_active
        expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[30s])) * 100)
      - record: mem_usage_active
        expr: 100*(1-node_memory_MemAvailable_bytes/node_memory_MemTotal_bytes)
    - name: cpu-usage-5m
      interval: 5m
      rules:
      - record: cpu_usage_max_avg_1h
        expr: max_over_time(cpu_usage_avg_5m[1h])
      - record: cpu_usage_max_avg_1d
        expr: max_over_time(cpu_usage_avg_5m[1d])
    - name: cpu-usage-1m
      interval: 1m
      rules:
      - record: cpu_usage_avg_5m
        expr: avg_over_time(cpu_usage_active[5m])
    - name: mem-usage-5m
      interval: 5m
      rules:
      - record: mem_usage_max_avg_1h
        expr: max_over_time(mem_usage_avg_5m[1h])
      - record: mem_usage_max_avg_1d
        expr: max_over_time(mem_usage_avg_5m[1d])
    - name: mem-usage-1m
      interval: 1m
      rules:
      - record: mem_usage_avg_5m
        expr: avg_over_time(mem_usage_active[5m])
```

3、安装 crane-scheduler

```bash
helm repo add crane https://gocrane.github.io/helm-charts
helm install scheduler -n crane-system --create-namespace --set global.prometheusAddr="REPLACE_ME_WITH_PROMETHEUS_ADDR" crane/scheduler
```

同时需要配置 Kubernetes 策略，将 crane-scheduler 作为第二调度器，具体配置方式可以参考 GitHub 上的 README。

4、对 Pod 做真实的调度测试

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_pod-scheduler.png)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/gocrane/crane-scheduler 

开源项目作者：gocrane

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=gocrane/crane-scheduler)

