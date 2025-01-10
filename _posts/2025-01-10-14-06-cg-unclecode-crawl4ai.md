---
layout: post
title: GitHub 开源项目 unclecode/crawl4ai 介绍，🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 unclecode/crawl4ai，该项目在 GitHub 有超过 23.7k Star。

![](https://stats.deeptrain.net/repo/unclecode/crawl4ai/?theme=light)

一句话介绍该项目：🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper





###### 项目介绍

### 背景介绍

在当今信息爆炸的时代，大量的数据被创建并存储在网页之中。从机器学习模型的训练到数据分析，获取准确且高质量的网络数据成为了科研人员、数据分析师以及算法工程师面临的挑战之一。然而，现有的网络爬虫工具往往在效率、定制性及对大型语言模型（LLM）友好性方面存在不足。这导致了对于需要高效率、高质量数据的开发者来说，数据采集变成了一个资源消耗大且困难重重的任务。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-52f42d6d3e65ebfec7478c783e16603a.png)

项目介绍

🚀🤖 **Crawl4AI** 是一个开源的、面向大型语言模型（LLM）友好的网络爬虫与数据抓取工具。它解决了现有工具在数据采集效率、定制性及对LLM支持不足等问题，提供了一个灵活、快速且易于部署的网络数据采集解决方案。Crawl4AI 主要功能包括：

- **LLMs 优化**：生成针对 RAG 和微调应用优化的简洁 Markdown，提高数据使用效率。
- **极速性能**：通过实时、成本高效的性能提供结果，速度是传统方法的 6 倍。
- **灵活的浏览器控制**：支持会话管理、代理以及自定义钩子，便于无缝访问数据。
- **智能提取**：采用高级算法高效提取数据，减少对成本高昂模型的依赖。
- **开源且易于部署**：完全开源，无需 API 密钥，支持 Docker 和云集成。
- **活跃的社区支持**：由一个充满活力的社区维护，并成为 GitHub 上的 #1 趋势项目。

### 如何使用

#### 安装 Crawl4AI

```bash
pip install -U crawl4ai
crawl4ai-setup
crawl4ai-doctor
```

如果遇到任何与浏览器相关的问题，可以手动安装它们：

```bash
python -m playwright install --with-deps chromium
```

#### 运行一个简单的网络爬取任务

```python
import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.nbcnews.com/business",
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
```

### 项目推介

**Crawl4AI** 不仅仅因为其强大的功能受到开发者的青睐，它还因为以下特点而受到推荐：

- **高活跃的开发状态**：作为 **GitHub** 上的 #1 趋势项目，Crawl4AI 拥有持续更新和维护的代码库，保证了工具的先进性和稳定性。
- **强大的社区支持**：一个充满活力的社区不断为项目贡献代码和提供支持，使得新用户可以容易地上手和解决遇到的问题。
- **广泛的应用场景**：从科研数据收集到商业竞争分析，Crawl4AI 的灵活设计使其适用于各种需要高效准确网络数据采集的场景。
- **知名公司和机构的使用**：该项目已经被多家知名公司和机构采用，在业内获得了广泛的认可和使用。

综合上述优势，Crawl4AI 成为了那些寻找

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=unclecode/crawl4ai&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/unclecode/crawl4ai 

开源项目作者：unclecode

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=unclecode/crawl4ai)

关注我们，一起探索有意思的开源项目。

