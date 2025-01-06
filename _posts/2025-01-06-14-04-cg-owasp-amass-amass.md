---
layout: post
title: GitHub 开源项目 owasp-amass/amass 介绍，In-depth attack surface mapping and asset discovery
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 owasp-amass/amass，该项目在 GitHub 有超过 12.3k Star。

![](https://stats.deeptrain.net/repo/owasp-amass/amass/?theme=light)

一句话介绍该项目：In-depth attack surface mapping and asset discovery




![OWASP Logo](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/owasp_logo.png)

![ZeroFox Logo](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/zerofox_logo.png)

![IPinfo Logo](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/ipinfo_logo.png)

![WhoisXML API Logo](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/whoisxmlapi_logo.png)

![Accenture Logo](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/accenture_logo.png)

![Visma Logo](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/visma_logo.png)

![Network graph](https://raw.githubusercontent.com/owasp-amass/amass/master/./images/network_06092018.png "Amass Network Mapping")

![](https://github.com/owasp-amass/amass/blob/master/images/amass_video.gif)


###### 项目介绍

在当今日益复杂和动态变化的网络环境中，企业和组织面临的核心痛点之一是越来越难以有效地映射和识别其整个攻击面。随着资产数量的增长和分布的扩散，传统的信息收集和资产发现方法变得不再适用，无法全面、实时地捕捉到所有外部资产，这给企业的网络安全带来了极大的挑战。为了解决这个问题，需要一个先进的、集多种信息收集和主动侦察技术于一体的工具，`OWASP Amass` 便是针对这一需求而生。

**

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-e02afaa7cf53ee13a2e98810825804c4.png)

项目介绍：**

`OWASP Amass` 是一个开源项目，它通过开源信息收集和主动侦察技术进行网络映射和外部资产发现，帮助用户深入理解攻击面。该项目利用的信息收集技术涵盖了 `APIs`、`Certificates`、`DNS`、`Routing`、`Scraping` 及 `Web Archives` 等多个方面，涉及超过 30 种数据源，包括但不限于 `GitHub`、`Shodan`、`Censys` 等，这使它能够提供比传统方法更为精确和广泛的信息。

**如何使用：**

使用 `OWASP Amass` 非常便捷，你可以通过多种方式进行安装：

- **预编译的包**：只需解压并将预编译的二进制文件放入你的路径中即可开始使用；
- **Homebrew**：如果你是 macOS 用户，可以简单地通过 `brew tap owasp-amass/amass` 和 `brew install amass` 命令进行安装；
- **Docker 容器**：通过运行 `docker pull caffix/amass` 拉取 Docker 镜像，然后使用 `docker run` 命令以容器形式运行；
- **源代码安装**：对于希望从源代码构建的高级用户，可以通过 `Go` 编程语言环境来完成。

例如，使用 Docker 运行项目的命令如下：
```
docker run -v OUTPUT_DIR_PATH:/.config/amass/ caffix/amass enum -d example.com
```
这将使图形数据库在执行间保持持久性，并允许访问主机系统上的输出文件。

**项目推介：**

`OWASP Amass` 不仅仅是一个工具，它是企业和网络安全研究人员理解和评估其外部攻击面的有力武器。不仅开发活跃，拥有大量的贡献者和持续的更新，而且由于其出色的功能和效率，已经获得了例如 `Accenture` 和 `Visma` 等知名公司的高度评价和广泛应用。这些公司的网络防御经理和红队成员都赞扬了其在外部枚举项目和攻击面评估中的不可或缺性。此外，`OWASP Amass` 还是 `OWASP` 项目的一部分，这为其带来了更高的信誉和安全保障。

总之，无论你是一位网络安全专家，还是一家寻求增强外部攻击面了解与防护能力的企业， `OWASP Amass` 都是你不能错过的工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=owasp-amass/amass&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/owasp-amass/amass 

开源项目作者：owasp-amass

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=owasp-amass/amass)

关注我们，一起探索有意思的开源项目。

