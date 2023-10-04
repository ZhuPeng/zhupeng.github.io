---
layout: post
title: MetaGPT - 一个多智能体元编程框架，AI 打造的软件外包公司
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在软件开发过程中，我们常常面临着复杂任务的处理和多人的协作问题。如何将不同的 GPT 模型分配给不同的角色，并形成一个协作的软件实体，成为我们需要解决的核心问题。这个问题涉及到从一个简短的需求描述中生成产品文档、架构设计、任务列表、代码等多个方面，具有较高的细节和复杂度。

今天要给大家推荐一个 GitHub 开源项目 geekan/MetaGPT，该项目在 GitHub 有超过 1.2k Star，用一句话介绍该项目就是：“The Multi-Agent Meta Programming Framework: Given one line Requirement, return PRD, Design, Tasks, Repo | 多智能体元编程框架：给定老板需求，输出产品文档、架构设计、任务列表、代码”。

![](https://raw.githubusercontent.com/geekan/MetaGPT/master/docs/resources/MetaGPT-logo.jpeg)

###### 项目介绍

MetaGPT是一个多智能体元编程框架，旨在解决上述问题。该项目具有以下特点：

- MetaGPT接受一个简短的需求描述作为输入，并输出用户故事、竞品分析、需求文档、数据结构、API文档等多个方面的输出。
- 在内部，MetaGPT包含了产品经理、架构师、项目经理、工程师等不同角色，提供了完整的软件公司流程和精心设计的标准操作流程（SOP）。
- 核心理念是“Code = SOP(Team)”，通过将SOP具体化并应用于由LLMs组成的团队，实现了软件公司多角色的协同工作。

![](https://raw.githubusercontent.com/geekan/MetaGPT/master/docs/resources/software_company_cd.jpeg)
![](https://raw.githubusercontent.com/geekan/MetaGPT/master/docs/resources/workspace/content_rec_sys/resources/data_api_design.png)

等于用 GPT 开了一家软件外包的公司，这个项目是不是很有想象力？

###### 如何使用

要开始使用MetaGPT，可以按照以下步骤进行安装：

```bash
# 第一步：确保系统上已安装NPM，并安装mermaid-js
npm --version
sudo npm install -g @mermaid-js/mermaid-cli

# 第二步：确保系统上已安装Python 3.9+，可以使用以下命令进行检查
python --version

# 第三步：克隆项目到本地，并安装依赖
git clone https://github.com/geekan/metagpt
cd metagpt
python setup.py install
```

项目的配置包括：
- 在`config/key.yaml`、`config/config.yaml`或环境变量中配置`OPENAI_API_KEY`，优先顺序为`config/key.yaml` > `config/config.yaml` > 环境变量。
- 可选的配置项是`OPENAI_API_BASE`。

以下是该项目根据如下命令 `python startup.py "Design a RecSys like Toutiao"`（设计一个类似头条的推荐系统） 生成的输出，其中包括数据和 API 设计等。是不是很牛逼？

![](https://github.com/geekan/MetaGPT/blob/main/docs/resources/workspace/content_rec_sys/resources/data_api_design.png?raw=true)

以下是一个 DEMO 视频：

https://user-images.githubusercontent.com/2707039/250054654-5e8c1062-8c35-440f-bb20-2b0320f8d27d.mp4

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=geekan/MetaGPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/geekan/MetaGPT 

开源项目作者：geekan

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=geekan/MetaGPT)

关注我们，一起探索有意思的开源项目。

