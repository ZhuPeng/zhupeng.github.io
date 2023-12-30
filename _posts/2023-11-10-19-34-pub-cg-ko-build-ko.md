---
layout: post
title: ko - 无需依赖 Docker，简单且快速的 Go 应用容器镜像构建工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在云原生应用的开发部署中，Go 语言由于其良好的并发性能和运行效率，越来越受到开发者的青睐。但是，构建 Go 应用的容器镜像却常常会遇到诸如：构建过程慢、依赖 Docker 服务、操作复杂以及无法方便的实现多平台构建（multi-platform builds）等问题。那么，如何快速、简单地构建和部署 Go 应用的容器镜像，成为了一个值得深入研究的问题。

今天要给大家推荐一个 GitHub 开源项目 ko-build/ko，该项目在 GitHub 有超过 6.6k Star，用一句话介绍该项目就是：“Build and deploy Go applications”。


![](https://raw.githubusercontent.com/ko-build/ko/master/./docs/images/demo.png)

###### 项目介绍

ko 是一个简单且快速的 Go 应用的容器镜像构建工具，它主要解决上述在构建 Go 应用的过程中遇到的问题。ko 非常适合你的镜像包含一个 Go 应用，而且没有依赖于 OS 基础镜像的情况（比如，没有 cgo，没有 OS 包依赖）。ko 通过在你的本地机器上有效地执行 `go build` 来构建镜像，因此无需安装 docker，尤其适合轻量级的 CI/CD 使用场景。除此之外，ko 还支持简单的 YAML 模板，可以方便地实现 Kubernetes 应用的部署。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203174422577.png)

###### 如何使用

根据 ko 的官方文档，你可以通过访问：`https://ko.build/install/`，来完成 ko 的安装。完成安装后，你可以通过访问：`https://ko.build/get-started/`，来了解如何开始使用 `ko` 进行 Go 应用的容器镜像构建和部署。

安装方法参考如下：

```bash
# Homebrew
brew install ko

# MacPorts
sudo port install ko

# Build from source
go install github.com/google/ko@latest
```

###### 项目推介

ko 是 Google 提交给 Cloud Native Computing Foundation 的沙箱项目。ko 的构建方式基于与 Docker 和 Kubernetes 相关的 Bazel 支持经验，其实验性工作已经在这里 https://www.youtube.com/watch?v=RS1aiQqgUTA 展示。除了 Google，相信还有更多的公司和个人在使用 ko 工具进行 Go 应用的容器化。如果你正好在处理构建和部署 Go 应用的相关工作，我建议你可以尝试使用 ko，相信你会有很好的体验。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203174828464.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ko-build/ko&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ko-build/ko 

开源项目作者：ko-build

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ko-build/ko)

关注我们，一起探索有意思的开源项目。

