---
layout: post
title: k8sgpt - Kubernetes 集群智能扫描和诊断工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在 Kubernetes 集群中，由于集群规模庞大，存在大量的资源和配置，因此很容易出现问题。而解决这些问题需要具备专业的知识和经验，对于普通用户来说是一项挑战。k8sgpt 项目的出现就是为了解决这个问题，它是一个基于自然语言处理和人工智能技术的 Kubernetes 集群扫描和诊断工具，能够以简单易懂的方式诊断和解决 Kubernetes 集群中的问题。

k8sgpt 项目在 GitHub 有超过 3.1k Star，用一句话介绍该项目就是：“Giving Kubernetes Superpowers to everyone”。

![](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/master/./images/banner-black.png)
使用示例如下：

![](https://raw.githubusercontent.com/k8sgpt-ai/k8sgpt/master/images/demo4.gif)

###### 项目介绍

k8sgpt 是一个 Kubernetes 集群扫描和诊断工具，能够以自然语言的方式诊断和解决 Kubernetes 集群中的问题。它通过将 SRE 经验编码到分析器中，能够提取最相关的信息，并通过 AI 技术进行丰富。k8sgpt 内置了多个分析器，如 podAnalyzer、pvcAnalyzer、rsAnalyzer、serviceAnalyzer、eventAnalyzer、ingressAnalyzer、statefulSetAnalyzer 等，能够帮助用户快速诊断和解决问题。此外，k8sgpt 还支持自定义分析器，用户可以根据自己的需求编写自己的分析器。

核心功能如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230826202647550.png)

###### 如何使用

k8sgpt 可以通过以下方式进行安装：

- Linux/Mac：使用 brew 安装

```bash
brew tap k8sgpt-ai/k8sgpt
brew install k8sgpt
```

- RPM-based（RedHat/CentOS/Fedora）：使用 rpm 安装

```bash
curl -LO https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.3.14/k8sgpt_386.rpm
sudo rpm -ivh k8sgpt_386.rpm
```

- DEB-based（Ubuntu/Debian）：使用 dpkg 安装

```bash
# 32 bit
curl -LO https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.3.14/k8sgpt_386.deb
sudo dpkg -i k8sgpt_386.deb

# 64 bit
curl -LO https://github.com/k8sgpt-ai/k8sgpt/releases/download/v0.3.14/k8sgpt_amd64.deb
sudo dpkg -i k8sgpt_amd64.deb
```

- APK-based（Alpine）：使用 apk 安装
- Windows：下载最新的 Windows 二进制文件并配置系统路径变量

安装完成后，用户可以通过以下命令使用 k8sgpt：
- k8sgpt generate：生成 OpenAI API 密钥
- k8sgpt auth add：设置 API 密钥
- k8sgpt filters：管理分析器的活动过滤器
- k8sgpt analyze：运行扫描
- k8sgpt analyze --explain：获取更详细的问题解释
- k8sgpt analyze --with-doc：获取 Kubernetes 的官方文档

详细命令解释如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230826202950257.png)

###### 项目推介

k8sgpt 是一个非常优秀的 Kubernetes 集群扫描和诊断工具，它的开发活跃度很高，已经获得了很多用户的认可和好评。此外，k8sgpt 还获得了业内知名人士的推荐，被广泛应用于生产环境中。如果你正在使用 Kubernetes 并且希望更好地管理和维护你的集群，那么 k8sgpt 绝对是一个值得尝试的工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=k8sgpt-ai/k8sgpt&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/k8sgpt-ai/k8sgpt 

开源项目作者：k8sgpt-ai

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=k8sgpt-ai/k8sgpt)

关注我们，一起探索有意思的开源项目。

