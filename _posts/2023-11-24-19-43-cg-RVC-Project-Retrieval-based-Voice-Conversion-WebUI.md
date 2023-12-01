---
layout: post
title: GitHub 开源项目 RVC-Project/Retrieval-based-Voice-Conversion-WebUI 介绍，Voice data <= 10 mins can also be used to train a good VC model!
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 RVC-Project/Retrieval-based-Voice-Conversion-WebUI，该项目在 GitHub 有超过 13.7k Star，用一句话介绍该项目就是：“Voice data <= 10 mins can also be used to train a good VC model!”。


![image](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/assets/129054828/092e5c12-0d49-4168-a590-0b0ef6a4f630)
![image](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/assets/129054828/143246a9-8b42-4dd1-a197-430ede4d15d7)
![](https://counter.seku.su/cmoe?name=rvc&theme=r34)



背景介绍：
随着深度学习技术的广泛应用，以及音频处理领域的持续发展，变声技术的需求越来越大。但是，使用深度学习训练优秀的变声模型通常需要大量的语音数据，一般是数小时甚至数十小时的语音数据才能得到相对满意的结果，这使得变声技术的应用受到一定的限制。因此，如何使用更少的语音数据（如小于10分钟）训练优秀的变声模型是一个迫切需要解决的问题。

项目介绍：
GitHub上的 [Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) 项目是一个基于VITS的变声框架，它的主要特点是可以使用少量的语音数据训练优秀的变声模型（推荐至少收集10分钟低底噪语音数据）。项目的主要功能包括：使用 top1检索替换输入源特征为训练集特征来杜绝音色泄漏；即便在相对较差的显卡上也能快速训练；可以通过模型融合来改变音色；提供了简单易用的网页界面等。另外，该项目还使用了最先进的人声音高提取算法 [InterSpeech2023-RMVPE](https://github.com/Dream-High/RMVPE) 来根绝哑音问题。

如何使用：
首先，你需要安装 Python 3.8或以上版本，并安装项目所需的库。然后，下载项目所需要的预模型和其他文件，可以从项目的[Hugging Face space](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main/) 下载。接下来，运行 `python infer-web.py` 命令来启动WebUI。如果你正在使用 Windows 或 macOS，你可以直接下载并解压`RVC-beta.7z`，前者可以运行`go-web.bat`以启动WebUI，后者则运行命令`sh ./run.sh`以启动WebUI。

项目推介：
该项目是由 [RVC-Project](https://github.com/RVC-Project) 维护，该团队一直致力于深度学习和音频处理领域的研究工作，项目更新较为活跃。如果你在音频处理或者变声技术方面有需求，我强烈推荐你使用这个项目。具体的使用方法和注意事项在项目的README文档中有详细的解释和示例，十分方便新手上手。同时，项目作者也提供了详细的开发和使用教程，可以帮助初学者快速了解和掌握变声技术。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=RVC-Project/Retrieval-based-Voice-Conversion-WebUI&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI 

开源项目作者：RVC-Project

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

关注我们，一起探索有意思的开源项目。

