---
layout: post
title: GitHub 开源项目 lipku/metahuman-stream 介绍，Real time interactive streaming digital human
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 lipku/metahuman-stream，该项目在 GitHub 有超过 2.2k Star。

![](https://stats.deeptrain.net/repo/lipku/metahuman-stream/?theme=light)

一句话介绍该项目：Real time interactive streaming digital human




![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/l3ZibgueFiaeyfaiaLZGuMGQXnhLWxibpJUS2gfs8Dje6JuMY8zu2tVyU9n8Zx1yaNncvKHBMibX0ocehoITy5qQEZg/640?wxfrom=12&tp=wxpic&usePicPrefetch=1&wx_fmt=jpeg&amp;from=appmsg)


###### 项目介绍

背景介绍：在数字娱乐、虚拟直播和远程会议等场景中，数字化角色和实时互动日益成为核心需求。观众和用户不仅期待与数字角色有着高度逼真的音视频同步互动体验，还希望这种互动能够达到低延迟、高效率，甚至是实时打断和全身视频拼接等高级功能的水平，来提供更为丰富和真实的交互体验。然而，市场上能够满足这些要求的解决方案不多，同时这些技术的实现通常需要较高的技术门槛和复杂的系统配置，这对于很多内容创作者和小型企业来说，是一个不小的挑战。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-a3b12fdff8633de62ef5d6bc97389201.png)

项目介绍：针对上述问题，《Metahuman Stream》是一个开源项目，致力于实现实时交互流式数字人，用以实现音视频同步对话，并基本达到商用效果。该项目支持多种数字人模型，如 ernerf、musetalk、wav2lip 等，并提供声音克隆、数字人说话被打断、全身视频拼接、支持 rtmp 和 webrtc 以及不说话时播放自定义视频等高级功能。《Metahuman Stream》通过高度优化的代码和算法，使得数字人生成和流式传输更为高效、灵活，为用户提供更为真实和丰富的互动体验。

如何使用：
1. 安装依赖：该项目要求在 Ubuntu 20.04 系统上，基于 Python3.10、Pytorch 1.12 和 CUDA 11.3 环境进行安装和运行。首先创建并激活 Python 虚拟环境，然后安装相关依赖库。
2. 快速开始：测试时默认采用 ernerf 模型，通过 webrtc 推流到 srs。首先运行 srs，然后启动数字人，用浏览器打开特定 URL 即可实现数字人对话及交互功能。
3. 高级用法：此外，项目还支持使用 LLM 模型进行数字人对话、声音克隆、音频特征用 hubert，以及设置背景图片等高级功能，供用户根据需要选择使用。

项目推介：《Metahuman Stream》自项目开源以来，因其强大的实时互动数字人生成能力和较低的使用门槛，吸引了众多开发者和内容创作者的广泛关注。项目在 GitHub 上的活跃度较高，得到了社区的积极响应和贡献。此外，多个知名公司和组织已经开始探索使用该项目来丰富他们的产品和服务。该项目以其前沿的技术实现、强大的功能和活跃的社区支持，成为了在实时交互流式数字人方面值得推荐的开源解决方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lipku/metahuman-stream&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lipku/metahuman-stream 

开源项目作者：lipku

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lipku/metahuman-stream)

关注我们，一起探索有意思的开源项目。

