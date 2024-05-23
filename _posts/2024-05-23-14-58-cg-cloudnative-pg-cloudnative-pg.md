---
layout: post
title: GitHub 开源项目 cloudnative-pg/cloudnative-pg 介绍，CloudNativePG is a comprehensive platform designed to seamlessly manage PostgreSQL databases within Kubernetes environments, covering the entire operational lifecycle from initial deployment to ongoing maintenance
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 cloudnative-pg/cloudnative-pg，该项目在 GitHub 有超过 3.5k Star。

![](https://stats.deeptrain.net/repo/cloudnative-pg/cloudnative-pg/?theme=light)

一句话介绍该项目：CloudNativePG is a comprehensive platform designed to seamlessly manage PostgreSQL databases within Kubernetes environments, covering the entire operational lifecycle from initial deployment to ongoing maintenance





###### 项目介绍

背景介绍：在当今快速发展的技术时代，云原生技术和容器化管理平台如 Kubernetes 已成为企业 IT 架构不可或缺的一部分。随着数据库在应用发展中的核心作用日益凸显，将数据库管理系统（DBMS）无缝集成到 Kubernetes 环境中，对于开发和运维团队来说是一个重大的挑战。尤其是如 PostgreSQL 这样广受欢迎的数据库，如何有效地在 Kubernetes 环境中进行部署、管理和维护，同时保证高可用性、扩展性和安全性，是一个亟待解决的关键问题。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-a8e1046ef6999eaee2ac254abbda34b8.png)

项目介绍：**CloudNativePG** 是一个开源的综合平台，旨在 Kubernetes 环境中无缝管理 PostgreSQL 数据库，涵盖从初始部署到持续维护的整个操作生命周期。该项目由 [EDB](https://www.enterprisedb.com) 最初构建和赞助。作为解决方案的核心，CloudNativePG 通过扩展 Kubernetes 控制器并以编程方式定义所有良好的数据库管理员(DBA)在管理高可用 PostgreSQL 数据库集群时通常需要执行的操作，从而实现了对 PostgreSQL 集群全生命周期的管理。它依循 Kubernetes 原生方法，全面拥抱操作符模式和最终一致性原则，通过 Kubernetes API 管理复杂的操作，如故障转移、读写分离、缩放、服务端点更新和容器镜像的滚动更新。

如何使用：要开始使用 CloudNativePG，可以从其 [快速开始](https://cloudnative-pg.io/docs/src/quickstart.html) 文档部分入手。通过简单的命令即可在 Kubernetes 环境中部署 PostgreSQL 数据库：

```bash
# 通过 CloudNativePG Helm 图表安装 CloudNativePG 操作员
helm repo add cloudnative-pg https://cloudnative-pg.github.io/charts/
helm repo update
helm install my-cloudnative-pg cloudnative-pg/cloudnative-pg

# 创建包含一个实例的 PostgreSQL 集群
kubectl apply -f cluster_with_one_instance.yaml
```

项目推介：自项目启动以来，CloudNativePG 已成为 Kubernetes 环境中部署和管理 PostgreSQL 数据库的优选方案之一。它不仅得到了其发起者 EDB 的大力支持，也在 [Adopters](https://github.com/cloudnative-pg/cloudnative-pg/blob/main/ADOPTERS.md) 名单中看到了许多知名企业的成功案例，证明了其在生产环境中的可靠性和效率。CloudNativePG 的开发活跃且持续迭代，社区支持充分，拥有完善的文档和丰富的交流渠道，如 Slack 频道和 GitHub 讨论。它的 Kubernetes 原生设计理念、高可用性管理和易用性操作使得 CloudNativePG 成为在 Kubernetes 环境中管理 PostgreSQL 数据库的理想选择。

无论是正在寻找 Kubernetes 环境中 PostgreSQL 数据库管理解决方案的企业，还是对云原生数据库技术感兴趣的技术人员，CloudNativePG 都值得关注和尝试。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cloudnative-pg/cloudnative-pg&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cloudnative-pg/cloudnative-pg 

开源项目作者：cloudnative-pg

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cloudnative-pg/cloudnative-pg)

关注我们，一起探索有意思的开源项目。

