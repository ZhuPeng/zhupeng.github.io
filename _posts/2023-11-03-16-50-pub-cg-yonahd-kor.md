---
layout: post
title: Kor - 探察和发现 Kubernetes 中未使用的资源
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着微服务的普及，我们越来越依赖 Kubernetes ( K8s ) 这样的容器编排工具进行部署。然而，在日常使用过程中，我们常常会遇到一个问题 —— 如何有效地找出并管理未使用的 Kubernetes 资源？这些包括 ConfigMaps、Secrets、Services、ServiceAccounts 等，这些悬浮（未被管理）的资源可能会占用额外的计算和存储资源，同时也给系统安全、维护、以及云成本管理带来额外的挑战。

今天要给大家推荐一个 GitHub 开源项目 yonahd/kor，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“A Golang Tool to discover unused Kubernetes Resources ”。

![](https://raw.githubusercontent.com/yonahd/kor/master//images/kor_logo.png)

![](https://raw.githubusercontent.com/yonahd/kor/master//images/screenshot.png)

###### 项目介绍

Kor 是基于 Golang 开发的一款工具，主要功能为探察和发现 Kubernetes 中未使用的资源。Kor 能够发现并列出的未使用资源包括：ConfigMaps、Secrets、Services、ServiceAccounts、Deployments、StatefulSets、Roles、HPAs、PVCs、Ingresses、PDBs 等。有了 Kor，管理员可以更好地感知和掌控 Kubernetes 集群的资源使用情况，从而做到更为精细和有效的资源管理。

以下是基于 Kor 展示的未使用资源监控图：

![Grafana Dashboard](https://raw.githubusercontent.com/yonahd/kor/master//grafana/dashboard-screenshot-1.png)

###### 如何使用

您可以从 [releases page](https://github.com/yonahd/kor/releases) 下载适合您的操作系统的 Kor 二进制文件，并将其添加到您的系统 PATH 中。也可以通过 Homebrew、源代码编译、Docker、Helm 等方式进行安装。

```bash
brew install kor

go install github.com/yonahd/kor@latest

docker run --rm -i yonahdissen/kor
docker run --rm -i -v "/path/to/.kube/config:/root/.kube/config" yonahdissen/kor all
```

Kor 提供了一系列子命令供您搜索和列出未使用的资源，如 `all`、`configmap`、`secret` 等。使用过程中若遇到问题，您可以参考项目的 README 文档，其中提供了丰富的使用示例和命令参数解释。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119224634228.png)

###### 项目推介

Kor 的代码覆盖率在 codecov 上有良好的表现，说明代码质量还不错。如果你在 Kubernetes 上有消耗未利用资源的问题，那么 Kor 是你必不可少的工具。希望你能用有效地应对 Kubernetes 的资源管理挑战，并为 Kor 提供更多的反馈和贡献，共同推动这个项目成长。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=yonahd/kor&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/yonahd/kor 

开源项目作者：yonahd

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=yonahd/kor)

关注我们，一起探索有意思的开源项目。

