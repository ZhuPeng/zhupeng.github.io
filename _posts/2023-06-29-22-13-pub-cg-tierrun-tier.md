---
layout: post
title: Tier - 给你的SaaS应用添加定价的最简单方式
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

## 1. 背景介绍

在构建和管理SaaS应用的过程中，定价模型是一个重要的方面。然而，传统的定价方法往往复杂而繁琐，难以管理。Tier是一个解决方案，它提供了一个简单、集中的方式来定义和管理你的SaaS应用的定价模型。通过Tier，你可以轻松解决与定价相关的问题，从而将注意力集中在核心业务上。

Tier 项目在 GitHub 有 600+  Star，用一句话介绍该项目就是：“The easiest way to add pricing to your SaaS. Get billing over with.”。

![](https://uploads-ssl.webflow.com/61e0906dfb20ab2b1c79f6af/638e175ae356c54fe57a7579_IMG_8588.png)

## 2. 项目介绍
Tier是一个能够让你在一个地方定义和管理SaaS应用的定价模型的工具。它的主要目标是帮助SaaS和基于消费模型的计费模型更加友好地使用和管理Stripe。Tier提供了SDK来实现访问检查、计量/报告等功能。

主要功能和设计要点：
- 在一个地方管理你的功能、计划以及它们的定价
- 提供按需测试环境和预览部署，让你安心地进行开发
- 根据特定客户或测试的需要创建自定义计划和变体
- Tier会自动与Stripe保持同步并进行全面管理
- 访问检查和授权由Tier的SDK处理

![](https://uploads-ssl.webflow.com/61e0906dfb20ab2b1c79f6af/637c39698d3ba183d982e32a_Screenshot%202022-11-21%20at%2010.43.54%20PM.png)

## 3. 如何使用
你可以按照以下步骤安装和使用Tier：

1. 安装Tier CLI：使用以下命令来安装（适用于Homebrew、Binary和Go）：
   - Homebrew（macOS）：`brew install tierrun/tap/tier`
   - Binary（macOS、Linux、Windows）：https://tier.run/releases
   - Go：运行以下命令（需要go1.19或更高版本）：
     ```
     go run tier.run/cmd/tier@latest
     ```
     或者
     ```
     go install tier.run/cmd/tier@latest
     ```

2. 创建你的第一个`pricing.json`文件：你可以在[Tier Model](https://model.tier.run)上创建并使用`tier push`命令推送到你的开发环境或生产环境。

3. 添加Tier SDK：通过访问[Tier SDK文档](https://www.tier.run/docs/sdk/)，获取并添加Tier SDK来启用访问检查和计量功能。

你可以在Tier Hello World (https://blog.tier.run/tier-hello-world-demo) 中找到一个示例。以下是一个 pricing.json 的示例：

```json
{
  "plans": {
    "plan:free@1": {
      "title": "Convert (free)",
      "features": {
        "feature:convert": {
          "title": "Temperature Conversions",
          "tiers": [
            {
              "upto": 10,
              "price": 0
            }
          ]
        }
      }
    },
    "plan:pro@1": {
      "title": "Convert (Pro)",
      "features": {
        "feature:convert": {
          "title": "Temperature Conversions",
          "tiers": [
            {
              "base": 1000,
              "price": 0,
              "upto": 100
            },
            {
              "price": 1
            }
          ]
        }
      }
    }
  }
}
```

## 4. 项目推介
为什么要选择Tier？以下是一些推荐理由：
- 开发活跃：Tier是一个活跃的开源项目，持续得到维护和改进。
- 知名用户/公司：许多知名的用户和公司已经在使用Tier来管理他们的SaaS应用的定价模型。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tierrun/tier&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tierrun/tier 

开源项目作者：tierrun

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tierrun/tier)

关注我们，一起探索有意思的开源项目。

