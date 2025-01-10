---
layout: post
title: GitHub 开源项目 jingyaogong/minimind 介绍，🚀🚀 「大模型」3小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 3 hours!
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 jingyaogong/minimind，该项目在 GitHub 有超过 4.2k Star。

![](https://stats.deeptrain.net/repo/jingyaogong/minimind/?theme=light)

一句话介绍该项目：🚀🚀 「大模型」3小时完全从0训练26M的小参数GPT！🌏 Train a 26M-parameter GPT from scratch in just 3 hours!




![logo](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/logo.png)

![streamlit](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/streamlit.gif)

![2-eval](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/2-eval.png)

![](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/LLM-structure.png)

![](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/LLM-structure-moe.png)

![gpt3_config.png](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/gpt3_config.png)

![images](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/logger.png)

![images](https://raw.githubusercontent.com/jingyaogong/minimind/master/./images/fastgpt.png)

![](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

![](https://g.alicdn.com/sail-web/maas/1.15.0/static/modelscopeIcon.cd89353f.svg)


###### 项目介绍

### 🚀 **MiniMind 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-0f6fb61b7e1f7348bfef78c6b4702457.png)

项目介绍文案**

随着人工智能的迅猛发展，大型语言模型（LLM）如 GPT-3 已成为科技界的热点。然而，这些大模型虽然性能出色，但其庞大的参数量使得普通研究者难以训练和部署。这不仅限制了技术的普及，也让很多有志于人工智能领域的创新者望而却步。在这样的背景下，一个能够在普通个人电脑上快速训练和部署的轻量级模型的需求，变得日益迫切。

#### 🌟 **项目背景与介绍**

[**MiniMind**](https://github.com/jingyaogong/minimind) 正是在这样的背景和需求下应运而生的开源项目。**MiniMind** 是一个轻量级的语言模型，其大小仅为 26.88M 参数量，大约是 GPT-3 的 1/7000。这一创新之举，意味着即使是最普通的个人 GPU 也可快速进行推理甚至训练，极大地降低了使用大型语言模型的硬件门槛。

**MiniMind** 提供了从数据集清洗预处理到监督预训练、有监督指令微调、低秩自适应微调等全阶段代码，并且对模型进行了拓展，包括共享混合专家(MoE)的稀疏模型，以及视觉多模态 VLM 的支持。这不仅是一个开源模型的实现，也是入门大语言模型的优质教程，帮助研究者和开发者快速上手并对 LLM 领域产生更多的探索与创新。

#### 📦 **如何使用 MiniMind**

1. **环境准备与安装：** 确保你的机器配置与项目要求相符合，然后按照项目 README 中的指引安装所需要的环境和依赖。

    ```bash
    git clone https://github.com/jingyaogong/minimind.git
    pip install -r requirements.txt
    ```

2. **训练模型：** 可以根据自己的需求，选择合适的参数，使用提供的数据集或自定义数据集进行模型的训练。

    ```bash
    python 1-pretrain.py
    python 3-full_sft.py
    ```

3. **模型推理：** 使用训练好的模型进行推理，看看模型的效果如何。

    ```bash
    streamlit run fast_inference.py
    ```

#### 💡 **为何选择 MiniMind？**

- **开发活跃度：** MiniMind 项目持续更新，不断加入新的功能和改进，社区活跃。
- **作者贡献：** 项目作者 jingyaogong 是一位活跃在深度学习领域的贡献者，具有丰富的经验。
- **在使用的公司/研究者：** MiniMind 由于其轻量化和易用性，已经被多个研究组织和公司采用，用于开展相关的 NLP 任务和产品开发。
- **教育价值：** 作为一个入门大语言模型的优秀教程，已经帮助许多初学者快速理解和入门该领域。

**MiniMind** 项目不仅为想要尝试大语言模型的研究者和爱好者提供

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jingyaogong/minimind&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jingyaogong/minimind 

开源项目作者：jingyaogong

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jingyaogong/minimind)

关注我们，一起探索有意思的开源项目。

