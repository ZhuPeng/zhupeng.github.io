---
layout: post
title: GitHub 开源项目 RVC-Boss/GPT-SoVITS 介绍，1 min voice data can also be used to train a good TTS model! (few shot voice cloning)
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 RVC-Boss/GPT-SoVITS，该项目在 GitHub 有超过 17.8k Star，一句话介绍该项目：1 min voice data can also be used to train a good TTS model! (few shot voice cloning)




![](https://counter.seku.su/cmoe?name=gptsovits&theme=r34)



背景介绍：
当今时代，语音转文本技术（TTS, Text to Speech）在人工智能领域逐渐占领一席之地。但是，要想训练一个出色的语音模型，往往需要大量的语音数据，而且这些数据的获取成本极高。一方面，你需要筛选和标注大量的音频数据，另一方面，你也需要一个强大的计算能力来处理这些数据。那么，能否有一种方法，只需要少量的语音数据，就能训练出一个高质量的语音模型呢？答案是肯定的。这就是我们今天要介绍的 GitHub 开源项目 GPT-SoVITS。

项目介绍：
GPT-SoVITS 是一款强大的少量样本语音转文本以及语音转换在线 WebUI 工具，它能做到以下几点：
1. 零样本 TTS：将录制的 5 秒钟语音片段转换成文字。
2. 少量样本 TTS：使用仅 1 分钟的训练数据对模型进行微调，提高语音相似度和真实感。
3. 跨语言支持：支持的语言包括英语、日语和中文，这使它能够在与训练数据集不同的语言中进行推理。
4. WebUI 工具：综合工具包括声音伴奏分离，自动训练集切割，中文语音转写，以及文本标签化，这些都能帮助新手创建训练数据集和 GPT/SoVITS 模型。

如何使用：
用户可以在中国区域点击[这里](https://www.codewithgpu.com/i/RVC-Boss/GPT-SoVITS/GPT-SoVITS-Official) 使用 AutoDL Cloud Docker 在线体验全部功能。Windows 用户可以直接下载[预包分发](https://huggingface.co/lj1995/GPT-SoVITS-windows-package/resolve/main/GPT-SoVITS-beta.7z?download=true) 并双击 _go-webui.bat_ 启动 GPT-SoVITS-WebUI。Linux 和 MacOS 用户则需要先创建环境，然后进行依赖的安装。具体步骤包括：

Linux：
```bash
conda create -n GPTSoVits python=3.9
conda activate GPTSoVits
bash install.sh
```
MacOS：
```bash
conda create -n GPTSoVits python=3.9
conda activate GPTSoVits
pip3 install --pre torch torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip install -r requirements.txt
```
项目推介：
在通常情况下，你可能需要大量的语音数据才能训练出优秀的语音模型，但 GPT-SoVITS 打破了这一常理，它只需要一分钟的语音数据，就能训练出一个出色的语音模型。其强大的少样本语音学习能力是其主要的亮点。此外，其 WebUI 工具提供的各种语音处理功能也极大地提高了用户的体验。该项目现在已经在开源领域获得众多关注，推荐给你，希望你也能从中受益。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=RVC-Boss/GPT-SoVITS&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/RVC-Boss/GPT-SoVITS 

开源项目作者：RVC-Boss

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=RVC-Boss/GPT-SoVITS)

关注我们，一起探索有意思的开源项目。

