---
layout: post
title: 在 Kubernetes 中构建容器镜像
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当前快速发展的云计算和容器化技术时代，开发者和企业面临着持续集成与持续部署（CI/CD）的挑战。构建容器镜像通常依赖于 Docker 守护进程，这在一些环境下存在安全与兼容性问题，尤其是在 Kubernetes 集群中。这里的核心痛点包括：Docker 守护进程的依赖限制了构建环境的灵活性，同时也增加了安全隐患；此外，在 Kubernetes 集群中直接构建镜像的需求日益增加，而现有工具往往不能提供满意的解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241007214834279.png)

今天要给大家推荐一个 GitHub 开源项目 kaniko，该项目在 GitHub 有超过 14.7k Star。

![](https://stats.deeptrain.net/repo/GoogleContainerTools/kaniko/?theme=light)

一句话介绍该项目：Build Container Images In Kubernetes

![](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/master/logo/Kaniko-Logo.png)

###### 项目介绍

**kaniko** 是一个可以在容器或 Kubernetes 集群内部，直接从 Dockerfile 构建容器镜像，而无需 Docker 守护进程。kaniko 实现了在用户空间内部执行 Dockerfile 中的每一条指令，使得在无法或不安全运行 Docker 守护进程的环境里，也能构建容器镜像，从而为 Kubernetes 环境下的镜像构建带来了革命性的进步。

![](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/master/docs/images/multi-arch.drawio.svg)

主要功能如下：

1、无需 Docker 守护进程： kaniko 不依赖 Docker 守护进程，可在任何用户空间中执行 Dockerfile 命令。

2、安全和便捷：适用于不易或不安全运行 Docker 守护进程的环境，如标准的 Kubernetes 集群。

3、灵活性：支持多种构建上下文和存储解决方案，如 Azure Blob Storage、私有 Git 仓库等。

4、高效缓存：提供强大的缓存选项，包括缓存层和基础镜像的缓存，显著提高构建效率。

5、多平台构建支持：通过 `--custom-platform` 标志，支持为不同平台构建镜像。

![](https://raw.githubusercontent.com/GoogleContainerTools/kaniko/master/docs/demo.gif)

###### 如何使用

首先需要将 executor 镜像 `gcr.io/kaniko-project/executor` 部署到集群中。以下是一个基本示例：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: kaniko
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:latest
    args: ["--dockerfile=<Path2Dockerfile>",
           "--context=dir://<Path2BuildContext>",
           "--destination=<TargetImageName>"]
    volumeMounts:
    - name: kaniko-secret
      mountPath: /kaniko/.docker
  volumes:
  - name: kaniko-secret
    secret:
      secretName: <DockerSecretName>
```

这个简单配置演示了如何在 Kubernetes 中运行 kaniko 来构建并推送镜像。

###### 项目推介

虽然 kaniko 不是一个官方支持的 Google 产品，但它已经在社区中获得广泛的关注和使用。它由 Google Container Tools 团队维护更新，保证了项目的活跃和技术支持。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909221604521.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=GoogleContainerTools/kaniko&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/GoogleContainerTools/kaniko 

开源项目作者：GoogleContainerTools

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=GoogleContainerTools/kaniko)

关注我们，一起探索有意思的开源项目。

