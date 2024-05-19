---
layout: post
title: 为云原生网络和网络安全插上翅膀
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在云原生时代，容器化和微服务架构的广泛采用使得网络管理和安全成为开发和运维团队面临的巨大挑战。团队需要一个既可以高效管理大规模容器网络，又能提供细粒度网络安全控制的解决方案。而在分布式、多云环境下，这一挑战更是难上加难，核心痛点包括网络性能优化、跨环境互操作性、以及高级网络安全需求等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-56a2b37094fdec485e0d16c39a6806fe.png)

今天要给大家推荐一个 GitHub 开源项目 calico，该项目在 GitHub 有超过 5.5k Star，一句话介绍该项目：Cloud native networking and network security


![](https://www.tigera.io/app/uploads/2024/02/Ecosystem_shrunken_2023.svg)

###### 项目介绍

[Project Calico](https://github.com/projectcalico/calico) 是一个旨在提供一套针对容器、虚拟机和裸机环境的云原生网络和网络安全解决方案。Calico 支持多种数据平面技术，包括 eBPF、标准 Linux、Windows 和 VPP ，具备良好的跨环境互操作性。它为用户提供了优化的性能表现、可扩展的架构，并引入了高级的安全特性，如细粒度访问控制和 WireGuard 加密。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240511232155533.png)

关键特点如下：

**1、数据平面的多样性**：支持多种数据平面技术，满足不同场景需求。

**2、高度互操作**：能够在多种分布式环境中无缝工作。

**3、性能优化**：针对高速网络和低 CPU 使用进行了优化。

**4、可扩展性**：随 Kubernetes 集群的增长而无缝扩展。

**5、先进的网络安全**：提供细粒度的访问控制和加密。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240511232255721.png)

###### 如何使用

用户可以访问 Calico 的[官方文档](https://docs.tigera.io/calico/latest/about)获取安装指南。也可以通过 Helm chart 或直接使用 YAML 文件在 Kubernetes 集群上部署 Calico。例如，安装 Calico 作为 Kubernetes 的网络插件的基本命令如下：

```bash
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.3/manifests/tigera-operator.yaml
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.3/manifests/custom-resources.yaml

# Confirm that all of the pods are running with the following command.
watch kubectl get pods -n calico-system
```
该命令会从 Calico 的官方文档中拉取最新的部署配置文件并应用到你的 Kubernetes 集群中，从而启用 Calico 网络插件。

###### 项目推介

Calico 作为最广泛采用的容器网络和安全解决方案之一，目前已经在全球 166 个国家的 800 万+ 节点上被采用。它拥有一个活跃的开发者和用户社区，超过 300 名贡献者来自全球各大知名公司。除此之外，Calico 提供了丰富的培训资源和文档，以及定期的社区会议，促进用户之间的交流和知识共享。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240511232555469.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectcalico/calico&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectcalico/calico 

开源项目作者：projectcalico

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectcalico/calico)

关注我们，一起探索有意思的开源项目。

