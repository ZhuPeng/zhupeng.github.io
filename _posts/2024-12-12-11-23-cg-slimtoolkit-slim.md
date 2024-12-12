---
layout: post
title: GitHub 开源项目 slimtoolkit/slim 介绍，Slim(toolkit): Don't change anything in your container image and minify it by up to 30x (and for compiled languages even more) making it secure too! (free and open source)
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 slimtoolkit/slim，该项目在 GitHub 有超过 20.1k Star。

![](https://stats.deeptrain.net/repo/slimtoolkit/slim/?theme=light)

一句话介绍该项目：Slim(toolkit): Don't change anything in your container image and minify it by up to 30x (and for compiled languages even more) making it secure too! (free and open source)




![SK](https://raw.githubusercontent.com/slimtoolkit/slim/master/assets/images/dslim/logo.png)

![Slim How](https://raw.githubusercontent.com/slimtoolkit/slim/master/assets/images/docs/SlimHow.jpeg)

![asciicast](https://raw.githubusercontent.com/slimtoolkit/slim/master/assets/images/dslim/DockerSlimIntPromptDemo.gif)

![asciicast](https://asciinema.org/a/rHqW8cbr3vXe0WxorHsD36n7V.png)

![DockerSlim demo](http://img.youtube.com/vi/uKdHnfEbc-E/0.jpg)

![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)

![DHD3](https://raw.githubusercontent.com/slimtoolkit/slim/master/assets/images/dhd/docker_global_hackday3_red.png)

![](https://raw.githubusercontent.com/slimtoolkit/slim/master/assets/images/cncf/cncf.svg)


###### 项目介绍

背景介绍：
在当今的云原生时代，容器化技术如Docker已经变得无处不在，为应用程序的部署和运行提供了极大的便利。然而，随着容器的普及，开发者面临着一个普遍问题：如何让容器镜像既轻量又安全？一个臃肿的容器会增加传输时间、占用更多的存储空间，并可能因为包含过多无用文件而带来安全隐患。手动优化Dockerfile和配置安全策略又是一件耗时耗力，需要深入了解Linux内核和各种安全机制的任务。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-63a5715d0fea8fc08af4baee19b9a5cb.png)

项目介绍：
针对上述问题，**Slim**（以全名 **SlimToolkit** 出现）提供了一个优雅的解决方案。**Slim** 是一个由 [Kyle Quest](https://twitter.com/kcqon) 创建并得到 [Slim.AI](https://slim.ai) 支持的开源项目，它允许开发者不做任何改变，即可将容器镜像缩减达30倍，对于编译型语言甚至更多。**Slim** 的主要功能包括 `xray`、`lint`、`build`、`debug`、`run`、`images`、`merge`、`registry`、`vulnerability` 等多种命令，不仅优化了镜像，还增强了安全性。它支持多种编程语言和操作系统，无需修改原有的Dockerfile或丢弃现有的工作流程。此外，**Slim** 通过分析应用需求，智能地精简容器，同时提供专用的调试side-car容器，利用`xray`命令，甚至能在优化前后对容器镜像进行深入比较，提供洞见。

如何使用：
首先，确保你的环境中安装了 Docker。接着，通过以下命令安装 **Slim**：
```bash
>> docker pull slimtoolkit/slim
```
使用 **Slim** 构建并优化一个包含 `curl` 的 `archlinux` 镜像作为示例：
```bash
>> slim build --target archlinux:latest --tag archlinux:curl --http-probe=false --exec "curl checkip.amazonaws.com"
...
>> docker run archlinux:curl curl checkip.amazonaws.com
...
>> docker images
archlinux                 curl                ...        ...         17.4MB
```

项目推介：
**Slim** 已成为CNCF的沙箱项目，持续由广泛的社区成员参与改进。它已被多种编程语言和操作系统上的应用证实有效，如 Node.js、Python、Ruby 等，支持的系统包括 Ubuntu、Debian、CentOS及Alpine等。由创始人Kyle Quest，一个在开源社区有着高度认可的人物，到目前为止项目已经吸引了大量的贡献者，这保证了 **Slim** 的活跃开发和持续改进。得益于其出色的优化能力和提升容器安全的特性，以及便捷的用户体验，**Slim** 已被多家知名公司和项目采用。如果你也正苦恼于如何优化你的容器镜像，提高安全性，同时不想改变现有的工作流程，**Slim** 可能是你最佳的选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=slimtoolkit/slim&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/slimtoolkit/slim 

开源项目作者：slimtoolkit

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=slimtoolkit/slim)

关注我们，一起探索有意思的开源项目。

