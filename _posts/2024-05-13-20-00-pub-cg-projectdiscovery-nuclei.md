---
layout: post
title: 快速且可定制的漏洞扫描器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数字安全领域，随着互联网技术的飞速发展，企业和个人在享受便利的同时，也面临着越来越多的安全挑战。尤其是在保障网络安全方面，传统的安全扫描工具往往无法满足高效、灵活、准确的需求，例如误报高、扫描速度慢、难以定制和更新等问题。因此，需要一种能够快速、准确、灵活地识别和验证漏洞的工具，以帮助企业和开发者更好地防御潜在的网络安全风险。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-d37c8976a3de278ef9addb8c2de573ca.png)

今天要给大家推荐一个 GitHub 开源项目 projectdiscovery/nuclei，该项目在 GitHub 有超过 17.4k Star。

![](https://stats.deeptrain.net/repo/projectdiscovery/nuclei)

一句话介绍该项目：Fast and customizable vulnerability scanner based on simple YAML based DSL.



![](https://raw.githubusercontent.com/projectdiscovery/nuclei/master/static/nuclei-logo.png)

###### 项目介绍

**Nuclei** 是一个基于简单的 **YAML DSL** 语言快速且可定制的漏洞扫描器，它通过模板向目标发送请求，从而实现零误报，并且能在大量主机上进行快速扫描。**Nuclei** 支持多种协议的扫描，包含 TCP、DNS、HTTP、SSL、文件、Whois、Websocket、Headless、代码等。依托于强大和灵活的模板系统，**Nuclei** 能够模拟各种安全检查，而且它拥有一个由 **300** 多名安全研究人员和工程师贡献的各种类型漏洞模板的专门仓库。

以下是一个具体工作原理示意图：

![](https://raw.githubusercontent.com/projectdiscovery/nuclei/master/static/nuclei-flow.jpg)

###### 如何使用

安装 **Nuclei** 需要 **go1.21** 或更高版本，通过以下命令安装最新版本：

```sh
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

也可以通过 **Brew** 或 **Docker** 进行安装：

```sh
brew install nuclei

docker pull projectdiscovery/nuclei:latest
```

安装完成后，可以使用 `nuclei -h` 命令来查看工具的帮助信息，进而根据需求进行漏洞扫描。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240519230326294.png)

###### 项目推介

作为一个处于活跃开发状态并且不断迭代的项目，**Nuclei** 不仅吸引了 300 多名安全研究者和工程师的贡献，还因其高效、灵活和零误报的特点被许多企业和安全团队采用。该工具提供的丰富模板覆盖了多种漏洞类型，帮助用户轻松实现安全自动化检查。

![](https://raw.githubusercontent.com/projectdiscovery/nuclei/master/static/check-nuclei-documentation.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/projectdiscovery/nuclei 

开源项目作者：projectdiscovery

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=projectdiscovery/nuclei)

关注我们，一起探索有意思的开源项目。

