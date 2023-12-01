---
layout: post
title: GitHub 开源项目 jianchang512/pyvideotrans 介绍，Translate the video from one language to another and add dubbing.  将视频从一种语言翻译为另一种语言，并添加配音
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 jianchang512/pyvideotrans，该项目在 GitHub 有超过 2.1k Star，用一句话介绍该项目就是：“Translate the video from one language to another and add dubbing.  将视频从一种语言翻译为另一种语言，并添加配音”。


![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p6.png)
![](https://private-user-images.githubusercontent.com/3378335/285566255-521d8623-fc91-43cb-bed4-e21b9b87f39d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDA5MDg0MDcsIm5iZiI6MTcwMDkwODEwNywicGF0aCI6Ii8zMzc4MzM1LzI4NTU2NjI1NS01MjFkODYyMy1mYzkxLTQzY2ItYmVkNC1lMjFiOWI4N2YzOWQucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMTEyNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzExMjVUMTAyODI3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MDZlODIyYjc1NjgzNWM0NGM4OWY1M2Y3N2Y3OTk3OTg3NzkxODZiOWIwY2Y4NmM0NjVhMjFkMDNlY2NkZjc5NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.-WNQR73lwrc-gEHU_-aX5Us-pzeyyRKNMm-5v212CWc)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p1.png?b)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p2.png?b)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p3.png?b)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p4.png?b)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p5.png?b)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/p6.png?b)
![](https://raw.githubusercontent.com/jianchang512/pyvideotrans/master/./images/cli.png?c)



色，该字段留空将不会配音

**--subtitle_file**：自定义字幕文件路径，可不填

**--auto_cut**：True or False，是否启用自动分割后再识别，默认 `True`, 适合大部分视频。如果你的视频中音轨静音音符较准确，则可选择 `False`

**--model_type**：语音识别模型选择，`base/small/medium/large/large-v3`，默认为 `base`，第一次使用需要稍等片刻下载模型

**--video_play_speed_down**：True or False，翻译后不同语言下发音时长不同，比如一句话中文3s，翻译为英文可能5s，导致时长和视频不一致。True 表示强制视频慢速播放，以便延长视频时长和配音对齐。默认 False

**--tts_play_speed_up**：配音后可能和原视频长度不一样，需要按比例调整，value 为 -90 到 90 之间的数值，默认 0

## 命令行实例

`python cli.py --source_mp4 ./test.mp4 --target_dir D:/video --source_language en-US --target_language zh-cn --subtitle_type=1 --voice_role=zhcn-nannan --model_type=base`

## API

> 参考 https://github.com/jianchang512/pyvideotrans/wiki

### 例子

点开查看百度智能云翻译的实例
>
> 参考百度智能云的[人声合成](https://cloud.baidu.com/doc/SPEECH/ASR-Online-Python-SDK.html)的文档，
> 

### FAQ

加入QQ群讨论：634408942

## Donate

开发者的 GitHub 主页有捐赠按钮，快去看看吧。你的支持将是无比的鼓励

**发现了问题，欢迎在 GitHub 提issue，我会尽快修复。**

## License

The author (@jianchang512) has released this software under the LGPL-3.0 License.

# 介绍文案：

1、背景介绍：

在数字时代，视频已经上升为主流的信息传递媒介。然而，面对涌现出的海量视频资料，一种普遍的问题看上去越发严重，那就是我们可能无法明白视频语言造成的隔阂。以视觉和听觉为基础的信息绝大部分来源于视频中的语言。当我们尝试理解一个使用非母语制作的视频时，难以理解的语言总会成为阻碍，我们需要一个将视频翻译成我们可以理解的语言，并添加配音的工具。

2、项目介绍：

`pyvideotrans` 是您在跨越语言鸿沟时的得力助手。它是一个开源的视频翻译和配音工具，可以将一种语言的视频翻译为另一种语言，并加入配音和字幕。它基于 `openai-whisper` 离线模型进行语音识别，并对文本进行翻译，翻译服务支持 `google|baidu|tencent|chatGPT|DeepL|DeepLX` ，并使用 `Microsoft Edge tts` 或 `Openai TTS-1` 进行语音合成。同时，它配有一个简单的视频工具箱，包括音视频分离、音视频字幕合并、语音识别、语音合成、格式转化以及摄像头麦克风录制等功能。

该项目强大的功能让他适用于各种场景，比如说，我们可以通过它翻译并配音 A 语言的视频，转为 B 语言配音，且显示 B 语言字


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=jianchang512/pyvideotrans&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jianchang512/pyvideotrans 

开源项目作者：jianchang512

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=jianchang512/pyvideotrans)

关注我们，一起探索有意思的开源项目。

