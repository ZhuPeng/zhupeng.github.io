---
layout: post
title: Donut：文档理解变革的官方实现
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

在处理文档时，我们常常面临诸多挑战，例如光学字符识别（OCR）的限制、多样化文档类型和语言的复杂性。然而，这些问题正是 Donut 项目所致力解决的。

今天要给大家推荐一个 GitHub 开源项目 clovaai/donut，该项目在 GitHub 有超过 3.0k Star，用一句话介绍该项目就是：“Official Implementation of OCR-free Document Understanding Transformer (Donut) and Synthetic Document Generator (SynthDoG), ECCV 2022”。

## 项目介绍

Donut（文档理解变革）是一种使用端到端 Transformer 模型的无 OCR 文档理解方法，并提供了 OCR-free Document Understanding Transformer（Donut）和 Synthetic Document Generator（SynthDoG）的官方实现。Donut 不需要预先训练的 OCR 引擎/API，却在各种视觉文档理解任务（如视觉文档分类和信息提取）中展现出最先进的性能。

![](https://raw.githubusercontent.com/clovaai/donut/master/misc/overview.png)

主要功能介绍：

- OCR-free 文档理解：利用 Transformer 模型实现无 OCR 的文档理解，解决了传统 OCR 方法的限制。
- 多领域、多语言支持：通过 SynthDoG（Synthetic Document Generator），Donut 在模型预训练阶段具备对多种语言和领域的灵活性。

此外，项目提供了详细的设计要点和实现细节，确保了项目的高性能和可扩展性。

![](https://raw.githubusercontent.com/clovaai/donut/master/misc/screenshot_gradio_demos.png)

## 项目推介

Donut是一个活跃的开源项目，是文档理解领域的重要贡献。该项目在 ECCV 2022 中被介绍，并由一批具有丰富经验的研究人员共同开发。其卓越的性能和灵活性使其受到广泛关注和使用。

我们推荐该项目给其他人，无论是对文档理解领域感兴趣的研究者，还是需要处理文档的开发人员。通过 Donut，您可以轻松解决文档理解中的挑战，提升工作效率和准确性。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=clovaai/donut&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/clovaai/donut 

开源项目作者：clovaai

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=clovaai/donut)

关注我们，一起探索有意思的开源项目。

