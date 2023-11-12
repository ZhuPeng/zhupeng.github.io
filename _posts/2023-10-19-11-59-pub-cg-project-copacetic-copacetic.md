---
layout: post
title: Copacetic - 基于 buildkit 的容器镜像漏洞修补工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的日常工作中，可能会遇到这样的问题：当容器镜像出现安全漏洞时，我们需要快速修补，但是往往需要等待上游进行全面重建，这样的时间窗口可能会导致漏洞被积极利用。特别是当这些漏洞来自于深层次的基础镜像，或者是你并不维护的第三方应用镜像时，等待更新发布的时间可能会超出你的安全服务等级协议。

今天要给大家推荐一个 GitHub 开源项目 project-copacetic/copacetic，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“CLI tool for directly patching container images using reports from vulnerability scanners”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029203357935.png)

###### 项目介绍

Copacetic 是一个用 Go 语言编写的、基于 buildkit 的 CLI 工具，它可以根据像 Trivy 这样的流行工具的漏洞扫描结果直接修补容器镜像。除了填补安全实践和工具无法满足的操作空白，Copacetic 还有以下优点：

- 允许除镜像发布者外的其他用户也能修补容器镜像，如 DevSecOps 工程师。
- 通过只创建一个额外的修补层，而不是重建整个镜像，减少了重新分发修补后的镜像的存储和传输成本。
- 无需等待基础镜像更新，操作速度比全面重建镜像更快，从而减少了修补容器镜像的周转时间。
- 通过运行一个工具对镜像进行操作，减少了从运行重建管道到修补镜像的复杂性。

一次示例修补流程参考如下：

![](https://raw.githubusercontent.com/project-copacetic/copacetic/master/./docs/imgs/direct-image-patching.png)

更详细的命令行使用 DEMO：

![](https://raw.githubusercontent.com/project-copacetic/copacetic/master/demo/copa-demo.gif)

###### 如何使用

Copacetic 是一个可扩展的引擎，它的工作流程如下：

1、解析由像 Trivy 这样的扫描器生成的容器镜像的漏洞报告中所需的更新包。可以编写新的适配器以适应更多的报告格式。

2、使用适当的包管理工具（如 apt，apk 等）获取和处理所需的更新包。可以编写新的适配器以支持更多的包管理器。

3、使用 buildkit 将结果更新二进制文件应用到容器镜像中。

![](https://raw.githubusercontent.com/project-copacetic/copacetic/master/./docs/imgs/vulnerability-patch.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231029203706342.png)

###### 项目推介

Copacetic 的设计理念是使直接修补容器变得广泛适用和易于访问，这使得开发者无需使用特定的工具构建他们的镜像或以某种方式修改它们以支持容器修补。同时，Copacetic 与现有的漏洞扫描和缓解生态系统兼容，这意味着镜像发布者无需为容器修补创建新的工作流程，消费者也无需迁移到新的、可能支持更有限的定制发行版的生态系统，或者改变他们的容器漏洞扫描管道。因此，我强烈推荐大家关注和使用 Copacetic 项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=project-copacetic/copacetic&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/project-copacetic/copacetic 

开源项目作者：project-copacetic

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=project-copacetic/copacetic)

关注我们，一起探索有意思的开源项目。

