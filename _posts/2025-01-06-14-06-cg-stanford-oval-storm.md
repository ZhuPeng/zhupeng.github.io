---
layout: post
title: GitHub 开源项目 stanford-oval/storm 介绍，An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 stanford-oval/storm，该项目在 GitHub 有超过 17.8k Star。

![](https://stats.deeptrain.net/repo/stanford-oval/storm/?theme=light)

一句话介绍该项目：An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations.




![](https://raw.githubusercontent.com/stanford-oval/storm/master/assets/logo.svg)

![](https://raw.githubusercontent.com/stanford-oval/storm/master/assets/overview.svg)

![](https://raw.githubusercontent.com/stanford-oval/storm/master/assets/two_stages.jpg)

![](https://raw.githubusercontent.com/stanford-oval/storm/master/assets/co-storm-workflow.jpg)


###### 项目介绍

### 背景介绍

在知识探索和研究领域，面临的一个主要挑战是从互联网上海量的信息中提取和整合知识，以生成有价值的、全面细致的报告。无论是学术研究、市场分析还是兴趣探索，人们往往需要耗费大量时间在预研阶段：从网上查找资料、阅读相关文档、整理和验证信息等，这个过程既费时又需要高度的专注和专业知识，对于大多数人来说是一个巨大的挑战，尤其是当需要深入了解一个全新主题时。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-010d57104ff88a30287ee45c78a85518.png)

项目介绍

**STORM** （Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking）和 **Co-STORM** 是由斯坦福大学 Oval 团队开发的一种基于大型语言模型（LLM）技术的知识整合系统，能够针对给定主题进行深度研究，并生成带有引用的全篇报告。这一系统解决了传统知识探索中的痛点：自动化地进行互联网研究，减少了手动搜集和整理信息的需求。

STORM 通过 **Pre-writing 和 Writing** 两个阶段，对生成长篇带引用文章的过程进行了优化。首先，系统会进行互联网研究，收集引用并生成大纲；然后，基于这些大纲和引用信息生成完整的文章。

Co-STORM 在 STORM 的基础上加入了人工智能合作元素，通过 **协同话语协议** 支持人机之间的流畅协作，进一步提升信息搜集和知识整理的效率和质量。

### 如何使用

1. 安装 knowledge-storm 库：

    ```shell
    pip install knowledge-storm
    ```

2. 若需要从源代码级别进行定制化开发，可以克隆仓库并安装依赖：

    ```shell
    git clone https://github.com/stanford-oval/storm.git
    cd storm
    conda create -n storm python=3.11
    conda activate storm
    pip install -r requirements.txt
    ```

此外，STORM 和 Co-STORM 支持多种语言模型和搜索引擎/检索模块的集成，为开发者在定制化功能和应用上提供了极高的灵活性和便利。

### 项目推介

STORM 和 Co-STORM 已经吸引了超过 70,000 人次的尝试使用，并在 2024 年的 NAACL 会议上进行了展示。这一开源项目得到了学术界和技术界的广泛关注和认可。它不仅在技术实现上展现了创新，在人工智能和知识管理领域的应用潜力也得到了业内专家的高度评价，特别是对于那些需要处理大量信息和进行深入研究的专业人士来说，STORM 提供了一个高效、便捷的解决方案。

无论是学术研究人员、内容创作者还是企业分析师，在面临复杂的信息收集和报告编写任务时，STORM 和 Co-STORM 都是值得尝试和使用的强有力工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stanford-oval/storm&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stanford-oval/storm 

开源项目作者：stanford-oval

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stanford-oval/storm)

关注我们，一起探索有意思的开源项目。

