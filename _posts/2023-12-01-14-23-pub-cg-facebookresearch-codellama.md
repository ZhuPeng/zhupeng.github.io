---
layout: post
title: Meta 开源的代码大模型
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常编程过程中，我们总会遇到诸多编程问题。微小的问题我们可以轻松解决，但对于大型的编程项目和复杂的问题，手动编程效率低且容易出错。同时，对于超大型输入的处理和编程任务的 zero-shot 指令跟踪，我们也总是力不从心。如果你正在寻找支持大型输入内容、具备编程任务 zero-shot 指令跟踪能力的模型，那么 Code Llama 是你的理想选择。

今天要给大家推荐一个 GitHub 开源项目 facebookresearch/codellama，该项目在 GitHub 有超过 11.4k Star，用一句话介绍该项目就是：“Inference code for CodeLlama models”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113192604002.png)

###### 项目介绍

Code Llama 是一种基于 `Llama 2` 的大型编程语言模型集合，具备开源模型中的最佳性能，支持填充能力，支持大型输入内容，还可以用于编程任务的 zero-shot 指令。Code Llama 提供包括一般模型（Code Llama），Python 专用模型（Code Llama - Python），和指令跟踪模型（Code Llama - Instruct）在内的多种版本，并且各个版本的参数量分别达到了 7B、13B 和 34B。所有的模型都是在 16k 的令牌序列上进行训练的，并对多达 100k 令牌的输入内容都有改进。7B 和 13B 的 Code Llama 以及 Code Llama - Instruct 支持基于周围内容的填充。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113192708799.png)

###### 如何使用

要使用 Code Llama，首先需要下载该模型的权重和标记器。下载的方式是访问 `Meta website` ，并接受其许可证。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113192855605.png)

在获得了权重和标记器之后，你需要有能够支持 PyTorch / CUDA 的 conda 环境，并在父目录下运行此命令安装：

```bash
pip install -e .
```
然后，我们可以根据我们的硬件和用途，设置`max_seq_len`和`max_batch_size` 的值，使用这个命令就可以调用预训练特定语言模型：
```bash
torchrun --nproc_per_node 1 example_completion.py \
    --ckpt_dir CodeLlama-7b/ \
    --tokenizer_path CodeLlama-7b/tokenizer.model \
    --max_seq_len 128 --max_batch_size 4
```
对于代码填充，`CodeLlama-7b`模型可以运行填充的命令如下：
```bash
torchrun --nproc_per_node 1 example_infilling.py \
    --ckpt_dir CodeLlama-7b/ \
    --tokenizer_path CodeLlama-7b/tokenizer.model \
    --max_seq_len 192 --max_batch_size 4
```
项目推介

Code Llama 是 Facebook Research 团队的项目，拥有包括 `Code Llama`、`Code Llama - Python`、和 `Code Llama - Instruct` 三大类，7B 到 34B 参数的大规模模型，涵盖了代码生成、Python 专用以及指令追踪等多个应用场景。Code Llama 的优良表现也已经被我们的许多使用者所证实，除此之外，以上模型还得到了许多广大研究社区和业界的一致好评。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=facebookresearch/codellama&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/facebookresearch/codellama 

开源项目作者：facebookresearch

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=facebookresearch/codellama)

关注我们，一起探索有意思的开源项目。

