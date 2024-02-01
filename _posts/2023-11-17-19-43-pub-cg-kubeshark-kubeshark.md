---
layout: post
title: Kubeshark - 一个专为 Kubernetes 设计的 API 流量分析器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在使用 Kubernetes 进行微服务管理的过程中，我们常常会遇到一些诸如服务间通信失败、请求延迟高昂或丢包等网络问题，然而 Kubernetes 的内部网络环境极为复杂，各个服务间的通信都通过协议进行，此时我们需要一个工具能够实时监控 Kubernetes 中的网络通信，并能在问题出现时尽快发现和定位问题。

今天要给大家推荐一个 GitHub 开源项目 kubeshark/kubeshark，该项目在 GitHub 有超过 9.8k Star，用一句话介绍该项目就是：“The API traffic analyzer for Kubernetes providing real-time K8s protocol-level visibility, capturing and monitoring all traffic and payloads going in, out and across containers, pods, nodes and clusters. Inspired by Wireshark, purposely built for Kubernetes”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231217220755655.png)

###### 项目介绍

Kubeshark 是一个专为 Kubernetes 设计的 API 流量分析器，灵感来自于 Wireshark，它能提供 Kubernetes 内部网络的实时、协议级别的可视化效果，捕获并监控所有在各个容器、pod、节点及集群之间进行的通信和传输。此外，Kubeshark 也发布了最新版本 v51.0.0，其中包含明显的性能提升和资源优化。

以下是 Kubeshark 的使用页面：

![](https://github.com/kubeshark/assets/raw/master/png/kubeshark-ui.png)

###### 如何使用

首先，从 Kubeshark 的 GitHub 项目页面下载最新发布的二进制发行版，或者Homebrew 用户可以通过以下命令添加 Kubeshark 并进行安装：

```shell
brew tap kubeshark/kubeshark
brew install kubeshark
```

然后运行以下示例命令：

```shell
kubeshark tap
```
或：
```shell
kubeshark tap -n sock-shop "(catalo*|front-end*)"
```
运行上述命令后，将在您的浏览器中打开 Web UI，实时展示 Kubernetes 集群中的流量情况。

###### 项目推介

Kubeshark 是一个活跃的开源项目，其功能强大且易用，为 Kubernetes 网络分析提供了一种非常有效的方式。项目的维护者不仅积极更新包含性能优化及资源优化等重要特性的版本，也非常欢迎社区的贡献。Kubeshark 具备良好的文档支持，旨在帮助开发者快速上手和理解 Kubeshark。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubeshark/kubeshark&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubeshark/kubeshark 

开源项目作者：kubeshark

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubeshark/kubeshark)

关注我们，一起探索有意思的开源项目。

