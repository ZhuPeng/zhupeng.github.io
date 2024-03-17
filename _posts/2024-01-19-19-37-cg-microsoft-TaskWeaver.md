---
layout: post
title: 微软开源的数据分析任务处理系统
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数据分析领域，我们经常会遇到需要将多种数据分析任务无缝地计划和执行的挑战。这些任务可能涉及诸如查看和解析数据、运行算法、生成报告等复杂过程。由于这些任务经常需要从多个源获取和处理数据，如数据库、网页以及 API，因此我们需要一个既可高效协调任务，又可方便地整合各类功能的解决方案。此外，为了提高代码质量，我们也需要一个可以检查输出代码并提供修复建议的工具。

今天要给大家推荐一个 GitHub 开源项目 microsoft/TaskWeaver，该项目在 GitHub 有超过 3.2k Star，用一句话介绍该项目就是：A code-first agent framework for seamlessly planning and executing data analytics tasks. 

![](https://raw.githubusercontent.com/microsoft/TaskWeaver/master/./.asset/logo.color.svg)

###### 项目介绍

TaskWeaver 是一个依托于代码的代理框架，专门为无缝规划和执行数据分析任务而设计。本框架颠覆创新地运用了代码片段理解用户请求，并能有效地协同形如函数的各类插件，以有状态的方式完成数据分析任务。TaskWeaver 的亮点包括丰富的数据结构支持、自定义算法支持、专业知识引入、有状态的执行、代码验证、易用性、易调试、安全问题考虑以及易扩展性等特点。

以下是系统的处理流程图：

![](https://raw.githubusercontent.com/microsoft/TaskWeaver/master/./.asset/taskweaver_arch.png)

###### 如何使用

TaskWeaver 的安装需要 Python 3.10 以上版本。运行以下命令克隆代码仓库并安装所需组件：

```
git clone https://github.com/microsoft/TaskWeaver.git
cd TaskWeaver
pip install -r requirements.txt
```

然后，修改配置文件 `taskweaver_config.json`，以确定使用的 LLM（内置的语言模型），例如 OpenAI。

在配置完成后，运行以下命令开始 TaskWeaver：
```
python -m taskweaver -p ./project/
```

除了命令行操作外，TaskWeaver 还支持通过 WebUI 操作,也可以作为一个库导入到你的现有项目中。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240310224250888.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240310224300487.png)

###### 项目推介

TaskWeaver 是微软的开源项目，持续更新且活跃度高，还有不断添加的新功能，如视觉网络探索器插件，流媒体支持以及加入了各种 LLM ，如 LiteLLM、Ollama、Gemini、和 QWen 等。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=microsoft/TaskWeaver&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/microsoft/TaskWeaver 

开源项目作者：microsoft

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=microsoft/TaskWeaver)

关注我们，一起探索有意思的开源项目。

