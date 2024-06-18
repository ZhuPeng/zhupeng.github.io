---
layout: post
title: Bilibili 视频转文字，一步到位输入链接即可使用
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在这个信息爆炸的时代，视频成了传播知识和信息的重要载体。Bilibili 作为年轻人喜爱的视频分享网站，汇聚了海量的学习、娱乐、科技等内容。然而，有时候我们需要将视频内容转换成文本形式，无论是为了学习笔记、内容整理还是信息提取。传统上，这要么依赖人工逐字逐句转录，耗费大量时间和精力；要么依靠不尽如人意的语音转文字服务，准确率和效率常常令人头疼。对于希望得到快速、准确转换结果的用户来说，这无疑是一个巨大的挑战。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-e0a725b4bf01f76b7e30e861696279ef.png)

今天要给大家推荐一个 GitHub 开源项目 bili2text，该项目在 GitHub 有差不多 500 Star。

![](https://stats.deeptrain.net/repo/lanbinshijie/bili2text/?theme=light)

一句话介绍该项目：Bilibili视频转文字，一步到位，输入链接即可使用

![](https://raw.githubusercontent.com/lanbinshijie/bili2text/master/light_logo2.png)

###### 项目介绍

Bili2text 专为将 Bilibili 视频转换为文本设计。通过简单的操作流程：下载视频、提取音频、分割音频，最后利用 OpenAI 的 **whisper** 模型实现高准确度的语音到文字的自动转换。

![](https://raw.githubusercontent.com/lanbinshijie/bili2text/master/assets/screenshot2.png)

整个过程一气呵成，只需要用户输入 Bilibili 视频的 **av** 号即可，既适合技术开发者，也适合普通用户通过友好的 UI 界面进行操作。

![](https://raw.githubusercontent.com/lanbinshijie/bili2text/master/assets/screenshot1.png)

###### 如何使用

1、首先，克隆仓库到本地：

```bash
git clone https://github.com/lanbinshijie/bili2text.git
cd bili2text
```

2、安装项目所需的依赖:

```bash
pip install -r requirements.txt
```

3、运行主脚本，按提示输入需要转换的 Bilibili 视频 av 号

```python
python main.py
```

4、或者使用带有用户界面的版本，方便友好

```bash
python window.py
```
输入链接后自动处理，整个过程使用者无需过多干预，真正实现了从视频到文本的无缝转换。

###### 项目推介

自项目上线以来，Bili2text 凭借其出色的表现和实用性，吸引了众多技术爱好者的关注和使用。尽管是新生项目，但其背后的技术—— OpenAI's whisper 模型的强大功能保证了其在语音转文字方面的高准确率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240601230500818.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lanbinshijie/bili2text&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lanbinshijie/bili2text 

开源项目作者：lanbinshijie

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lanbinshijie/bili2text)

关注我们，一起探索有意思的开源项目。

