---
layout: post
title: GitHub 开源项目 ComposioHQ/composio 介绍，Composio equip's your AI agents & LLMs with 100+ high-quality integrations via function calling
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 ComposioHQ/composio，该项目在 GitHub 有超过 13.7k Star。

![](https://stats.deeptrain.net/repo/ComposioHQ/composio/?theme=light)

一句话介绍该项目：Composio equip's your AI agents & LLMs with 100+ high-quality integrations via function calling




![](https://raw.githubusercontent.com/ComposioHQ/composio/master/./python/docs/imgs/follow_x.png)

![](https://raw.githubusercontent.com/ComposioHQ/composio/master/./python/docs/imgs/try_hosted.png)

![](https://raw.githubusercontent.com/ComposioHQ/composio/master/./python/docs/imgs/composio_white_font.svg)

![](https://raw.githubusercontent.com/ComposioHQ/composio/master/./python/docs/imgs/composio_black_font.svg)

![](https://raw.githubusercontent.com/ComposioHQ/composio/master/./python/docs/imgs/banner.gif)

![](https://contributors-img.web.app/image?repo=composiodev/composio)


###### 项目介绍

背景介绍：在快速演进的人工智能领域中，为 AI 代理或大型语言模型（LLMs）拓展功能、接入多样化的第三方服务成为了一个显著的需求。开发者面临的主要挑战包括处理复杂的认证流程、维护与第三方服务的稳定性及数据准确性等。同时，为了提高 AI 应用的灵活性与实用性，开发者需不断地探索与集成新工具，这一过程往往耗时耗力。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0448e73d5e402cb4601bf1c922565aaa.png)

项目介绍：针对上述挑战，GitHub 上的 Composio 项目提供了一站式解决方案。Composio 装备您的 AI 代理和大型语言模型（LLMs）通过函数调用方式，接入 100+ 高质量的第三方服务。它覆盖了软件管理、操作系统指令、浏览器操作、搜索引擎、软件工程工具以及实时信息检索等多个领域。Composio 的关键设计要点包括对主流 AI 框架的支持、统一的认证管理、高度的数据处理准确性，以及易于扩展的插件系统。这些特性简化了开发过程，让开发者可以专注于构建更加智能和实用的 AI 应用。

如何使用：
- Python 安装：
```bash
pip install composio-core
```
- Python 示例，用 Composio 让 AI 代理对 GitHub 仓库进行标星：
```python
from openai import OpenAI
from composio_openai import ComposioToolSet, App, Action

openai_client = OpenAI(
    api_key="{{OPENAIKEY}}"
)

composio_tool_set = ComposioToolSet()
actions = composio_tool_set.get_actions(
    actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER]
)
# 这里省略了部分详细代码，具体的使用方法请参考 GitHub 上的文档。
```
- Javascript 安装：
```bash
npm install composio-core
```
- Javascript 示例，配置 OpenAI 和 Composio 工具集：
```javascript
import { OpenAI } from "openai";
import { OpenAIToolSet } from "composio-core";
// 这里省略了部分详细代码，具体的使用方法请参考 GitHub 上的文档。
```

项目推介：Composio 自发布以来，凭借其生产就绪的工具集、丰富的集成选项以及易用性，已经吸引了不少开发者的关注和使用。其活跃的开发状态，频繁的更新，以及广受好评的社区支持，都证明了这是一个值得投入的项目。更重要的是，Composio 有助于大幅度提升 AI 应用的开发效率和应用场景的广度，使得开发者可以更轻松地为 AI 代理装备上强大的工具和服务。无论您是 AI 领域的初学者还是经验丰富的开发者，Composio 都值得您的尝试和关注。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=ComposioHQ/composio&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ComposioHQ/composio 

开源项目作者：ComposioHQ

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=ComposioHQ/composio)

关注我们，一起探索有意思的开源项目。

