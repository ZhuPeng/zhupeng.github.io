---
layout: post
title: 【视频】少有人知道的 Go 实用工具集介绍
tags: 视频
---

最近又有新视频发布了，后续我们会定期把在 B 站更新的热门推文视频在公众号上做一下同步，但是一般会有滞后一到两周，如果大家想及时观看视频，欢迎关注我们的 B 站同名账号 **GitHub精选**。

######  1、少有人知道的 Go 实用工具集介绍

[少有人知道的 Go 实用工具集介绍](https://www.bilibili.com/video/BV19s421u78M/)

该项目是 `Go` 语言的一套手册，聚焦于为 `Go` 开发者提供寻找常用或者少有人知道的好用的开发工具。其中包括了人工智能工具、测试、依赖关系、代码可视化、性能优化、安全性和一些实用的一行命令，无论是常规工具还是未知小工具，这个项目都可以为开发者提供一个一站式的解决方案。

开源项目地址：https://github.com/nikolaydubina/go-recipes

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247489549&idx=1&sn=9eb7f081a83464bb350ba0d383b59639&chksm=9b3f88d5ac4801c3dae1c6d1eeb3332b5291522941ab8998a8cf6641df2a5c99db3bb9658211#rd

###### 2、开箱即用的 Protocol Buffer 数据验证工具

[开箱即用的 Protocol Buffer 数据验证工具](https://www.bilibili.com/video/BV1fD421u7mc/)

`protovalidate` 是一款基于谷歌 Common Expression Language (CEL) 的 Protobuf 消息验证库。该项目旨在帮助开发者保护网络数据的一致性和完整性，而无需生成额外的代码。与其前身 `protoc-gen-validate` 相比，`protovalidate`在设计上有着更多的优点。它和 `protoc-gen-validate` 的区别和优越性可以在以下博客中找到具体的说明。

开源项目地址：https://github.com/bufbuild/protovalidate

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247490505&idx=1&sn=02062c31c7d639a3fc4a2abeb438a4b3&chksm=9b3f8b11ac480207445c55b8364d42b4f87d685e0948567e5be2514e1571ae1e90e457a0e3c8#rd

###### 3、K8S 镜像拉取速度慢？看这里

[K8S 镜像拉取速度慢？看这里](https://www.bilibili.com/video/BV1tn4y1o7xk/)

Spegel，瑞典语中的“镜子”，作为一个无状态的集群本地 OCI 注册表镜像，解决了以上问题。Spegel 的主要功能是允许 Kubernetes 集群中的每个节点充当本地注册表镜像，这样节点之间就可以共享镜像。任何一个节点已经拉取的图像，其他节点都可以直接拉取。这样既能够减少工作负载启动时间，又减少了出口流量，因为镜像将存储在本地集群中。另外，即使外部镜像服务关闭或故障，新创建的工作负载也能够继续被拉取到，提升了集群的容灾能力。

开源项目地址：https://github.com/XenitAB/spegel

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247489649&idx=1&sn=9a47e93dec86ffb6138395af57832c27&chksm=9b3f88a9ac4801bf9754c8b2ae54fed871fc819813cd5e02ce75a2fd3e63dfc5a3172a2a7602#rd

如果觉得我们的视频还不错的话，欢迎大家一键三连关注我们，我们也会做更多有意思的视频。

粉丝专属 GitHub 必备插件：https://github.com/ZhuPeng/github_linker

公众号快速添加小程序插件：https://github.com/ZhuPeng/mp-transform-public