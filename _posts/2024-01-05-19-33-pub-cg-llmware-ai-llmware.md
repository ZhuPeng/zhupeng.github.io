---
layout: post
title: 专为企业级大模型开发的框架、工具和模型
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的企业环境下，很多的公司都在落地大模型相关的应用。但是并不是每个公司都具备相应的专业大模型的人才，能够很好的处理大模型落地过程中碰到的问题。

今天要给大家推荐一个 GitHub 开源项目 llmware-ai/llmware，该项目在 GitHub 有超过 1.6k Star，用一句话介绍该项目就是：“Providing enterprise-grade LLM-based development framework, tools, and fine-tuned models.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224230037127.png)

###### 项目介绍

`llmware` 是一个专为企业级 LLM 开发的框架、工具和模型。该项目在私有云中将企业知识与 LLM 安全并有效地整合，以便于创建出专业的、基于知识的企业 LLM 应用。主要功能包括：

1、提供高性能的文档解析器以快速处理多种常用文档类型；

2、提供完整的直观的查询方法，如语义查询，文本查询以及混合查询；

3、支持人类参与评估、反馈和纠正 AI 的响应；

4、可灵活地分析和审核 LLM 提示生命周期，等等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224230151931.png)

此外，`llmware` 还提供快速开始使用增强型检索生成（RAG）的教程和视频，以便于让大家探索并掌握这个开源项目。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240224230213569.png)

###### 如何使用

`llmware` 的安装和使用十分方便，可以通过 `pip` 命令进行安装。

```bash
pip3 install llmware
```

对于 MongoDB 和 Milvus 的使用者，`llmware` 可以直接通过 Docker Compose 文件进行安装，以便于提供生产级的数据库和向量嵌入能力。安装完成后，只需引入 `llmware` 库即可开始编写代码。

```python
from llmware.models import ModelCatalog

ModelCatalog().get_llm_toolkit()  # get all SLIM models, delivered as small, fast quantized tools 
ModelCatalog().tool_test_run("slim-sentiment-tool") # see the model in action with test script included  
```

###### 项目推介

`llmware` 构建的框架由四大主要组件组成，可以满足全面而多元的业务需要。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=llmware-ai/llmware&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/llmware-ai/llmware 

开源项目作者：llmware-ai

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=llmware-ai/llmware)

关注我们，一起探索有意思的开源项目。

