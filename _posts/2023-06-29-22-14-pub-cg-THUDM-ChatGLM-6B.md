---
layout: post
title: ChatGLM-6B：可本地部署的开源双语对话语言模型
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

## 背景介绍

在处理双语对话时，我们经常会遇到各种语言模型不足的问题，包括语义理解、回答准确性等。这些问题限制了对话系统的表现，给开发者带来了挑战。而如今出现的大模型在以上问题有不错的表现，但是一般大模型在部署上需要非常的资源，难以本地化的部署，而今天要推荐的开源项目 ChatGLM-6B 作为一种开源的双语对话语言模型，正是为了解决这些核心痛点而诞生的。

ChatGLM-6B 项目在 GitHub 有超过 30.4k Star，用一句话介绍该项目就是：“ChatGLM-6B: An Open Bilingual Dialogue Language Model | 开源双语对话语言模型”。

![](https://raw.githubusercontent.com/THUDM/ChatGLM-6B/master/resources/webglm.jpg)

## 项目介绍
ChatGLM-6B基于 [General Language Model (GLM)](https://github.com/THUDM/GLM) 架构，是一个开源的中英双语对话语言模型，拥有62亿参数。该模型结合了模型量化技术，用户可以将其部署在低端硬件上（只需要6GB显存），实现本地化部署。它通过训练超过1T标识符的中英双语对话数据，具备了中文问答、对话回答和对话生成的优化能力。通过ChatGLM-6B，用户可以进行微调、反馈自助、人类反馈强化学习等技术的应用。62亿参数的ChatGLM-6B已经能够生成相当合理人类偏好的回答，更多信息请参考我们的博客 https://chatglm.cn/blog。

主要特点：
- 开源的双语对话语言模型
- 基于62亿参数的ChatGLM-6B，可在较少资源下本地部署
- 与ChatGPT技术相似，对中文问答和对话具有优化能力

以下是一个对应的对话示例：

![](https://raw.githubusercontent.com/THUDM/ChatGLM-6B/master/resources/visualglm.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=THUDM/ChatGLM-6B&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/THUDM/ChatGLM-6B 

开源项目作者：THUDM

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=THUDM/ChatGLM-6B)

关注我们，一起探索有意思的开源项目。

