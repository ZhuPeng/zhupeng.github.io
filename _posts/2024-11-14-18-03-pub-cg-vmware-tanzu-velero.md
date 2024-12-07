---
layout: post
title: 备份和迁移 Kubernetes 应用及存储的利器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今云计算和微服务架构迅猛发展的背景下，Kubernetes 已成为容器编排领域的事实标准。随着越来越多的企业将他们的应用部署在 Kubernetes 集群上，这带来了一系列新的挑战：如何有效备份和恢复 Kubernetes 集群资源？如何在不同的集群间迁移应用和数据？当灾难发生时，如何最小化数据丢失和服务中断的风险？这些问题成为了许多 IT 管理员和开发者亟需解决的核心痛点。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f24b2f3179e204a9165002e65c6bd0e2.png)

今天要给大家推荐一个 GitHub 开源项目 velero，该项目在 GitHub 有超过 8.8k Star。

![](https://stats.deeptrain.net/repo/vmware-tanzu/velero/?theme=light)

一句话介绍该项目：Backup and migrate Kubernetes applications and their persistent volumes

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221037115.png)

###### 项目介绍

Velero（前身为 Heptio Ark）提供了一套工具来备份和恢复 Kubernetes 集群资源及其持久卷。不论是公有云平台还是本地部署，你都可以运行 Velero。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221131806.png)

通过 Velero，用户可以：

1、对集群进行备份，以防数据丢失时进行恢复。

2、迁移集群资源到其他集群。

3、将生产集群复制到开发和测试集群，帮助提升应用质量和开发效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221201455.png)

###### 如何使用

首先需要在 Kubernetes 集群上安装 Velero 服务器。然后，通过命令行客户端来管理备份和恢复操作。以下是一些基本的安装和使用示例：

1、安装 Velero：具体安装步骤因平台而异，可以参考 [Velero Document](https://velero.io/docs/) 获取详细指引。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221308137.png)

2、创建备份：使用命令 `velero backup create <backup-name>` 创建一个集群的备份。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221511941.png)

3、恢复备份：使用命令 `velero restore create --from-backup <backup-name>` 从备份中恢复集群。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221435526.png)

###### 项目推介

Velero 不仅支持广泛的 Kubernetes 版本，还能够在 IPv4、IPv6 和双栈环境中运行，体现了其强大的通用性和兼容性。项目由 VMware Tanzu 维护，确保了其专业性和可靠性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241117221551612.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=vmware-tanzu/velero&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/vmware-tanzu/velero 

开源项目作者：vmware-tanzu

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=vmware-tanzu/velero)

关注我们，一起探索有意思的开源项目。

