---
layout: post
title: 学生党打工人的福音，对任意主题自动化生成调研报告
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现今信息爆炸的社会中，寻找、筛选和了解关于某一话题的全面细致信息变得日益困难。手动研究任务需要花费大量时间找到合适的资源和信息，有时可能要持续数周。此外，目前的 LLMs（大语言模型）训练的都是过时信息，存在严重的产生错误记忆的风险，这使得它们在研究任务中用处比较有限。像 ChatGPT + Web 插件这样具有网络搜索功能的解决方案，仅考虑了有限的资源和内容，有可能结果表面化，甚至带有偏见。

今天要给大家推荐一个 GitHub 开源项目 assafelovic/gpt-researcher，该项目在 GitHub 有超过 6.2k Star，用一句话介绍该项目就是：“GPT based autonomous agent that does online comprehensive research on any given topic”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240219220432856.png)

###### 项目介绍

GPT Researcher 是一个由 GPT 开发的自动代理，专门用于对各种任务进行全面的在线研究。这个代理可以产生详细的、客观的、无偏见的研究报告，还提供选项用于关注相关的资源、概括和课程。GPT Researcher 以并行化的方式高效完成任务，不同于同步操作，可以提供更稳定的性能和更高的速度。本项目的使命是利用人工智能的力量，为个人和组织提供准确、无偏见、事实的信息。

以下是系统的工作流程图：

![](https://cowriter-images.s3.amazonaws.com/architecture.png)

###### 如何使用

首先需要安装 Python 3.11 或更高版本，然后通过以下命令下载项目并安装依赖项：

```bash
git clone https://github.com/assafelovic/gpt-researcher.git
cd gpt-researcher
pip install -r requirements.txt
```
然后在 .env 文件中创建您的 OpenAI Key 和 Tavily API key，或者只需将其导出：
```bash
export OPENAI_API_KEY={Your OpenAI API Key here}
export TAVILY_API_KEY={Your Tavily API Key here}
```
在配置了环境和安装了依赖项后，您就可以使用 GPT Researcher 了。GPT Researcher 的平均研究任务耗时大约 3 分钟，费用约 0.1 美元。

以下是一个示例 DEMO：

<video src="/Users/zhupeng/Downloads/252265342-a00c89a6-a295-4dd0-b58d-098a31c40fda.mp4"></video>
###### 项目推介

GPT Researcher 是一个非常实用的工具，可以根据每个生成的研究问题来寻找最相关的信息，然后过滤和聚合所有相关信息并创建一个研究报告。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=assafelovic/gpt-researcher&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/assafelovic/gpt-researcher 

开源项目作者：assafelovic

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=assafelovic/gpt-researcher)

关注我们，一起探索有意思的开源项目。

