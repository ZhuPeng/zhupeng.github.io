---
layout: post
title: GitHub 开源项目 svc-develop-team/so-vits-svc 介绍，SoftVC VITS Singing Voice Conversion
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 svc-develop-team/so-vits-svc，该项目在 GitHub 有超过 21.1k Star，用一句话介绍该项目就是：“SoftVC VITS Singing Voice Conversion”。


![Diagram](https://raw.githubusercontent.com/svc-develop-team/so-vits-svc/master/shadowdiffusion.png)



背景介绍：
在音乐、动漫创作、语音合成等领域，如何让虚拟角色进行唱歌的表演是一个重要的问题。传统的文本到语音（TTS）技术无法满足这种需求，因为它主要针对的是说话，而不是唱歌。此外，如果我们的目标是模仿一个特定的声音或者角色，就需要进行声音转换，但传统的声音转换技术在合成效果、音质等方面也有诸多问题，比如音高变化不够流畅，音质不够清晰，这使得创作过程中的体验不好，反映在成品中也显得不够自然流畅。

项目介绍：
这是一个用于解决上述问题的开源项目—— SoftVC VITS Singing Voice Conversion，简称 SVC 。不同于传统的 TTS 技术，本项目专注于声乐转换，而不是文本到语音的转换。SVC 的技术特点是，它利用 SoftVC 内容编码器从原始音频中提取语音特征，然后这些特征向量直接输入到 VITS 中，而无需将其转换为文本。这样可以保存原始音频的音调和语调，同时利用 [NSF HiFiGAN](https://github.com/openvpi/DiffSinger/tree/refactor/modules/nsf_hifigan) 替代了原始的声码器，解决了音质连续性的问题。

如何使用：
首先，由于本项目当前限时更新已经结束，将进入存档状态，所以用户需要知道如何克隆项目和设置环境。并且，由于此项目完全离线运行，请确保你自己的设备有足够的可用计算资源。然后，你可以按照 README 文件提供的指引以及示例来进行模型训练和声性转换。由于项目的特殊性，可能训练数据和模型的获取需要用户自行获取授权解决，请在使用时探索并尊重相关的版权规定和约定。

项目推介：
该项目由 SvcDevelopTeam 开发和维护，它已经获得了很多用户的关注和称赞。目前项目仓库的 star 数已经比较高，说明这个项目引领了一个有趣的技术方向，对于关注音乐、动漫、语音技术的爱好者和研究者来说，有很多可以学习和使用的地方。这个项目的主要目的在于方便动漫角色进行表演，因此符合相关爱好者的需求，在这样的背景驱动下，我们相信项目的质量和活跃度都是值得信赖的。如果你对声乐、字符声音合成以及角色配音等领域感兴趣，那么你肯定不应该错过这个项目。这个项目为开发者提供了一个实现声乐转换的强大工具，无论是学习还是使用，都将为你带来很大的帮助。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=svc-develop-team/so-vits-svc&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/svc-develop-team/so-vits-svc 

开源项目作者：svc-develop-team

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=svc-develop-team/so-vits-svc)

关注我们，一起探索有意思的开源项目。

