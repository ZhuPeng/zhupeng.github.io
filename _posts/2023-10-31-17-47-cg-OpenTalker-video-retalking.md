---
layout: post
title: VideoReTalking - 根据输入的音频编辑真实世界中的讲话人视频的面部表情
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

如果你是一个视频相关的工作人员，遇到需要对视频进行编辑的情况，尤其是对于讲话人的视频，需要去改变视频中讲话人的语音或者情绪时，如何让视频中的嘴唇动作与新的语音同步，这就成为了一个难题。这个问题的核心痛点在于，我们需要在保持视频质量的同时，实现对讲话人嘴唇动作的精准编辑，以达到与新的语音同步。

今天要给大家推荐一个 GitHub 开源项目 OpenTalker/video-retalking，该项目在 GitHub 有超过 2.8k Star，用一句话介绍该项目就是：“[SIGGRAPH Asia 2022] VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild”。

![](https://opentalker.github.io/video-retalking/static/images/teaser.png)



###### 项目介绍

VideoReTalking 是一个全新的系统，能够根据输入的音频编辑真实世界中的讲话人视频的面部表情，即使情绪不同，也能产生高质量且嘴唇同步的输出视频。该系统将这个目标分解为三个顺序任务：1）使用标准表情生成面部视频；2）音频驱动的嘴唇同步；3）提高照片真实感的面部增强。所有这些步骤都采用了基于机器学习的方法，所有模块都可以在一个顺序的流程中处理，无需用户干预。

![](https://raw.githubusercontent.com/OpenTalker/video-retalking/master/./docs/static/images/pipeline.png?raw=true)

演示视频地址：https://user-images.githubusercontent.com/4397546/224310754-665eb2dd-aadc-47dc-b1f9-2029a937b20a.mp4

###### 如何使用

首先，你需要从 GitHub 上克隆项目到本地，然后创建一个名为 video_retalking 的 python 环境，并激活它。然后，你需要安装 ffmpeg 和 PyTorch，以及其他必要的依赖。接下来，你可以下载该项目的预训练模型，并将它们放在 ./checkpoints 目录下。最后，你可以通过运行 inference.py 脚本来进行推理。此脚本包括数据预处理步骤，你可以测试任何讲话人视频，无需手动对齐。

```bash
git clone https://github.com/vinthony/video-retalking.git
cd video-retalking
conda create -n video_retalking python=3.8
conda activate video_retalking

conda install ffmpeg

# Please follow the instructions from https://pytorch.org/get-started/previous-versions/
# This installation command only works on CUDA 11.1
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt
```

###### 项目推介

VideoReTalking 是 SIGGRAPH Asia 2022 Conference Track 的一部分，由来自西安电子科技大学和腾讯 AI 实验室的研究人员共同开发，该项目已经在腾讯 AI 实验室中得到应用。如果你在研究中发现该工作有用，请考虑引用他们的工作。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=OpenTalker/video-retalking&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/OpenTalker/video-retalking 

开源项目作者：OpenTalker

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=OpenTalker/video-retalking)

关注我们，一起探索有意思的开源项目。