---
layout: post
title: EmotiVoice - 网易有道开源强大且现代化的文本转语音引擎
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在数字化语音的领域中，我们经常会遇到一个问题：怎么样能降低机器生成语音的机械性，增强情感色彩。比如在任何需要语音互动的场合，如智能语音助手、导航、儿童故事机、电台等，更真实且多样化的语音会极大提升用户体验。这就是我们需要解决的痛点。

今天要给大家推荐一个 GitHub 开源项目 netease-youdao/EmotiVoice，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“EmotiVoice 😊: a Multi-Voice and Prompt-Controlled TTS Engine”。

以下是 EmotiVoice 生成的一些示例：

~/Downloads/EmotiVoice-1.mp4

~/Downloads/EmotiVoice-2.mp4

###### 项目介绍

EmotiVoice 是一个强大且现代化的文本转语音引擎，可以以 2000 多种不同的声音读出英文和中文文本。其最突出的特点是能完成**情感合成**，让生成的语音带有各种情绪，如开心、兴奋、伤心、生气等。它提供了一个易于使用的 web 界面，还有脚本接口可以批量生成结果。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231216225521775.png)

###### 如何使用

我们可以通过运行 docker 镜像快速尝试 EmotiVoice。首先需要有 NVidia 的 GPU，然后设置好 NVidia 容器工具，最后运行以下命令启动它：

```sh
docker run -dp 127.0.0.1:8501:8501 syq163/emoti-voice:latest
```

现在在浏览器中打开 http://localhost:8501 就可以使用 EmotiVoice 的强大 TTS 能力了。同时，它也提供了后台方式运行，需要先通过相应的命令行完成环境的配置和模型文件的准备，之后就可以开始语音的生成了。具体安装方式可参考项目 README。

###### 项目推介

EmotiVoice 是网易有道出品的开源项目，得益于公司的强大研发实力，项目的质量和维护都有保证。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=netease-youdao/EmotiVoice&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/netease-youdao/EmotiVoice 

开源项目作者：netease-youdao

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=netease-youdao/EmotiVoice)

关注我们，一起探索有意思的开源项目。

