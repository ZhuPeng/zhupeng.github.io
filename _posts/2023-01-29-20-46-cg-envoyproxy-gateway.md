---
layout: post
title: GitHub 开源项目 envoyproxy/gateway 介绍，Manages Envoy Proxy as a standalone or Kubernetes-based application gateway
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 envoyproxy/gateway，该项目在 GitHub 有超过 0.8k Star，用一句话介绍该项目就是：“Manages Envoy Proxy as a standalone or Kubernetes-based application gateway”。


envoyproxy/gateway 是 Envoy 开源项目中的一部分，是一个高性能的代理服务器。它提供了一种可扩展的机制来管理网络流量，支持负载均衡、路由、服务发现等功能。

该项目提供了一个可扩展的配置模型，可以方便地将不同的组件组合在一起，实现各种类型的代理。

Envoy 的特点是高性能和灵活性，适用于微服务架构中的服务网格，可以与各种服务发现组件（如 Consul，Etcd 等）集成。

该项目是一个开源项目，并且拥有丰富的文档和社区支持，可以帮助用户快速上手和使用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=envoyproxy/gateway&type=Timeline)

### 如何安装使用

Envoy 是一个可执行程序，可以在各种平台上运行，包括 Linux，MacOS 和 Windows。安装 Envoy 的方法如下：

1. 从 GitHub 上下载 Envoy 的可执行文件。
2. 将下载的可执行文件移动到系统的 PATH 目录中。
3. 创建一个配置文件，用于配置 Envoy 的运行参数。
4. 在命令行中运行 Envoy，并使用配置文件启动它。

具体安装方法请参考官网 https://www.envoyproxy.io/docs/envoy/latest/start/start

需要注意的是, Envoy 依赖于 C++ 编译环境，如果您的系统中没有安装 C++ 编译环境，需要先安装。


### 使用示例 DEMO

这是一个 Envoy 的简单配置示例，用于将请求转发到后端服务器：

```
admin:
  access_log_path: /tmp/admin_access.log
  address:
    socket_address: { address: 0.0.0.0, port_value: 9901 }

static_resources:
  listeners:
  - name: listener_0
    address:
      socket_address: { address: 0.0.0.0, port_value: 10000 }
    filter_chains:
    - filters:
      - name: envoy.http_connection_manager
        config:
          codec_type: AUTO
          stat_prefix: ingress_http
          route_config:
            name: local_route
            virtual_hosts:
            - name: local_service
              domains: ["*"]
              routes:
              - match: { prefix: "/" }
                route:
                  cluster: service_cluster
          http_filters:
          - name: envoy.router
  clusters:
  - name: service_cluster
    connect_timeout: 0.25s
    type: STATIC
    lb_policy: ROUND_ROBIN
    hosts: [{ socket_address: { address: servicehost, port_value: 80 }}]
```

这个配置文件定义了一个监听器，监听在 0.0.0.0:10000 上的请求。所有请求都会被转发到后端服务器 servicehost:80。

将以上配置保存为一个文件，例如 envoy.yaml。然后，您可以使用以下命令来启动 Envoy：

```
envoy -c envoy.yaml
```

这样就可以在本地起一个服务了

需要注意的是, 此示例仅供参考，实际配置可能会有所不同。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/envoyproxy/gateway 

开源项目作者：envoyproxy

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=envoyproxy/gateway)

