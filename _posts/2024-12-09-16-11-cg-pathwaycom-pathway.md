---
layout: post
title: LLM 友好的实时数据流处理引擎
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数据分析和处理的工作中，我们面临着从实时分析到流处理、从长短期记忆（LLM）管道到关系型代数图（RAG）等多方面的挑战。数据的快速增长和需求的多样化，要求我们不断寻找更高效、更智能化的处理解决方案。尤其是在处理实时数据流和大规模机器学习模型时，如何有效地整合流数据和批数据处理、保证数据的一致性和准确性，以及如何在不牺牲开发效率的前提下实现高性能计算，成为了许多企业和开发者的核心痛点。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-1ddb52cbff33b93adbad269a69c180dd.png)

今天要给大家推荐一个 GitHub 开源项目 pathway，该项目在 GitHub 有超过 6.3k Star。

![](https://stats.deeptrain.net/repo/pathwaycom/pathway/?theme=light)

一句话介绍该项目：Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20241211000538237.png)

###### 项目介绍

Pathway 是一个基于 Python 的 ETL （提取、转换、加载）框架，专注于流处理、实时分析、LLM 管道和 RAG。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20241211000619586.png)

Pathway 的亮点在于它提供了易于使用的 Python API，允许开发者无缝集成他们喜爱的 Python 机器学习库，并且支持在开发和生产环境中有效处理批量和流数据。进一步地，Pathway 由一个基于差分数据流的可扩展 Rust 引擎驱动，使你的 Pathway 代码以 Rust 引擎运行，从而实现了多线程、多进程和分布式计算的能力。此外，整个管道都保持在内存中，并可以通过 Docker 和 Kubernetes 轻松部署。

![](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20241211000743236.png)











![](https://github.com/pathwaycom/pathway-benchmarks/raw/main/images/bm-wordcount-lineplot.png)



###### 如何使用

安装 Pathway 要求 Python 3.10 或以上版本，只需通过 pip 命令：

```
$ pip install -U pathway
```
以下是一个实时计算正值总和的简单示例，展示了 Pathway 的基本使用方法：
```python
import pathway as pw

class InputSchema(pw.Schema):
  value: int

input_table = pw.io.csv.read(
  "./input/",
  schema=InputSchema
)

filtered_table = input_table.filter(input_table.value >= 0)
result_table = filtered_table.reduce(
  sum_value = pw.reducers.sum(filtered_table.value)
)
pw.io.jsonlines.write(result_table, "output.jsonl")

# Run the computation
pw.run()
```
###### 项目推介

Pathway 项目以其独特的功能集、对开发者友好的接口和强大的性能表现，在业界脱颖而出。它适用于 MacOS 和 Linux 系统，拥有丰富的连接器、状态处理和持久性功能。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pathwaycom/pathway&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pathwaycom/pathway 

开源项目作者：pathwaycom

开源协议：Other

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pathwaycom/pathway)

关注我们，一起探索有意思的开源项目。

