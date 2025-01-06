---
layout: post
title: GitHub 开源项目 devtron-labs/devtron 介绍，The only Kubernetes dashboard you need
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 devtron-labs/devtron，该项目在 GitHub 有超过 4.6k Star。

![](https://stats.deeptrain.net/repo/devtron-labs/devtron/?theme=light)

一句话介绍该项目：The only Kubernetes dashboard you need




![](https://raw.githubusercontent.com/devtron-labs/devtron/master/./assets/devtron-logo-dark-light.png)

![](https://raw.githubusercontent.com/devtron-labs/devtron/master/./assets/dashboard.png)

![](https://raw.githubusercontent.com/devtron-labs/devtron/master/./assets/devtron-feat-glance.png)

![](https://raw.githubusercontent.com/devtron-labs/devtron/master/./assets/we-support.jpg)


###### 项目介绍

**背景介绍：**

在当今云原生时代，Kubernetes 已经成为容器编排和微服务部署的事实标准。然而，随着应用和服务数量的增加，管理和观测这些分布在各个集群中的服务变得愈发复杂和耗时。团队面临的核心挑战包括应用的部署、配置管理、监测以及安全性控制等。更具挑战的是，每个环境的配置都可能有细微差别，导致了环境之间的配置不一致，增加了管理上的复杂度。同时，为了确保安全性和可靠性，精细化的访问控制和单点登录等功能也变得至关重要。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-2dd341e8da3ee8eb77cbdce03e669ec8.png)

项目介绍：**

[Devtron](https://github.com/devtron-labs/devtron) 是一个扩展性的 Kubernetes Dashboard，旨在为开发和运维团队提供一个集中化的 DevOps 中心。它通过单一且直观的界面，提高了 Helm 应用管理的效率，并提供了对 Kubernetes 集群的清晰可视化。Devtron 内置了 RBAC (基于角色的访问控制) 功能，确保安全访问，同时集成了对通过 GitOps 工具像 ArgoCD 和 FluxCD 部署的工作负载跨多个集群的洞察。它通过加速操作流程，将运维工作效率提升至 20 倍。

项目的主要功能包括但不限于：
- Helm 应用管理，简化 Helm 应用的部署、配置和管理；
- 资源浏览器，可视化并管理集群资源，如节点、Pods、ConfigMaps 和 CRDs 等；
- 单点登录(SSO)，简化团队成员的加入和认证过程；
- 细粒度 RBAC，控制用户对不同仪表板和集群资源的访问级别。

**如何使用：**

首先，创建一个 [Kubernetes 集群](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/)（推荐 K8s 1.16 或更高版本）并安装 [Helm](https://helm.sh/docs/intro/install/)。

安装 Devtron Kubernetes Dashboard：

```bash
helm repo add devtron https://helm.devtron.ai
helm install devtron devtron/devtron-operator \
--create-namespace --namespace devtroncd
```

获取 Devtron Dashboard 的 URL：

```bash
kubectl get svc -n devtroncd devtron-service -o jsonpath='{.status.loadBalancer.ingress}'
```
用户名：`admin`  
管理员密码获取指令：

```bash
kubectl -n devtroncd get secret devtron-secret -o jsonpath='{.data.ADMIN_PASSWORD}' | base64 -d
```

**项目推介：**

Devtron 通过其功能强大且易于使用的接口，得到了广泛的认可和使用。它不仅被多个知名公司采用，还吸引了大批 Kubernetes 和云原生爱好者的关注。项目的开发活跃状态、频繁的更新迭代以及社区的积极参与都保证了 Devtron 持续提供前沿的解决方案。此外，Devtron 的核心团队专业且响应迅速，为用户提供及时的支持与帮助。不论您是初学者还是有经验的 Kubernetes 用户，Devtron 都能助您轻松管理 Kubernetes 集群，加速 DevOps 流程。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=devtron-labs/devtron&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/devtron-labs/devtron 

开源项目作者：devtron-labs

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=devtron-labs/devtron)

关注我们，一起探索有意思的开源项目。

