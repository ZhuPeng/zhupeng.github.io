---
layout: post
title: GitHub 开源项目 containerd/containerd 介绍，An open and reliable container runtime
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 containerd/containerd，该项目在 GitHub 有超过 15.8k Star，用一句话介绍该项目就是：“An open and reliable container runtime”。


![containerd banner light mode](https://raw.githubusercontent.com/cncf/artwork/master/projects/containerd/horizontal/color/containerd-horizontal-color.png#gh-light-mode-only)
![containerd banner dark mode](https://raw.githubusercontent.com/cncf/artwork/master/projects/containerd/horizontal/white/containerd-horizontal-white.png#gh-dark-mode-only)
![architecture](https://raw.githubusercontent.com/containerd/containerd/master/docs/historical/design/architecture.png)
![cri](https://raw.githubusercontent.com/containerd/containerd/master/./docs/cri/cri.png)



项目背景：
对于开发人员和企业来说，为程序提供一个可靠、简单且可以无缝集成的容器运行环境，以及管理完整的容器生命周期，始终是一个值得关注的课题。同时，加强容器运行时环境的健壮性和通用性，对于促进开发效率、节约开发成本也起着至关重要的作用。

项目介绍：
`containerd` 是一款用突出其简便性、健壮性和可移植性的，行业标准的容器运行环境。它强大的功能包括图像传输和存储、容器执行和监控、底层存储和网络连接等。我们设计 `containerd` 用来被嵌入到一个更大的系统中，而非直接被遭遇第或最终用户使用。`containerd` 是 `CNCF` 中的一员，拥有 `graduated` 身份。

如何使用：
为了方便大家更快投入使用 `containerd` ，我们提供了详细的文档，并进行了分类：["for ops and admins"](docs/ops.md), ["namespaces"](docs/namespaces.md), ["client options"](docs/client-opts.md)。同时，如果你想为 `containerd` 做出贡献，可以查看我们的[贡献指南](CONTRIBUTING.md)。要尝试使用 `containerd`，请看我们的例子 [Getting Started](docs/getting-started.md)。

项目推介：
`containerd` 项目是目前最活跃的开源项目之一，是行业标准的容器运行环境，被大量知名的平台如 `Docker`, `moby`, `buildkit` 等所使用， `containerd` 的影响力及其广大。同时， `containerd` 已经获得 `CNCF` 的最高级别 `graduated` 认证，再一次证明了 `containerd` 的稳定和可靠。说明 `containerd` 不仅得到了业内人士的认可，同时也在大规模生产环境中历经考验，证明了其稳定、可靠和成熟。除此之外， `containerd` 项目还在招募更多的人员加入，无论是文档编写、社区推广还是安全顾问等都有位置，欢迎大家加入我们的行列。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=containerd/containerd&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/containerd/containerd 

开源项目作者：containerd

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=containerd/containerd)

关注我们，一起探索有意思的开源项目。

