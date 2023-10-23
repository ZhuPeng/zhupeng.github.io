---
layout: post
title: Weaver - 一款简化分布式应用编写、部署和管理的编程框架
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在云计算和分布式技术日益发展的今天，我们经常会遇到编写、部署和管理分布式应用的需求。然而，这个过程可能会遇到各种问题，比如环境配置复杂、部署步骤繁琐、本地和云端环境一致性难以保证等。这些问题不仅消耗了大量的开发时间，也增加了项目的复杂性。

今天要给大家推荐一个 GitHub 开源项目 ServiceWeaver/weaver，该项目在 GitHub 有超过 3.8k Star，用一句话介绍该项目就是：“Programming framework for writing and deploying cloud applications.”，为云应用而设计的编程框架。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223009759.png)

###### 项目介绍

Weaver 是一个编程框架，专门用于编写、部署和管理分布式应用。你可以在本地机器上运行、测试和调试 Service Weaver 应用，然后用一个命令就可以将其部署到云端。这大大简化了开发和部署的过程，提高了工作效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223203336.png)

以下是本地和远程云部署的使用方式：

```
$ go run .                      # Run locally.
$ weaver gke deploy weaver.toml # Run in the cloud.
```

Weaver 的主要功能介绍如下：

1、高性能：使用 RPC 通信和序列化

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223357548.png)

2、更少的配置项

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223411076.png)

3、自动集成可观测性指标，包含日志、指标和链路追踪

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223500618.png)

4、内建的分片支持

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223538091.png)

###### 如何使用

首先，你需要访问 https://serviceweaver.dev/docs.html 进行安装和了解如何开始使用。可使用 Go 按如下方式安装：

```bash
go install github.com/ServiceWeaver/weaver/cmd/weaver@latest
```

安装好后可以按如下方式开发和部署应用：

1、将应用拆分定义成组件：使用接口对业务逻辑进行定义

组件对应于 Weaver 可独立调度和管理的单元，组件之间的交互由 Weaver 来管理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223805986.png)

2、调用组件：直接使用方法进行调用，不用关心内部的 RPC 或者 HTTP 调用

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006223949497.png)

3、部署组件：可选择本地或者其他的云进行部署

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006224050660.png)

4、调整组件部署方式：可按需进行单进程部署，或者多实例、多云的部署

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006224243705.png)

通过以上步骤，可以很明显的感知到，Weaver 的使用让开发者像开发单进程程序一样开发分布式程序，在部署时可根据负载按需的做多实例多云的部署调整，简直是分布式应用开发的利器，早期可以单进程部署，后期流量大了以后，可根据组件进行按需的调整部署配置。

###### 项目推介

Service Weaver 的设计理念非常独特，如果你对分布式应用的开发和部署感兴趣，或者你正在寻找一个可以提高工作效率的工具，那么 Service Weaver 将是你的不二之选。让我们一起参与到这个项目中，共同推动它的发展吧！

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ServiceWeaver/weaver&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ServiceWeaver/weaver 

开源项目作者：ServiceWeaver

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ServiceWeaver/weaver)

关注我们，一起探索有意思的开源项目。

