---
layout: post
title: 【视频】专为 Go 语言设计的函数式编程库
tags: 视频
---

最近又有新视频发布了，后续我们会定期把在 B 站更新的热门推文视频在公众号上做一下同步，但是一般会有滞后一到两周，如果大家想及时观看视频，欢迎关注我们的 B 站同名账号**GitHub精选**。

######  1、专为 Go 语言设计的函数式编程库

[专为 Go 语言设计的函数式编程库](https://www.bilibili.com/video/BV1dC41187ju/)

fp-go 是一个功能强大的函数式编程库，专为 Go 语言设计。它的设计目标是提供一套数据类型和函数，使得在 Go 语言中编写可维护和可测试的代码变得简单而有趣。它鼓励以下编程开发模式：

a、编写许多小型、可测试和纯函数；

b、提供帮助器以将副作用隔离到延迟执行的函数（IO）中；

c、公开一致的组合集，以从现有函数创建新函数。

开源项目地址：https://github.com/IBM/fp-go

更多介绍：https://mp.weixin.qq.com/s?biz=MzAwMzE5NzM2Nw==&mid=2247488245&idx=1&sn=79fc0f03ccd552695dfa46b9381c782d&chksm=9b3f822dac480b3bdeac3def9058788928fd4fa426e22f472358d1cbf44c3eb16b920a6c8fd9&token=1240254177&lang=zh_CN&poc_token=HCc742WjWsp9wWOevTs7DV0hNdPNTKR1YxVMoRO9

###### 2、无需依赖 Docker，简单且快速的 Go 应用容器镜像构建工具

[无需依赖 Docker，简单且快速的 Go 应用容器镜像构建工具](https://www.bilibili.com/video/BV1Gr421p7ZR/)

ko 是一个简单且快速的 Go 应用的容器镜像构建工具，它主要解决上述在构建 Go 应用的过程中遇到的问题。ko 非常适合你的镜像包含一个 Go 应用，而且没有依赖于 OS 基础镜像的情况（比如，没有 cgo，没有 OS 包依赖）。ko 通过在你的本地机器上有效地执行 `go build` 来构建镜像，因此无需安装 docker，尤其适合轻量级的 CI/CD 使用场景。除此之外，ko 还支持简单的 YAML 模板，可以方便地实现 Kubernetes 应用的部署。

开源项目地址：https://github.com/ko-build/ko

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247489125&idx=1&sn=f81baefdb3ff1cab24a4279d53dfe00e&chksm=9b3f86bdac480fabf30d4233dd16a83b6b102280ea7a6d92fcac38405c18316710d5e9ef535a&token=1240254177&lang=zh_CN#rd

###### 3、探察和发现 Kubernetes 中未使用的资源

[探察和发现 Kubernetes 中未使用的资源](https://www.bilibili.com/video/BV1QC411W7Rm/)

Kor 是基于 Golang 开发的一款工具，主要功能为探察和发现 Kubernetes 中未使用的资源。Kor 能够发现并列出的未使用资源包括：ConfigMaps、Secrets、Services、ServiceAccounts、Deployments、StatefulSets、Roles、HPAs、PVCs、Ingresses、PDBs 等。有了 Kor，管理员可以更好地感知和掌控 Kubernetes 集群的资源使用情况，从而做到更为精细和有效的资源管理。

开源项目地址：https://github.com/yonahd/kor

更多介绍：https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247488954&idx=1&sn=b68c277db5121e61b0e74c99f69425b4&chksm=9b3f8562ac480c7425407b56498ff3352a4050d46b0ec4a472523d456df5237dd1bc36e008be&token=1240254177&lang=zh_CN#rd

如果觉得我们的视频还不错的话，欢迎大家一键三连关注我们，我们也会做更多有意思的视频。
