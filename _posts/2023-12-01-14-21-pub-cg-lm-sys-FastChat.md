---
layout: post
title: 训练托管和评估大语言模型的开放平台
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 项目背景

在如今的各大公司，都开始了大语言模型的训练军备竞赛，而训练语言模型还是有不少的门槛的。在大规模语言模型（LLM）的开发和服务方面，对于一些刚起步的公司来说，缺乏一些专业的平台来进行训练，测试以及优化语言模型。另外，对于智能聊天引擎的评估，如何建立一个全面系统的评估标准和平台也十分必需。

今天要给大家推荐一个 GitHub 开源项目 lm-sys/FastChat，该项目在 GitHub 有超过 29.6k Star，用一句话介绍该项目就是：“An open platform for training, serving, and evaluating large language models"。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240106233705645.png)

###### 项目介绍

FastChat 是一个开放平台，致力于训练，托管，以及评估基于大型语言模型（LLM）的聊天机器人。该项目主要功能有：

1、提供了训练和评估最先进模型（如 Vicuna，MT-Bench）的代码；

2、便携式的多模型服务器系统同时包含 Web UI 和与 OpenAI 兼容的RESTful APIs。

FastChat 支持 Chatbot Arena，为 30 多个 LLM 提供超过 500 万个聊天请求响应。此外，基于LLM对话收集了超过 10 万的人工投票数据，以此编制了在线 LLM 评估排行榜。此外，FastChat 还发布了多个版本的 LLM 模型和对应的权重，例如Vicuna，LongChat 和 FastChat-T5 等。

![](https://raw.githubusercontent.com/lm-sys/FastChat/master/assets/screenshot_gui.png)

###### 如何使用

FastChat 的安装和使用较为简单，以下是一个基本示例：

1、工具安装

方法一：pip 安装
```bash
pip3 install "fschat[model_worker,webui]"
```

方法二：源码安装
```bash
git clone https://github.com/lm-sys/FastChat.git
cd FastChat
# Mac 
brew install rust cmake
# 安装依赖
pip3 install --upgrade pip  # enable PEP 660 support
pip3 install -e ".[model_worker,webui]"
```

这样，FastChat 就安装完成了。

2、程序运行

你可以用以下命令启动聊天，这将会从 Hugging Face 仓库自动下载模型。
例如：如果你要运行 Vicuna 模型，只需执行这条命令：

```bash
python3 -m fastchat.serve.cli --model-path lmsys/vicuna-7b-v1.5
```

###### 项目推介

FastChat 是一个快速发展的开源项目，它是由知名的 lm-sys 团队开发和维护的，具有很高的活跃度。在谷歌学术和 arXiv上，你可以找到 FastChat 的相关论文和技术报告。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240106234426407.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240106234346717.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lm-sys/FastChat&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lm-sys/FastChat 

开源项目作者：lm-sys

开源协议：Apache-2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lm-sys/FastChat)

关注我们，一起探索有意思的开源项目。

