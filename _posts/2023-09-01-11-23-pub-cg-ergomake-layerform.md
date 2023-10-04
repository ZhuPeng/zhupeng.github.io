---
layout: post
title: Layerform - 基于 Terraform 帮助工程师创建可复用的环境堆栈
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常的软件开发过程中，我们常常会遇到环境配置的问题。每当我们需要创建一个新的环境，比如一个 staging 环境，我们往往需要从头开始配置，这不仅耗时耗力，而且可能会因为配置的细微差异导致环境不一致的问题。这就是我们需要解决的核心痛点。

今天要给大家推荐一个 GitHub 开源项目 ergomake/layerform，该项目在 GitHub 有超过 891 Star，用一句话介绍该项目就是：“Layerform helps engineers create reusable environment stacks using plain .tf files. Ideal for multiple "staging" environments.”。

![](https://raw.githubusercontent.com/ergomake/layerform/master/./assets/img/crocodile-spawn.png)

###### 项目介绍

Layerform 是一个基于 Terraform 的项目，它帮助工程师使用简单的 `.tf` 文件创建可复用的环境堆栈。Layerform 引入了 层的概念，每个层包含一些基础设施，可以堆叠在另一个层之上。这使得团队可以复用核心的基础设施部分，使得开发环境更加便宜且快速。使用 Layerform，工程师只需要描述他们需要的基础设施层，创建的过程交给 Layerform。

![](https://raw.githubusercontent.com/ergomake/layerform/master/./assets/img/dev-environments.png)


###### 如何使用

首先，你需要在你的机器上安装 Layerform。然后，你可以开始创建你的 `.tf` 文件，并使用 Layerform 来生成你的环境堆栈。以下是安装方式：

```bash
$ go install github.com/ergomake/layerform@latest
```

然后可以创建对应的层的描述，比如以下示例，分为 eks 和 services 层。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230907215718039.png)

![](https://raw.githubusercontent.com/ergomake/layerform/master/./assets/img/default-base-layer.png)

另外，如果你在 Kubernetes 集群中运行应用，你不需要为每个工程师的环境创建一个全新的集群。相反，你可以复用同一个集群，并让多个工程师在其上运行他们的应用。

![](https://raw.githubusercontent.com/ergomake/layerform/master/./assets/img/multiple-top-layers.png)

使用如下命令就可以根据需要创建对应层的实例。

```bash
$ layerform spawn services my-dev-infra
```

###### 项目推介

Layerform 设计理念和实现方式都非常独特，它的使用可以大大降低开发环境的创建和维护成本，提高开发效率。此外，Layerform 还能够自动跟踪每个层实例的成本，帮助你更好地管理你的资源。如果你是一名工程师，或者你的团队正在寻找一个有效的环境管理解决方案，我强烈推荐你试试 Layerform。

![](https://raw.githubusercontent.com/ergomake/layerform/master/./assets/img/lgtm-gnu.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ergomake/layerform&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ergomake/layerform 

开源项目作者：ergomake

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ergomake/layerform)

关注我们，一起探索有意思的开源项目。

