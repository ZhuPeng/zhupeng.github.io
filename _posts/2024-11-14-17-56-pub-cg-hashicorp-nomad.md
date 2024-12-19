---
layout: post
title: 易用灵活的工作负载编排器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

开发者们需要在不断变化的环境中部署和管理各种应用。这包括容器化应用、批处理任务、传统非容器化应用，甚至虚拟机。这种多样化的需求带来了显著的挑战：如何简化操作、提高性能、同时保证系统的灵活性和可扩展性？面对在本地、云环境或是混合环境中大规模地部署和管理不同种类的工作负载，开发者和企业需要一个统一的解决方案以降低复杂性和成本。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-384f372b0a58f85e5e59164e701bd674.png)

今天要给大家推荐一个 GitHub 开源项目 nomad，该项目在 GitHub 有超过 15k Star。

![](https://stats.deeptrain.net/repo/hashicorp/nomad/?theme=light)

一句话介绍该项目：Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations.


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241114233123730.png)


###### 项目介绍

Nomad 是一个易用、灵活且性能卓越的工作负载编排器，由 HashiCorp 开发。它能够跨不同的平台（Linux、Windows 和 macOS）部署和管理混合微服务、批处理、容器化及非容器化应用。作为一个单一二进制的软件，Nomad 自成体系，并集资源管理和调度于一身，无需外部存储或协调服务。它通过插件式的任务驱动器支持部署容器和传统应用，直接使用设备插件及 GPU 支持来提升对工作负载如机器学习（ML）和人工智能（AI）的处理能力。此外，Nomad 支持多区域、多云联合部署，并已在生产环境证明可扩展至超过 10K+ 节点。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241114233133820.png)

###### 如何使用

1、测试：可以访问 [Developer: Getting Started](https://developer.hashicorp.com/nomad/tutorials/get-started) 页面，遵循指导在本地设置一个非生产用的 Nomad 集群。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241114233340286.png)

2、生产：为了在生产环境中部署，建议阅读 [Developer: Nomad Reference Architecture](https://developer.hashicorp.com/nomad/tutorials/enterprise/production-reference-architecture-vm-with-consul) 获取推荐实践和生产部署的参考架构。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241114233400153.png)

###### 项目推介

Nomad 由知名的 HashiCorp 公司开发的解决方案，与 Terraform、Consul、Vault 等产品无缝集成，为开发人员提供全面的云基础架构自动化工具。HashiCorp 以其高质量的开源项目和强大的企业级功能而闻名，而 Nomad 也不例外。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241114233449928.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=hashicorp/nomad&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/hashicorp/nomad 

开源项目作者：hashicorp

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=hashicorp/nomad)

关注我们，一起探索有意思的开源项目。

