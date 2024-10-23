---
layout: post
title: 容器镜像和文件系统漏洞扫描器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着容器技术的普及，容器安全成为企业云原生应用部署的重要考虑因素。容器镜像可能包含已知的漏洞，这些漏洞如果不被及时发现和修复，将给企业信息安全带来严重隐患。而随着应用依赖的不断增加，手动检查容器镜像和文件系统中的漏洞变得越来越困难，耗时且容易出错，这就迫切需要一个自动化、高效且可靠的漏洞扫描工具来解决这个问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-bbeec61ec16577b923c36824595b7b07.png)

今天要给大家推荐一个 GitHub 开源项目 grype，该项目在 GitHub 有超过 8.7k Star。

![](https://stats.deeptrain.net/repo/anchore/grype/?theme=light)

一句话介绍该项目：A vulnerability scanner for container images and filesystems

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831230328465.png)


###### 项目介绍

Grype 是一个用于容器镜像和文件系统的漏洞扫描器，它易于安装，与 Syft 协同工作，为容器镜像和文件系统提供了强大的软件物料清单（SBOM）工具。Grype 能扫描容器镜像或文件系统的内容，发现已知的漏洞，支持 Docker、OCI 和 Singularity 镜像格式。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831230427907.png)

它不仅涵盖主流操作系统包（如 Alpine、Ubuntu、CentOS 等）的漏洞扫描，也支持多种语言特定软件包的漏洞扫描（如 Ruby、Java、Python 等）。此外，Grype 还提供 OpenVEX 支持，用于过滤和增强扫描结果。

以下是一个使用示例：

![](https://user-images.githubusercontent.com/590471/90276236-9868f300-de31-11ea-8068-4268b6b68529.gif)

###### 如何使用

安装可以通过 curl 脚本、Chocolatey、Homebrew 或 MacPorts 进行安装

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831230606152.png)

curl 的具体命令如下：

```bash
# curl
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
```

安装完成后，通过简单的命令就可以开始扫描容器镜像的漏洞，示例命令如下：

```shell
# scan certain image
grype yourrepo/yourimage:tag
```

###### 项目推介

Grype 的可靠性和易用性使其成为容器安全领域的一个重要工具。此外，该项目还与 Syft 紧密集成，提供了一套完整的软件物料清单管理解决方案，进一步增强了其在容器安全方面的应用能力。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240831230733584.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=anchore/grype&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/anchore/grype 

开源项目作者：anchore

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=anchore/grype)

关注我们，一起探索有意思的开源项目。

