---
layout: post
title: GitHub 开源项目 aquasecurity/trivy 介绍，Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 aquasecurity/trivy，该项目在 GitHub 有超过 18.9k Star，用一句话介绍该项目就是：“Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more”。


![k8s summary](https://raw.githubusercontent.com/aquasecurity/trivy/master/docs/imgs/trivy-k8s.png)
![](https://raw.githubusercontent.com/aquasecurity/trivy/master/docs/imgs/logo.png)





背景介绍：
在当前的云计算环境中，容器、Kubernetes、代码仓库等都可能成为安全隐患的源头。这些隐患可能包括已知的漏洞（CVEs）、配置错误、敏感信息和秘密等。为了解决这些问题，我们需要一个全面且多功能的安全扫描器。

项目介绍：
Trivy 是一个全面且多功能的安全扫描器，它可以扫描容器镜像、文件系统、Git 仓库（远程）、虚拟机镜像、Kubernetes 和 AWS。Trivy 可以在这些目标中找到操作系统包和正在使用的软件依赖（SBOM）、已知的漏洞（CVEs）、IaC 问题和配置错误、敏感信息和秘密、软件许可证等。Trivy 支持大多数流行的编程语言、操作系统和平台。

如何使用：
Trivy 可以通过多种方式安装，包括通过 brew 安装、通过 docker 运行、从官网下载二进制文件等。Trivy 还可以与许多流行的平台和应用程序集成，包括 GitHub Actions、Kubernetes operator、VS Code 插件等。使用 Trivy 进行扫描的命令格式为 "trivy [--scanners] "，例如 "trivy image python:3.4-alpine"。

项目推介：
Trivy 是由 Aqua Security 开发的开源项目，Aqua Security 是一家知名的云原生安全公司。Trivy 的开发活跃，且已经有许多知名的用户和公司在使用。如果你对 Trivy 感兴趣，你还可以尝试 Aqua，它在 Trivy 的基础上提供了更多增强的功能，以提供完整的安全管理服务。




以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/aquasecurity/trivy 

开源项目作者：aquasecurity

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=aquasecurity/trivy)

关注我们，一起探索有意思的开源项目。

