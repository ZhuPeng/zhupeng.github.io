---
layout: post
title: GPT Academic - 专门为学术研究而优化的大模型实用化交互项目
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的学术研究过程中，经常会遇到一些问题，比如阅读英文论文的难度、论文的润色和写作、代码的解析等。这些问题可能会消耗我们大量的时间和精力，而且如果没有足够专业的知识和技能，可能还会影响我们的研究效果的进展。因此，我们需要一个工具，能够帮助我们解决这些问题，提高我们学术研究的效率。

今天要给大家推荐一个 GitHub 开源项目 binary-husky/gpt_academic，该项目在 GitHub 有超过 44.6k Star，用一句话介绍该项目就是：“为 ChatGPT/GLM 提供实用化交互界面，特别的优化论文阅读/润色/写作体验，支持 Python 和 C++ 等项目剖析&自译解功能、PDF/LaTex 论文翻译&总结功能”。

![](https://raw.githubusercontent.com/binary-husky/gpt_academic/master/docs/logo.png)

![](https://user-images.githubusercontent.com/96192199/230361456-61078362-a966-4eb5-b49e-3c62ef18b860.gif)

###### 项目介绍

GPT 学术优化（GPT Academic）是一个为 ChatGPT/GLM 提供实用化交互界面的开源项目，它特别优化了论文阅读/润色/写作体验，模块化设计，支持自定义快捷按钮&函数插件，支持 Python 和 C++ 等项目剖析&自译解功能，PDF/LaTex 论文翻译&总结功能，支持并行问询多种 LLM 模型，支持 chatglm2 等本地模型。此外，该项目还兼容文心一言, moss, llama2, rwkv, claude2, 通义千问, 书生, 讯飞星火等。

以下是一些具体的使用示例：

1、论文润色/纠错

![](https://user-images.githubusercontent.com/96192199/231980294-f374bdcb-3309-4560-b424-38ef39f04ebd.gif)

2、如果输出包含公式，会同时以 text 形式和 Latex 渲染形式显示，方便复制和阅读

![](https://user-images.githubusercontent.com/96192199/230598842-1d7fcddd-815d-40ee-af60-baf488a199df.png)

3、解释代码：懒得看项目代码？整个工程直接给 ChatGPT 炫嘴里

![](https://user-images.githubusercontent.com/96192199/226935232-6b6a73ce-8900-4aee-93f9-733c7e6fef53.png)

###### 如何使用

首先，你需要安装项目的依赖，可以通过 `pip install -r requirements.txt` 来安装。然后，你可以根据项目的 README 来了解每个功能的使用方法。例如，你可以使用一键润色功能来查找论文的语法错误，使用一键中英互译功能来进行中英文的翻译，使用一键代码解释功能来解析代码等。此外，你还可以自定义快捷键，使用函数插件来扩展项目的功能。

以下是对应自定义 Prompt 提示词的示例：

配置：

```json
"超级英译中": {
    # 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
    "Prefix": "请翻译把下面一段内容成中文，然后用一个markdown表格逐一解释文中出现的专有名词：\n\n", 
    
    # 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来。
    "Suffix": "",
},
```

效果：

![](https://user-images.githubusercontent.com/96192199/226899272-477c2134-ed71-4326-810c-29891fe4a508.png)

###### 项目推介

GPT 学术优化是一个非常活跃的开源项目，项目已经获得了很多 Star。项目的功能非常强大，可以帮助我们解决很多学术研究中的问题，提高我们的学术研究效率。因此，我强烈推荐你试试这个项目，我相信它会给你带来很大的帮助。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=binary-husky/gpt_academic&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/binary-husky/gpt_academic 

开源项目作者：binary-husky

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=binary-husky/gpt_academic)

关注我们，一起探索有意思的开源项目。

