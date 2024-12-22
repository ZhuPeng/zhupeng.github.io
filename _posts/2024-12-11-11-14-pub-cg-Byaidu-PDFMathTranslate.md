---
layout: post
title: 科研文档双语翻译工具
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在学术研究或阅读科研文献时，语言常常成为一大障碍。尤其是对于那些非英语母语的研究者和学习者来说，理解复杂的科学文章非常具有挑战性。而传统的文档翻译工具往往无法处理公式、图表、目录和注释等元素的翻译和保留格式，这无疑加大了阅读和理解的难度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f37a7738dff15f8a879878955095bbdf.png)

今天要给大家推荐一个 GitHub 开源项目 PDFMathTranslate，该项目在 GitHub 有超过 4.2k Star。

![](https://stats.deeptrain.net/repo/Byaidu/PDFMathTranslate/?theme=light)

一句话介绍该项目：PDF scientific paper translation with preserved formats

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241211234326570.png)


###### 项目介绍

PDFMathTranslate 致力于为科研论文提供格式保留的完整双语翻译服务。它支持通过 Google、DeepL、Ollama、OpenAI 等多种翻译服务转换文档，并且提供了命令行工具（CLI）、交互式用户界面（GUI）和 Docker 支持，以满足不同用户的需求。核心功能包括公式、图表、目录和注释的格式保留，多语言支持，并且允许用户自定义翻译服务，以达到最佳的翻译效果。

![](https://raw.githubusercontent.com/Byaidu/PDFMathTranslate/main/docs/images/preview.gif)

###### 如何使用

1、命令行使用：使用命令行工具非常适合那些需要批量转换文档的用户。

```bash
pip install pdf2zh
pdf2zh document.pdf
```
2、GUI 使用：GUI 提供了一个友好的交互界面

```bash
pip install pdf2zh
pdf2zh -i
http://localhost:7860/
```
![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/gui.gif)

3、Docker 使用：使用 Docker 可以避免环境配置的麻烦，实现快速部署。

```bash
docker pull byaidu/pdf2zh
docker run -d -p 7860:7860 byaidu/pdf2zh
http://localhost:7860/
```
###### 项目推介

PDFMathTranslate 其优点在于能够精准处理科学文档中的专业元素，而且格式保持完善，极大地提高了非英语母语研究者的阅读效率。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Byaidu/PDFMathTranslate&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Byaidu/PDFMathTranslate 

开源项目作者：Byaidu

开源协议：GNU Affero General Public License v3.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Byaidu/PDFMathTranslate)

关注我们，一起探索有意思的开源项目。

