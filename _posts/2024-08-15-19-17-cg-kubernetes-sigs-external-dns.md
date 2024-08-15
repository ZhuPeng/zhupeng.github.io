---
layout: post
title: GitHub 开源项目 kubernetes-sigs/external-dns 介绍，Configure external DNS servers (AWS Route53, Google CloudDNS and others) for Kubernetes Ingresses and Services
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 kubernetes-sigs/external-dns，该项目在 GitHub 有超过 7.5k Star。

![](https://stats.deeptrain.net/repo/kubernetes-sigs/external-dns/?theme=light)

一句话介绍该项目：Configure external DNS servers (AWS Route53, Google CloudDNS and others) for Kubernetes Ingresses and Services




![](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/docs/img/external-dns.png)


###### 项目介绍

### 背景介绍
随着 Kubernetes 成为容器编排的事实标准，一项日益紧迫的需求是如何将集群内部的资源（如 Services 和 Ingresses）自动映射至外部 DNS 记录，以实现服务发现。此需求包括，但不限于：动态更新域名记录以反映服务的 IP 地址变化、跨多个 DNS 提供商管理记录、以及容纳来自不同云平台的服务。手动管理这些 DNS 记录不仅耗时耗力，而且容易出错。因此，需要一个能够自动完成这些任务的解决方案，以减少管理开销并提高准确性。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-39cfa4cf57229cf4259541c7a98b06cc.png)

项目介绍
`ExternalDNS` 是一个 Open Source 项目，其主要目标是使 Kubernetes 资源（如 Services 和 Ingresses）可以通过公共 DNS 服务器进行发现。`ExternalDNS` 通过从 Kubernetes API 抓取资源列表来确定所需的 DNS 记录列表。与 Kubernetes 自身的 DNS 服务（KubeDNS）不同，`ExternalDNS` 不是一个 DNS 服务器，而是将 DNS 记录的配置任务委托给了其他的 DNS 提供商，如 AWS Route 53、Google Cloud DNS 等。此项目对 Kubernetes 生态系统和跨云平台服务的集成提供了极大的便利和灵活性，是一个 DNS 提供商无关的解决方案。

`ExternalDNS` 支持多个 DNS 提供商，包括但不限于 Google Cloud DNS、AWS Route 53、AzureDNS 等。此外，它允许用户通过 `--domain-filter` 参数筛选特定的域名区域，以同步 Ingresses 和 Services 的 `type=LoadBalancer` 以及不同 DNS 提供商中的节点。

### 如何使用
要部署和使用 `ExternalDNS`，需要在 Kubernetes 集群中进行安装。首先，确保您有一个 Kubernetes 集群，并且已经安装和配置了 kubectl。然后，您可以按照以下步骤进行：

1. 克隆 `ExternalDNS` 项目的 GitHub 仓库到本地。
2. 根据您的 DNS 提供商情况，配置 `ExternalDNS` 的运行参数。例如，如果您使用 AWS Route 53，可能需要设置相应的 AWS 访问密钥和域名过滤参数。
3. 使用 kubectl 应用配置到您的集群中。

```shell
kubectl apply -f {配置文件路径}
```

请参考官方文档和示例配置以了解更多详情，包括不同 DNS 提供商的具体配置方式。

### 项目推介
`ExternalDNS` 是由 Kubernetes SIGs 维护的一个活跃项目，具有广泛的社区支持和持续的开发活动。自从其发布以来，它已被众多知名公司和组织采用，包括但不限于 AWS、Google Cloud 等。凭借其高度的灵活性和广泛的 DNS 提供商支持，无论是小规模项目还是大型企业级部署，`ExternalDNS` 都能提供强大的 DNS 管理能力。

此项目的一个显著特点是其对新 DNS 提供商的支持方式。通过引入 webhook 系统，社区可以轻松添加新的 DNS 提供商，不断扩展 `ExternalDNS` 的能力。此外，各大云服务商和 DNS 提供商的积极参与确保了 `ExternalDNS` 在不同环境下的良好兼容性和稳定性。

综上所述，无论您是 Kubernetes 的新手还是经验丰富的专业人士，`ExternalDNS` 都是管理外部 DNS 记录的强大工具，值得在您的 Kubernetes 项目中采用。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubernetes-sigs/external-dns&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes-sigs/external-dns 

开源项目作者：kubernetes-sigs

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubernetes-sigs/external-dns)

关注我们，一起探索有意思的开源项目。

