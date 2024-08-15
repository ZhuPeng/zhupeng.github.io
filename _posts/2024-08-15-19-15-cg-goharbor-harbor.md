---
layout: post
title: GitHub 开源项目 goharbor/harbor 介绍，An open source trusted cloud native registry project that stores, signs, and scans content.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 goharbor/harbor，该项目在 GitHub 有超过 23.3k Star。

![](https://stats.deeptrain.net/repo/goharbor/harbor/?theme=light)

一句话介绍该项目：An open source trusted cloud native registry project that stores, signs, and scans content.




![Nightly Status](https://us-central1-eminent-nation-87317.cloudfunctions.net/harbor-nightly-result)

![](https://raw.githubusercontent.com/goharbor/website/master/docs/img/readme/harbor_logo.png)


###### 项目介绍

### 背景介绍：

在当今的软件开发环境中，随着云原生技术的蓬勃发展，容器化和服务化架构已经变得越来越流行。这种发展趋势对于应用程序的部署和管理提出了新的挑战，尤其是在容器镜像的存储、分发和安全性方面。开发团队面临的核心痛点包括但不限于：如何高效地管理和分发容器镜像、如何确保镜像的安全性、以及如何实现多个环境之间镜像的快速同步。同时，企业还需要确保其开发流程中的用户认证、权限控制和操作审计能够符合内部的安全策略和合规要求。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-3a64e455dd6be28a2c29caba43108d5f.png)

项目介绍：

[Harbor](https://github.com/goharbor/harbor) 是一个开源的、值得信赖的云原生注册中心项目，用于存储、签名和扫描内容。Harbor 扩展了开源的 Docker Distribution，增加了用户通常需要的功能，如安全性、身份和管理。注册中心靠近构建和运行环境可以提高镜像传输效率。Harbor 支持在注册表之间复制镜像，并提供高级安全功能，例如用户管理、访问控制和活动审计。此外，Harbor 还通过定期扫描镜像来检测漏洞，并支持通过策略检查防止部署有漏洞的镜像。

### 如何使用：

**系统要求：** 在 Linux 主机上，需要 docker 20.10.10-ce+ 和 docker-compose 1.18.0+。

1. 下载 [Harbor 发行版的二进制文件](https://github.com/vmware/harbor/releases)。
2. 遵循 [安装和配置指南](https://goharbor.io/docs/latest/install-config/) 来安装 Harbor。
3. 如果您想在 Kubernetes 上部署 Harbor，请使用 [Harbor chart](https://github.com/goharbor/harbor-helm)。

更多关于如何使用 Harbor 的详细信息，请参考 [官方文档](https://goharbor.io/docs/)。

### 项目推介：

Harbor 是由 [云原生计算基金会](https://cncf.io) (CNCF) 托管的项目，它已经成为许多组织在构建云原生技术生态系统时的关键组件。以其强大的功能、灵活的部署方式和高级的安全特性，Harbor 获得了业界的广泛认可和使用，包括传统企业到创新型科技公司。Harbor 还通过 OCI 分发一致性测试，确保了与其他标准 registry 服务的良好兼容性。凭借活跃的开发者社区和丰富的生态系统支持，Harbor 不断演进，为用户带来最前沿的技术和最佳实践。无论是在寻求高效镜像管理解决方案的组织还是关注云原生安全的团队，Harbor 都能提供强大支持，帮助他们在云原生时代取得成功。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=goharbor/harbor&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/goharbor/harbor 

开源项目作者：goharbor

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=goharbor/harbor)

关注我们，一起探索有意思的开源项目。

