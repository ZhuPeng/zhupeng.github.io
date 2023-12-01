---
layout: post
title: GitHub 开源项目 imoneoi/openchat 介绍，OpenChat: Advancing Open-source Language Models with Imperfect Data
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 imoneoi/openchat，该项目在 GitHub 有超过 3.4k Star，用一句话介绍该项目就是：“OpenChat: Advancing Open-source Language Models with Imperfect Data”。


![](https://raw.githubusercontent.com/imoneoi/openchat/master/assets/logo_new.png)
![](https://raw.githubusercontent.com/imoneoi/openchat/master/assets/openchat.png)
![](https://raw.githubusercontent.com/imoneoi/openchat/master/assets/openchat_grok.png)



背景介绍：对于语言理解和聊天对话生成等各种应用场景，我们面临着如何不偏爱任何标识的同时从混合质量的数据中进行学习的问题。传统的大型语言模型常常需要全程监督，在缺乏高质量偏爱标签的数据上可塑性并不高。虽然有一些预训练语言模型可供选择，但在聊天机器人等应用上的表现仍有待提升。

项目介绍：OpenChat 是一款借鉴了离线强化学习策略的开源语言模型库。即使以 `7B` 的模型在消费级显卡（如 RTX 3090）上运行，OpenChat 的性能也可与 `ChatGPT` 持平。该项目的目标是开发出一款高性能、适合商业应用的开源大型语言模型，目前已经对此进行了多次优化和迭代。OpenChat 的模型学习的数据源包括各种质量的数据，能够有效处理和解决混合质量学习的问题。

如何使用：可以通过 Github 下载 OpenChat 项目代码，按照 readme 的说明完成安装。另一方面，用户能够直接通过模型链接 `https://huggingface.co/openchat/` 在线使用 OpenChat 的各个版本的模型。计算各种评测的代码的运行如下：

```bash
# 在此仓库的基础目录运行以下命令
python -m ochat.evaluation.run_eval --condition "GPT4 Correct" --model openchat/openchat_3.5
python ochat/evaluation/view_results.py
```
项目推介：OpenChat 是一款活跃的开源项目，作者积极推出更新版模型和优化策略。OpenChat 的模型性能达到甚至超越了同类型的大型商业模型。OpenChat 的 `7B` 模型在 MT-bench 上的评分达到了 7.81，超过了 70B 的模型。此外，OpenChat 也发布了自己的论文 "OpenChat: Advancing Open-source Language Models with Mixed-Quality Data"，详细介绍了其开发设计理念和具体实现。因此，对于需要在语言理解、对话生成等领域应用的开发者和研究人员来说，OpenChat 是一款极具价值且表现优秀的开源项目。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=imoneoi/openchat&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/imoneoi/openchat 

开源项目作者：imoneoi

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=imoneoi/openchat)

关注我们，一起探索有意思的开源项目。

