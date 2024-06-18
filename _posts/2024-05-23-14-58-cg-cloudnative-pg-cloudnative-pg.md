---
layout: post
title: 云原生方式管理 PostgreSQL 数据库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

云原生技术和容器化管理平台如 Kubernetes 已成为企业 IT 架构不可或缺的一部分。随着数据库在应用发展中的核心作用日益凸显，将数据库管理系统（DBMS）无缝集成到 Kubernetes 环境中，对于开发和运维团队来说是一个重大的挑战。尤其是如 PostgreSQL 这样广受欢迎的数据库，如何有效地在 Kubernetes 环境中进行部署、管理和维护，同时保证高可用性、扩展性和安全性，是一个亟待解决的关键问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-a8e1046ef6999eaee2ac254abbda34b8.png)

今天要给大家推荐一个 GitHub 开源项目 cloudnative-pg，该项目在 GitHub 有超过 3.6k Star。

![](https://stats.deeptrain.net/repo/cloudnative-pg/cloudnative-pg/?theme=light)

一句话介绍该项目：CloudNativePG is a comprehensive platform designed to seamlessly manage PostgreSQL databases within Kubernetes environments, covering the entire operational lifecycle from initial deployment to ongoing maintenance

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240606225835271.png)

###### 项目介绍

**CloudNativePG** 是一个开源的综合平台，旨在 Kubernetes 环境中无缝管理 PostgreSQL 数据库，涵盖从初始部署到持续维护的整个操作生命周期。该项目由 EDB 最初构建和赞助。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240606225922115.png)

作为解决方案的核心，CloudNativePG 通过扩展 Kubernetes 控制器并以编程方式定义所有良好的数据库管理员(DBA)在管理高可用 PostgreSQL 数据库集群时通常需要执行的操作，从而实现了对 PostgreSQL 集群全生命周期的管理。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240606230039437.png)

它依循 Kubernetes 原生方法，全面拥抱 Operator 模式和最终一致性原则，通过 Kubernetes API 管理复杂的操作，如故障转移、读写分离、缩放、服务端点更新和容器镜像的滚动更新。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240606230406238.png)

###### 如何使用

通过简单的命令即可在 Kubernetes 环境中部署 PostgreSQL 数据库：

```bash
# CloudNativePG Helm install CloudNativePG Operator
helm repo add cloudnative-pg https://cloudnative-pg.github.io/charts/
helm repo update
helm install my-cloudnative-pg cloudnative-pg/cloudnative-pg

# Create one instance for PostgreSQL cluster
kubectl apply -f cluster_with_one_instance.yaml
```

###### 项目推介

自项目启动以来，CloudNativePG 已成为 Kubernetes 环境中部署和管理 PostgreSQL 数据库的优选方案之一。它不仅得到了其发起者 EDB 的大力支持，也在 Adopters 名单中看到了许多知名企业的成功案例，证明了其在生产环境中的可靠性和效率。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20240606230304857.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cloudnative-pg/cloudnative-pg&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cloudnative-pg/cloudnative-pg 

开源项目作者：cloudnative-pg

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cloudnative-pg/cloudnative-pg)

关注我们，一起探索有意思的开源项目。

