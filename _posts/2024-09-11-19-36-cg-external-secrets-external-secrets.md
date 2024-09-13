---
layout: post
title: GitHub 开源项目 external-secrets/external-secrets 介绍，External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 external-secrets/external-secrets，该项目在 GitHub 有超过 4.3k Star。

![](https://stats.deeptrain.net/repo/external-secrets/external-secrets/?theme=light)

一句话介绍该项目：External Secrets Operator reads information from a third-party service like AWS Secrets Manager and automatically injects the values as Kubernetes Secrets.




![](https://raw.githubusercontent.com/external-secrets/external-secrets/master/assets/Godaddylogo_2020.png)

![External Secrets Inc.](https://raw.githubusercontent.com/external-secrets/external-secrets/master/assets/ESI_Logo.svg)

![Container Solutions](https://raw.githubusercontent.com/external-secrets/external-secrets/master/assets/CS_logo_1.png)

![Form 3](https://raw.githubusercontent.com/external-secrets/external-secrets/master/assets/form3_logo.png)

![Pento ](https://raw.githubusercontent.com/external-secrets/external-secrets/master/assets/pento_logo.png)

![](https://raw.githubusercontent.com/external-secrets/external-secrets/master/assets/eso-logo-large.png)


###### 项目介绍

### **外部秘密操作员：自动化 Kubernetes 秘密管理的未来**

#### **背景介绍**
在当今云原生的开发环境中，安全地管理敏感信息，如数据库密码、API 密钥或证书，已成为开发与运维团队面临的一个重要挑战。一般而言，这些秘密信息需要被频繁地更新和管理，以避免潜在的安全风险。然而，手动管理这些秘密往往既繁琐又容易出错，尤其是在复杂的多云或混合云环境中。Kubernetes 作为当前最流行的容器编排工具，虽提供了秘密管理的基础能力，但在与多个外部秘密管理系统结合时，仍缺乏足够的灵活性和扩展性。

#### **

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-2278e5fe8569a1729a5cd029eaf00acf.png)

项目介绍**
**外部秘密操作员（External Secrets Operator）** 是一个能够集成多个外部秘密管理系统（如 AWS Secrets Manager、HashiCorp Vault、Google Secrets Manager 等）到 Kubernetes 环境中的操作员。此项目的核心功能是自动从这些外部系统中读取秘密信息，并将其注入到 Kubernetes Secrets 中，从而极大地简化了在 Kubernetes 环境下的秘密管理工作。通过这种方式，开发与运维团队可以在一个统一的平台上管理所有秘密，同时保持秘密的安全性和一致性。

此外，**外部秘密操作员** 支持广泛的秘密管理系统，使其能够满足不同组织的具体需求。项目还非常重视社区贡献，并且积极鼓励开发者加入其开发。通过不断的迭代和改进，该项目旨在为云原生应用提供一个稳定、安全、高效的秘密管理解决方案。

#### **如何使用**
**外部秘密操作员** 的安装与使用都十分直接。首先，需要在 Kubernetes 集群上安装该操作员。项目的官方文档提供了详细的安装指南。安装完成后，用户只需根据需要配置外部秘密源即可开始自动同步秘密。

一个简单的使用示例可能如下：
1. 安装 **外部秘密操作员** 到您的 Kubernetes 集群。
2. 配置一个外部秘密提供者，如 AWS Secrets Manager。
3. 定义一个 `ExternalSecret` 资源，指定要同步的秘密以及同步目标。
4. **外部秘密操作员** 会自动监视这些配置，并将外部秘密同步到 Kubernetes Secrets 中。

该过程实现了对秘密的集中管理和自动同步，极大提升了工作效率和安全性。

#### **项目推介**
**外部秘密操作员** 不仅拥有健壮的社区支持，而且多家知名企业已开始采用此项目来管理其秘密。该项目由一支活跃的开发团队维护，且定期发布更新和改进。它的设计考虑了当前云原生应用的秘密管理需求，使其成为了构建安全、可靠的云原生应用的理想选择。

此外，与许多其他开源项目一样，**外部秘密操作员** 强调社区贡献的重要性，并鼓励开发者参与到项目的开发中来。无论是通过代码贡献、提供反馈，还是参与双周开发会议，每一个贡献

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=external-secrets/external-secrets&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/external-secrets/external-secrets 

开源项目作者：external-secrets

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=external-secrets/external-secrets)

关注我们，一起探索有意思的开源项目。

