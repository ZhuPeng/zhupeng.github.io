---
layout: post
title: GitHub 开源项目 GoogleCloudPlatform/terraformer 介绍，CLI tool to generate terraform files from existing infrastructure (reverse Terraform). Infrastructure to Code
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 GoogleCloudPlatform/terraformer，该项目在 GitHub 有超过 12.8k Star。

![](https://stats.deeptrain.net/repo/GoogleCloudPlatform/terraformer/?theme=light)

一句话介绍该项目：CLI tool to generate terraform files from existing infrastructure (reverse Terraform). Infrastructure to Code




![Waze SRE logo](https://raw.githubusercontent.com/GoogleCloudPlatform/terraformer/master/assets/waze-sre-logo.png)

![asciicast](https://asciinema.org/a/243961.svg)


###### 项目介绍

### Terraformer：基础设施反向生成 Terraform 代码的神器

#### 背景介绍

随着云计算的兴起，越来越多的企业将他们的服务部署在云上，依赖于不同云服务商提供的各式各样的资源。在这个过程中，基础设施即代码（Infrastructure as Code，IaC）成为了一个趋势，它允许开发者使用代码的形式来管理和配置基础设施，使得基础设施的建设、管理变得更加自动化和可控。而 Terraform 作为市场上领先的 IaC 工具之一，支持多种云服务商，让基础设施的部署变得简单。

然而，当涉及到已经存在的老旧基础设施，或是需要从一个云服务转移到另一个时，如何快速、准确地把现有的基础设施转换为 Terraform 代码，成为了一个实际问题。手工编写 Terraform 代码不仅耗时耗力，还极易出错。因此，一个能够自动将现有基础设施转化为 Terraform 代码的工具，是云基础设施管理中不可或缺的。

#### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-9fdcf6535dac17efd25b728cac4650bb.png)

项目介绍

Terraformer 是一个命令行工具，能够基于现有的基础设施生成 `tf`/`json` 和 `tfstate` 文件，实现从基础设施到 Terraform 代码的自动反向生成。这意味着，使用 Terraformer，可以轻松地将任何支持的云服务商的当前云资源状态导出为 Terraform 配置文件，极大地简化了基础设施代码化的流程。

Terraformer 支持主流的云提供商，包括但不限于 Google Cloud、AWS、Azure、AliCloud 和 IBM Cloud，同时也支持了诸如 Kubernetes、Cloudflare、GitHub 等多种基础设施软件和服务。其设计充分利用了 Terraform 提供者，可以轻松地添加支持新资源的能力，以及通过升级 Terraform 提供者来增加资源的新字段。

#### 如何使用

1. **安装 Terraformer**

   Terraformer 可以通过几种方法安装，例如使用 Homebrew 对于 macOS 用户：

   ```bash
   brew tap GoogleCloudPlatform/terraformer
   brew install terraformer
   ```

2. **使用示例**

   假设要从 Google Cloud Platform 导入所有资源，可以使用以下命令：

   ```bash
   terraformer import google --resources=* --projects=<你的GCP项目ID> --regions=<地区>
   ```

   对于 AWS，如果希望仅导入特定的 VPC 和相关的安全组，可以使用：

   ```bash
   terraformer import aws -r sg,vpc --filter Type=sg;Name=vpc_id;Value=<VPC_ID> --filter Type=vpc;Name=id;Value=<VPC_ID>
   ```

#### 项目推介

自从 Terraformer 在 GitHub 上开源以来，它已经吸引了大量的关注和使用。由 Waze 的 SRE 团队创建，这个项目不仅获得了 GoogleCloudPlatform 的官方支持，而且有着持续活跃的开发状态和日益增长的社区。

由于它强大的功能和简单的使用方式，Terraformer 已被众多公司和开发者所采用，以帮助他们快速地从现有的基础设施迁移到使用 Terraform 管理。不论你是需要迁移云基础设施，还是希望将你的基础设施代码化，Terraformer 都是一个不可或缺的工具。

总的来说，

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=GoogleCloudPlatform/terraformer&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/GoogleCloudPlatform/terraformer 

开源项目作者：GoogleCloudPlatform

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=GoogleCloudPlatform/terraformer)

关注我们，一起探索有意思的开源项目。

