---
layout: post
title: 【视频】大模型加持的浏览器自动化工具
tags: 视频
---

最近又有新视频发布了，后续我们会定期把在 B 站更新的热门推文视频在公众号上做一下同步，但是一般会有滞后一到两周，如果大家想及时观看视频，欢迎关注我们的 B 站同名账号 **GitHub精选**。

######  1、非 Docker 无守护进程的容器管理工具

[非 Docker 无守护进程的容器管理工具](https://www.bilibili.com/video/BV1dZ421M7R4/)

Podman 是一个全面的容器管理工具，旨在解决 OCI（开放容器倡议）标准容器和容器组的管理问题。作为一个无守护进程、支持多平台的工具，Podman 提供了完整的容器生命周期管理，包括容器的创建、运行、停止以及移除。它还支持容器镜像的全面管理，如拉取、构建、提交和推送到各种存储后端。此外，Podman 在支持无 root 运行容器方面做了特别的优化，提供了用户级别的命名空间隔离，增强了容器的安全性和隔离性。

开源项目地址：https://github.com/containers/podman

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247491165&idx=1&sn=2be6c22087a33b3499836dbcaaa13d32&chksm=9b3f8e85ac480793eeabb4f6658cf297fc4093be7b5440b90dbfbaddaaa58546eb8080ad2676#rd

###### 2、大模型加持的浏览器自动化工具，抢茅台也是可以的

[大模型加持的浏览器自动化工具，抢茅台也是可以的](https://www.bilibili.com/video/BV1QW421X78w/)

Skyvern 主要是利用了大语言模型（LLMs）和计算机视觉技术来自动化浏览器操作流程。Skyvern 不仅能解析实时视窗中的项目，创建互动方式，并进行交互，而且可以在从未见过的网站上运行，通过将视觉元素映射到完成工作流所需的操作，无需任何定制代码。更重要的是，Skyvern 遇到页面布局变化时，不会像传统的自动化工具那样出现问题，因为它没有预设的 XPaths 或者寻找页面导航需要的其他选择器。Skyvern 通过 LLMs 处理交互来应对更复杂的情况，并且对于网页变化及时准确反应。

开源项目地址：https://github.com/Skyvern-AI/skyvern

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247490843&idx=1&sn=a431f9b22a7e6431e148bbb1920de09f&chksm=9b3f8dc3ac4804d5e55cca45d6f2caa5a9d5f53843fd79e6762feeb48a4455526e77a11b151e#rd

###### 3、基于 Go eBPF 的开源云原生负载均衡器

[基于 Go eBPF 的开源云原生负载均衡器](https://www.bilibili.com/video/BV1Qi421e7bN/)

loxilb 是一款基于 Go  eBPF 的开源云原生负载均衡器，能实现广泛的 K8S 环境的互通性。loxilb 主要用于提供服务类型的负载均衡，可以根据用户需求在集群内或集群外运行，还支持 cluster-ip 和 node-port 服务，从而为 Kubernetes 提供端到端的连通性。它的性能优于众多竞品，使用了 eBPF 实现了高度的灵活性和可定制性，还提供了高级的服务质量（可分别针对负载均衡器、端点或客户端进行调整）。

开源项目地址：https://github.com/loxilb-io/loxilb

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247490089&idx=1&sn=be8ffdf4e4707fc36a34c28dd679ba00&chksm=9b3f8af1ac4803e712221608f2d0deddb9179a268f1c5f2c61d78109dfdfeafc23247405f7fe#rd

如果觉得我们的视频还不错的话，欢迎大家一键三连关注我们，我们也会做更多有意思的视频。

读者专属插件：github.com/ZhuPeng/github_linker

公众号快速添加小程序插件：github.com/ZhuPeng/mp-transform-public