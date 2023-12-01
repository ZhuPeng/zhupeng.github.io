---
layout: post
title: GitHub 开源项目 lm-sys/FastChat 介绍，An open platform for training, serving, and evaluating large language models. Release repo for Vicuna and Chatbot Arena.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 lm-sys/FastChat，该项目在 GitHub 有超过 29.6k Star，用一句话介绍该项目就是：“An open platform for training, serving, and evaluating large language models. Release repo for Vicuna and Chatbot Arena.”。


![](https://raw.githubusercontent.com/lm-sys/FastChat/master/assets/demo_narrow.gif)
![](https://raw.githubusercontent.com/lm-sys/FastChat/master/assets/screenshot_cli.png)
![](https://raw.githubusercontent.com/lm-sys/FastChat/master/assets/screenshot_gui.png)



项目背景：在快捷的互联网社会，人们相互间的沟通往往严重依赖于各种社交平台。然而，当前的大部分社交平台并不能满足所有用户的沟通需求，尤其在大规模语言模型（LLM）的开发和服务方面，缺乏专业的平台来进行训练，测试以及优化。另外，对于聊天引擎的评估，如何建立一个全面系统的评估标准和平台也十分必需。

项目介绍：FastChat 是一个开放平台，致力于训练，服务，以及评估基于大型语言模型（LLM）的聊天机器人。该项目主要功能有：提供了训练和评估最先进模型（如 Vicuna，MT-Bench）的代码；便携式的多模型服务器系统同时包含web UI和与OpenAI兼容的RESTful APIs。FastChat支持 Chatbot Arena，为30多个LLM提供超过500万个聊天请求。此外，基于LLM对战收集了超过10万的人工投票，以此编制了在线LLM Elo排行榜。此外，FastChat还发布了多个版本的LLM模型和对应的权重，例如Vicuna，LongChat和FastChat-T5等。

如何使用：FastChat 的安装和使用较为简单，以下是一个基本范例

### 工具安装
方法一：
```bash
pip3 install "fschat[model_worker,webui]"
```

方法二：
首先克隆FastChat的代码库
```bash
git clone https://github.com/lm-sys/FastChat.git
cd FastChat
```

如果你在Mac上运行，你需要先安装rust和cmake
```bash
brew install rust cmake
```

然后安装项目相关依赖
```bash
pip3 install --upgrade pip  # enable PEP 660 support
pip3 install -e ".[model_worker,webui]"
```

这样，FastChat就安装完成了。

### 程序运行
你可以用以下命令启动聊天，这将会从Hugging Face仓库自动下载模型权重。
例如：如果你要运行Vicuna模型，只需执行这条命令：
```bash
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5
```

项目推介：FastChat是一个快速发展的开源项目，它是由知名的lm-sys团队开发和维护的，具有很高的活跃度。FastChat的统计数据显示，该项目已经为超过30多个LLM提供了超过5百万次的聊天请求，并且有大量的活跃用户。在谷歌学术和arXiv上，你可以找到FastChat的相关论文和技术报告。在开源社区，FastChat也收到了大量的热烈关注和好评。FastChat希望将在未来的发展中，进一步提升其产品的优势，并为广大开发者和用户提供更优质的服务。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lm-sys/FastChat&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lm-sys/FastChat 

开源项目作者：lm-sys

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lm-sys/FastChat)

关注我们，一起探索有意思的开源项目。

