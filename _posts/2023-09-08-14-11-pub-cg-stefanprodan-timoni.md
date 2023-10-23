---
layout: post
title: Timoni - 一个由 CUE 驱动，受 Helm 启发的 Kubernetes 包管理器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在 Kubernetes 的生态系统中，我们经常需要对各种应用进行打包和部署。传统的 Helm 或 Kustomize 方案虽然能够满足需求，但在使用过程中，我们可能会遇到 Go 模板和 YAML 混合使用的问题，或者需要在 YAML 上进行多层次的叠加，这些都会给我们的开发工作带来一定的困扰。

今天要给大家推荐一个 GitHub 开源项目 stefanprodan/timoni，该项目在 GitHub 有接近 1000 Star，用一句话介绍该项目就是：“Timoni is a package manager for Kubernetes, powered by CUE and inspired by Helm.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231004203221160.png)

###### 项目介绍

Timoni 是一个由 CUE 驱动，受 Helm 启发的 Kubernetes 包管理器。该项目的目标是改善编写 Kubernetes 配置的用户体验。与 Helm 的 Go 模板和 YAML 混合使用，或者 Kustomize 的 YAML 多层叠加相比，Timoni 利用 cuelang 的类型安全、代码生成和数据验证功能，为创建、打包和交付 Kubernetes 应用提供了更好的体验。

Timoni 的主要组成部分包括模块（Module）、实例（Instance）和包（Bundle）。模块是一组由用户提供的 values.cue 文件驱动的 CUE 定义和约束，输出一组 Kubernetes 对象，由 Timoni 部署在 Kubernetes 上。实例代表了在 Kubernetes 集群上的模块实例化，用户可以提供自己的 values.cue 文件，与模块中的默认值进行合并。包则提供了一种声明式的方式来管理应用及其基础设施的生命周期。

###### 如何使用

首先，访问文档网站 timoni.sh 来开始安装和使用 Timoni，安装方式参考如下：

```bash
# Install with brew: macOS or Linux
brew install stefanprodan/tap/timoni
# Install with arkade: Windows, macOS or Linux
arkade get timoni
# Install with nix
nix-env -i timoni
# Install from source: Using Go >= 1.21
go install github.com/stefanprodan/timoni/cmd/timoni@latest
```

对于已经安装好了 timoni 命令行工具，且已有以下本地模块，你可以使用以下命令：

- 初始化模块：timoni mod init
- 检查模块：timoni mod lint
- 构建模块：timoni build  -n
- 应用模块：timoni apply  -f  --dry-run --diff

对于远程模块的操作，你可以使用以下命令：

- 推送模块：timoni mod push  <path/to/module> oci://<module-url> -v <semver>
- 拉取模块：timoni mod pull oci://<module-url> -v <semver> -o <path/to/module>
- 列出模块：timoni mod list oci://<module-url>

对于实例的操作，你可以使用以下命令：

- 应用实例：timoni apply <name> oci://<module-url> -v <semver> -f <path/to/values.cue>
- 删除实例：timoni delete  <name> -n <namespace>
- 列出实例：timoni list -n <namespace>
- 检查实例：timoni inspect [module|values|resources] <name> -n <namespace>
- 查看状态：timoni status <name> -n <namespace>

###### 项目推介

Timoni 项目目前仍在积极开发中，虽然 API 和命令行接口可能会发生变化，但其独特的设计理念和对 Kubernetes 配置编写体验的改进，使其具有很高的关注价值。如果你在 Kubernetes 的应用打包和部署方面有需求，或者对 Helm 和 Kustomize 方案有所困扰，那么 Timoni 项目值得你一试。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stefanprodan/timoni&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stefanprodan/timoni 

开源项目作者：stefanprodan

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stefanprodan/timoni)

关注我们，一起探索有意思的开源项目。

