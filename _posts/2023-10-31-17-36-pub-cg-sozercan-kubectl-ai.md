---
layout: post
title: kubectl-ai - 快速生成并 Kubernetes manifests 的 AI 应用
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常的开发和测试过程中，我们常常需要找到并收集各种 Kubernetes manifests，这个过程既繁琐又耗时。而且，由于 Kubernetes 的复杂性，我们往往需要花费大量的时间和精力去理解和编写这些 manifests，这非常影响日常的开发和测试的效率。

今天要给大家推荐一个 GitHub 开源项目 sozercan/kubectl-ai，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“Kubectl plugin for OpenAI GPT”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104235239217.png)

###### 项目介绍

kubectl-ai 是一个基于 OpenAI GPT 的 kubectl 插件，它可以帮助我们生成并应用 Kubernetes manifests。这个项目的主要功能就是通过 OpenAI GPT 来自动生成 Kubernetes manifests，从而避免了我们手动查找和收集 manifests 的麻烦。此外，kubectl-ai 还支持通过环境变量来配置 OpenAI API key、Azure OpenAI Service API key 和 endpoint 以及 Local AI，使得我们可以根据实际需求来选择使用哪种 AI 服务。

###### 如何使用

kubectl-ai 的安装非常简单，我们可以通过 Homebrew、Krew 或者直接从 GitHub release 下载二进制文件来进行安装。安装完成后，我们需要配置一些环境变量，比如 OpenAI API key、Azure OpenAI Service API key 和 endpoint 以及 Local AI。然后，我们就可以开始使用 kubectl-ai 来生成和应用 Kubernetes manifests 了。

以下是一个详细的使用 DEMO（https://asciinema.org/a/MEXrlAqUjo7DMnfoyQearpVQ7）：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/kubectl-ai.gif)

此外，kubectl-ai 还提供了一些标志和环境变量，比如 --require-confirmation、--temperature、--use-k8s-api 和 --k8s-openapi-url，我们可以通过这些标志和环境变量来定制 kubectl-ai 的行为。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104235530630.png)

默认 AI 生成后的 manifests 可以通过选项确认后续的操作，可通过参数 --require-confirmation 关闭对应的命令确认。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104235703984.png)

###### 项目推介

kubectl-ai 的作者是在微软工作的知名的开发者 sozercan，已经在 GitHub 开源了多个项目。如果你正在寻找一个可以帮助你自动生成 Kubernetes manifests 的工具，那么 kubectl-ai 无疑是一个非常好的选择。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231104235911289.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sozercan/kubectl-ai&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/sozercan/kubectl-ai 

开源项目作者：sozercan

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sozercan/kubectl-ai)

关注我们，一起探索有意思的开源项目。

