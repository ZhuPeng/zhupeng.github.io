---
layout: post
title: 开源云原生安全治理平台
tags: 安全
---

大家好，今天的文章来自读者的投稿。

HummerRisk 是开源的云原生安全治理平台，以非侵入的方式解决云原生的安全和治理问题。核心能力包括混合云的安全治理和 K8s 容器云安全检测。

![HummerRiskk](https://hummerrisk-1312321453.cos.ap-beijing.myqcloud.com/hummerrisk-github-banner.jpg)

HummerRisk 的功能包含**混合云安全治理**、**K8S 容器云安全**，接下来将依次介绍。

**混合云安全治理**

1、混合云安全合规检测：
对主流的公(私)有云资源进行安全合规检测，例如等保 2.0 预检、CIS 合规检查、各种基线检测，同时可自定义检测规则；

2、漏洞检测：
基于漏洞规则库，通过扫描等手段对指定的网络设备及应用服务的安全脆弱性进行检测；

3、合规报告：
一键获取合规报告，全面掌控安全态势。

4、操作审计： 统一对多云上的操作日志进行审计

![混合云安全合规](https://hummerrisk-1312321453.cos.ap-beijing.myqcloud.com/multicloud.png)

**K8S 容器云安全**

1、K8S 资源态势：
可以关联多个 K8S 集群，统一查看各个关联环境的资源态势；

2、环境检测：
根据 K8S 安全基线进行检测，发现存在的配置错误、安全漏洞、危险动作等内容；

3、镜像检测：
全面检测镜像相关的漏洞，包括操作系统、软件包、应用程序依赖等方面；

4、部署检测：
检测 K8S 的部署编排文件，在部署前发现其中的配置问题；

5、主机检测：
可以自定义检测内容，发现底层主机/虚机中存在问题。

6、源码检测：
检测开发者的源代码，提前发现其中的开源协议、依赖、漏洞、代码等问题；

7、SBOM 管理:
SBOM 的可视化管理和分析，检测 SBOM 的变更，快速发现和定位软件供应链中的风险和漏洞，给出合理的处理建议。

  ![K8S容器云安全](https://hummerrisk-1312321453.cos.ap-beijing.myqcloud.com/k8s.png)

**产品架构**

![产品架构](https://hummerrisk-1312321453.cos.ap-beijing.myqcloud.com/architecturev.png)

**优势是什么？**

1、支持全面: 支持的几乎所有公有云,尤其是中国的云厂商支持

2、容易上手: 只需绑定云账号，就可以一键执行检测

3、开箱即用: 大量内置检测规则，如 CIS 规则，等保2.0 规则等，同时支持自定义规则;

4、无侵入式：基于无侵入式的实现方式，快速上手，降低潜在风险;

5、独立性: 中立产品，不绑定任何云厂商



**项目预览**

![预览图](https://hummerrisk-1312321453.cos.ap-beijing.myqcloud.com/product-silde.gif)



**快速开始**  

仅需两步快速安装 HummerRisk：

1、准备一台不小于 4 核 8 G 内存的 64 位 Linux 主机；

2、以 root 用户执行如下命令一键安装 HummerRisk。

curl -sSL https://github.com/HummerRisk/HummerRisk/releases/latest/download/quick_start.sh | sh

更多项目详情请查看如下链接。

开源项目地址：https://github.com/HummerRisk/HummerRisk

开源项目团队：HummerRisk