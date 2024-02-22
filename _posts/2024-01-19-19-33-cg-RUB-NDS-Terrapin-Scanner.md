---
layout: post
title: GitHub 开源项目 RUB-NDS/Terrapin-Scanner 介绍，This repository contains a simple vulnerability scanner for the Terrapin attack present in the paper "Terrapin Attack: Breaking SSH Channel Integrity By Sequence Number Manipulation".
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 RUB-NDS/Terrapin-Scanner，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“This repository contains a simple vulnerability scanner for the Terrapin attack present in the paper "Terrapin Attack: Breaking SSH Channel Integrity By Sequence Number Manipulation".”。





背景介绍：
在计算机网络安全上，SSH（安全外壳）协议是一种应用广泛的安全协议，其主要用于提供加密的网络服务。但是，SSH 协议可能存在 “Terrapin 攻击” 的安全漏洞，该漏洞主要借由序列号操作，破坏 SSH 频道的完整性。你可能尝试过手动检查 SSH 客户端或服务器的安全性，但是往往耗时且无法准确判断安全状态。因此，如何高效且准确地识别 SSH 客户端或服务器的潜在风险，是大部分安全和网络工程师需要面临的问题。

项目介绍：
Terrapin Vulnerability Scanner 是一个用 Go 写的小工具，能够准确快速地判断 SSH 客户端或服务器是否存在 “Terrapin 攻击” 的安全漏洞。这个工具并不实际执行 SSH 密钥交换，也不尝试在服务器上进行认证，更不会实际执行攻击。而是通过检查支持的算法和已知防御措施（严格的密钥交换）来判断 SSH 是否存在安全漏洞。这使得判断结果百分之百准确，因为如果服务器支持了此工具未知的防御措施，可能会误判为存在漏洞。

如何使用：
Terrapin Vulnerability Scanner 提供了预编译的二进制文件，无需自行编译，可以在 [Release page](https://github.com/RUB-NDS/Terrapin-Scanner/releases/latest) 页面获取。你也可以使用我们提供的 Docker 镜像快速运行此工具，命令如下：

```bash
docker run --rm -it ghcr.io/rub-nds/terrapin-scanner
```

但如果你更喜欢自行编译，确保你已经安装了 Go v1.18，执行以下命令即可，

```bash
go install github.com/RUB-NDS/Terrapin-Scanner@latest
```

详细的使用示例在项目的 README 中有详细介绍，你可以根据需要进行参数设置。

项目推介：
Terrapin Vulnerability Scanner 项目是由知名的德国波鸿大学的网络和数据安全实验室 (RUB-NDS) 开发并维护。项目活跃度高，且作者积极解答使用中遇到的问题，可以说是非常适用于对 SSH 安全性有高要求的工程师们。如果你在寻找一个可以便捷、高效识别 SSH “Terrapin 攻击”漏洞的工具，那么 Terrapin Vulnerability Scanner 就是你的最佳选择。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=RUB-NDS/Terrapin-Scanner&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/RUB-NDS/Terrapin-Scanner 

开源项目作者：RUB-NDS

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=RUB-NDS/Terrapin-Scanner)

关注我们，一起探索有意思的开源项目。

