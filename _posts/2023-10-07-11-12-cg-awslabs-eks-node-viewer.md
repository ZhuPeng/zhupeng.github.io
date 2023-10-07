---
layout: post
title: GitHub 开源项目 awslabs/eks-node-viewer 介绍，EKS Node Viewer
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 awslabs/eks-node-viewer，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“EKS Node Viewer”。


![](https://raw.githubusercontent.com/awslabs/eks-node-viewer/master/./.static/screenshot.png)





背景介绍：
在日常的集群管理中，我们常常需要对节点的使用情况进行可视化展示，以便更好地理解和管理集群资源。然而，传统的工具往往无法满足我们对动态节点使用情况的可视化需求，无法清晰地展示出已调度的 pod 资源请求与节点上的可分配容量之间的关系。这就是我们需要 "EKS Node Viewer" 这个项目的原因。

项目介绍：
"EKS Node Viewer" 是一个用于可视化集群内动态节点使用情况的工具。它最初是 AWS 内部开发的一个工具，用于展示 Karpenter 的整合能力。它能够展示已调度的 pod 资源请求与节点上的可分配容量之间的关系，但并不查看实际的 pod 资源使用情况。此外，它还支持一些自定义标签名称，可以通过 --extra-labels 传递给它以显示更多的节点信息。

如何使用：
"EKS Node Viewer" 的安装非常简单，可以通过 Homebrew 或者手动安装。安装完成后，可以通过命令行参数来使用它，例如查看特定的 AWS 配置文件和区域，或者显示 CPU 和内存的使用情况等。此外，你还可以通过在家目录创建一个名为 .eks-node-viewer 的文件来提供默认选项。

项目推介：
"EKS Node Viewer" 是 AWS 实验室开发的开源项目，开发活跃，更新频繁，已经在 AWS 的内部得到了广泛的应用。它的功能强大，使用简单，非常适合需要管理和监控 Kubernetes 集群的开发者和运维人员使用。此外，它还在 AWS re:Invent 2022 等多个会议上进行了展示，受到了业内人士的高度评价。




以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=awslabs/eks-node-viewer&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/awslabs/eks-node-viewer 

开源项目作者：awslabs

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=awslabs/eks-node-viewer)

关注我们，一起探索有意思的开源项目。

