---
layout: post
title: GitHub 开源项目 netease-youdao/QAnything 介绍，Question and Answer based on Anything.
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 netease-youdao/QAnything，该项目在 GitHub 有超过 1.7k Star，用一句话介绍该项目就是：“Question and Answer based on Anything.”。



![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/videos/multi_paper_qa.mp4)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/videos/information_extraction.mp4)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/videos/various_files_qa.mp4)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/videos/web_qa.mp4)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/images/qanything_logo.png)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/images/qanything_arch.png)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/images/two_stage_retrieval.jpg)
![](https://github.com/netease-youdao/BCEmbedding/blob/master/Docs/assets/rag_eval_multiple_domains_summary.jpg)
![](https://raw.githubusercontent.com/netease-youdao/QAnything/master/docs/images/Wechat.jpg)



背景介绍：
在日常生活和工作中，我们时常面临大量信息资料需要关联理解和处理。频繁地切换区分文件格式，加上需要跨语言理解的环境下，如何找到一个准确、快速、可靠地处理文件的解决方案恍若眼前一道难题。这个问题非常现实，也非常复杂，我们需要一个强大且可靠的工具来解决这个问题。

项目介绍：
`QAnything`(**Q**uestion and **A**nswer based on **Anything**) 是一个本地化的知识库问答系统，可以支持大量的文件格式和数据库，并允许离线安装和使用。在 `QAnything` 的帮助下，你只需要简单地操作本地储存的文件，无论文件格式如何，都能收到精确、快捷、可靠的答案。

这个项目的主要功能包括：
- 数据安全，支持断网环境下的安装和使用
- 支持跨语言问答，可根据文档的语言自由切换中英文答案
- 支持大规模数据问答，使用二阶段检索排名，解决大规模数据检索降级问题
- 高性能生产级系统，可直接部署在企业环境下
- 用户友好，无需复杂配置，一键安装部署，开箱即用
- 多知识库问答支持，支持选择多个知识库进行问答

如何使用：
在你开始使用 `QAnything` 之前，你需要先满足一些先决条件，比如：
- Python 3.6 或以上版本
- torch 1.8 或以上版本
- numpy 1.19 或以上

安装过程非常简单，只需要一步操作：
```bash
pip install QAnything
```
在安装完毕后，你可以使用 QAnything 提供的 API 对你的本地文件进行操作。

项目推介：
`QAnything` 项目是由网易有道出品，目前开发活跃。此项目的优势在于其能处理大量不同格式的数据，包括 PDF，Word, PPT ，Eml，TXT，图片等。同时也支持中英文对照，无论问答和文档的语言是什么，都可以自由切换。这对于开发者和数据分析师来说，无疑是一个强大的工具。

此外，`QAnything` 还使用了两阶段的检索策略，这种策略在知识库数据大的情况下有很明显的优势。因此，这个项目可以在处理大量数据的使用情境下，发挥出更优异的性能。

所以，无论你是一个开发者，还是数据分析师，或者只是希望找到一个可以处理大量不同数据的工具，`QAnything` 都能满足你的需求。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=netease-youdao/QAnything&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/netease-youdao/QAnything 

开源项目作者：netease-youdao

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=netease-youdao/QAnything)

关注我们，一起探索有意思的开源项目。

