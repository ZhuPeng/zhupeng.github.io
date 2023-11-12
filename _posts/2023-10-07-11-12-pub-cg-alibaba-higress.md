---
layout: post
title: Higress - 阿里巴巴基于内部两年多实践沉淀的下一代云原生网关
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在云原生架构的背景下，我们需要一个能够满足微服务、安全防护以及流量管理等多重需求的网关，同时，我们还希望这个网关能够轻松地与现有的系统进行集成，而不是需要我们进行大规模的改造。

今天要给大家推荐一个 GitHub 开源项目 alibaba/higress，该项目在 GitHub 有超过 1.8k Star，用一句话介绍该项目就是：“Next-generation Cloud Native Gateway | 下一代云原生网关”。

![](https://img.alicdn.com/imgextra/i2/O1CN01NwxLDd20nxfGBjxmZ_!!6000000006895-2-tps-960-290.png)

###### 项目介绍

Higress 是阿里巴巴基于内部两年多的 Envoy Gateway 实践沉淀，以开源 Istio 与 Envoy 为核心构建的下一代云原生网关。Higress 实现了安全防护网关、流量网关、微服务网关三层网关合一，可以显著降低网关的部署和运维成本。Higress 除了具备传统网关的功能外，还提供了丰富的可观测性、插件扩展机制、多种服务发现方式以及丰富的路由能力等特性。

以下是项目的架构图：

![](https://img.alicdn.com/imgextra/i1/O1CN01iO9ph825juHbOIg75_!!6000000007563-2-tps-2483-2024.png)

以下是 Higress 的功能演示：

1、**丰富的可观测**

提供开箱即用的可观测，Grafana&Prometheus 可以使用内置的也可对接自建的

![](https://raw.githubusercontent.com/alibaba/higress/master/./docs/images/monitor.gif)

2、**插件扩展机制**

官方提供了多种插件，用户也可以[开发](https://github.com/alibaba/higress/blob/main/plugins/wasm-go)自己的插件，构建成 docker/oci 镜像后在控制台配置，可以实时变更插件逻辑，对流量完全无损。

![](https://raw.githubusercontent.com/alibaba/higress/master/./docs/images/plugin.gif)

3、**多种服务发现**

默认提供 K8s Service 服务发现，通过配置可以对接 Nacos/ZooKeeper 等注册中心实现服务发现，也可以基于静态 IP 或者 DNS 来发现

![](https://raw.githubusercontent.com/alibaba/higress/master/./docs/images/service-source.gif)

4、**域名和证书**

可以创建管理 TLS 证书，并配置域名的 HTTP/HTTPS 行为，域名策略里支持对特定域名生效插件

![](https://raw.githubusercontent.com/alibaba/higress/master/./docs/images/domain.gif)

5、**丰富的路由能力**

通过上面定义的服务发现机制，发现的服务会出现在服务列表中；创建路由时，选择域名，定义路由匹配机制，再选择目标服务进行路由；路由策略里支持对特定路由生效插件

![](https://raw.githubusercontent.com/alibaba/higress/master/./docs/images/route-service.gif)

###### 如何使用

Higress 的使用非常简单，只需要按照项目的 Quick Start 指南进行操作即可。

1、**Helm 安装命令**

```bash
helm repo add higress.io https://higress.io/helm-charts
helm install higress -n higress-system higress.io/higress --create-namespace --render-subchart-notes --set higress-console.domain=console.higress.io
```

2、在本地 K8s环境中使用，使用 kind

```bash
##### Mac #####
# for Intel Macs
[ $(uname -m) = x86_64 ] && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.18.0/kind-darwin-amd64
# for Apple Silicon Macs (M1/M2), but higress image does not support ARM yet.
# [ $(uname -m) = arm64 ] && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
# [ $(uname -m) = arm64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.18.0/kind-darwin-arm64
chmod +x ./kubectl ./kind
sudo mv ./kubectl ./kind /usr/local/bin

##### Linux #####
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.18.0/kind-linux-amd64
chmod +x ./kubectl ./kind
sudo mv ./kubectl ./kind /usr/local/bin
```

具体的使用场景包括 Kubernetes Ingress 网关、微服务网关以及安全防护网关。例如，Higress 可以作为 K8s 集群的 Ingress 入口网关，也可以作为微服务网关，能够对接多种类型的注册中心发现服务配置路由，例如 Nacos, ZooKeeper, Consul, Eureka 等。

###### 项目推介

Higress 是阿里巴巴内部经过两年多生产验证的产品，支持每秒请求量达数十万级的大规模场景，具有很高的稳定性和可靠性。同时，Higress 的开发活跃，社区活跃，有很多知名的公司和开发者在使用。如果你正在寻找一个功能强大、易用、稳定可靠的云原生网关，那么 Higress 就是你的最佳选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=alibaba/higress&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/alibaba/higress 

开源项目作者：alibaba

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=alibaba/higress)

关注我们，一起探索有意思的开源项目。

