---
layout: post
title: 【视频】Go 超快安全轻量级的 Actor 引擎
tags: 视频
---

最近又有新视频发布了，后续我们会定期把在 B 站更新的热门推文视频在公众号上做一下同步，但是一般会有滞后一到两周，如果大家想及时观看视频，欢迎关注我们的 B 站同名账号 **GitHub精选**。

######  1、轻量级、低开销且功能强大的虚拟 K8S 集群解决方案

[轻量级、低开销且功能强大的虚拟 K8S 集群解决方案](https://www.bilibili.com/video/BV15t421K7w5/)

vCluster 是一个创新的开源解决方案，它提供给我们全功能的虚拟 Kubernetes 集群。vCluster 本身就运行在底层 K8s 集群的一个命名空间中，这样就可以实现在命名空间级别的资源隔离，同时，vCluster 可以提供比单纯的命名空间更好的多租户和隔离性，因为它允许用户使用 CRDs、命名空间、集群角色等集群范围的资源。

开源项目地址：https://github.com/loft-sh/vcluster

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247490415&idx=1&sn=38d2c75e4b8c5bc5438e1a89e9f013a2&chksm=9b3f8bb7ac4802a1c7a0f55e74c8ff55108d62d4132b572416740295e85fa415ab54114ce538#rd

###### 2、Go 超快安全轻量级的 Actor 引擎

[Go 超快安全轻量级的 Actor 引擎](https://www.bilibili.com/video/BV1gn4y197Rw/)

Hollywood 是一个基于 Golang 的超快安全轻量级的 Actor 引擎项目。它是为快速和低延迟的应用程序（如游戏服务器，广告代理商，交易引擎等）而构建的，能在一秒内处理超过 1000 万的消息。Hollywood 的主要特性包括消息在 Actor 失败时的可靠传输 (缓冲机制)、忘却式或请求响应式消息传送，采用高性能的 dRPC 作为运输层、优化的 proto 缓冲区（没有反射）、轻量级和高度可定制、集群支持等。

开源项目地址：https://github.com/anthdm/hollywood

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247489647&idx=1&sn=78b66d76491dc095a7b110ac7a832655&chksm=9b3f88b7ac4801a171535f20a604b0428654262e1f2620ad703821553a19d7793daa6a4a8edb#rd

###### 3、更快更安全的全新 SSH3 协议

SSH3 项目是 SSH 协议的全新改造。基于 HTTP 的机制，使用 QUIC+TLS1.3 进行安全通道的建立，使用 HTTP 授权机制进行用户认证。

开源项目地址：https://github.com/francoismichel/ssh3

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247490013&idx=1&sn=89fdcec334ff1a8d83b3da7070b60150&chksm=9b3f8905ac480013ba6b99a5e1f8fab2e09ccbc5c8534c0835e300a5e413173161f091ebe778#rd

如果觉得我们的视频还不错的话，欢迎大家一键三连关注我们，我们也会做更多有意思的视频。

读者专属插件：github.com/ZhuPeng/github_linker

公众号快速添加小程序插件：github.com/ZhuPeng/mp-transform-public