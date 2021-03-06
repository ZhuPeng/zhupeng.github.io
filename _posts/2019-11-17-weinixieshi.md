---
layout: post
title: 为你弹琴写诗的机器学习模型
tags: 其他
---

在开始今天的分享之前，我们先听一首老歌《为你写诗》，这大概是我看到今天分享的项目的时候，第一是时间想到的。



“为你写诗为你静止，为你做不可能的事。”，回忆那些青葱岁月，当年那个为你写诗的小伙现在怎么样了？

嗯，他考上了梦想的大学，学了计算机专业，开始研究用计算机写诗。他还是那个他，但是你还是当年的你嘛？

今天就是要分享两个机器学习的项目，为你写诗和对对联。

1. 为你写诗

[Morizeyao/GPT2-Chinese](https://github.com/Morizeyao/GPT2-Chinese) 是一个使用 BERT 的 Tokenizer 或 Sentencepiece 的BPE 机器学习模型，可以写诗，新闻，小说，或是训练的通用语言模型。支持字为单位或是分词模式或是 BPE 模式（需要略微修改项目中 train.py 的代码），支持大语料训练。

从描述来看有点专业，我们来看一下根据这个模型生成的一些成果。

![](https://raw.githubusercontent.com/Morizeyao/GPT2-Chinese/master/sample/poem_1.png)



![](https://raw.githubusercontent.com/Morizeyao/GPT2-Chinese/master/sample/金庸_倚天屠龍記.jpg)

> 项目地址：https://github.com/Morizeyao/GPT2-Chinese



2. 对对联

用深度学习来对对联，用 Tensorflow 实现。可以通过网站 https://ai.binwang.me/couplet/ 体验。

| 上联           | 下联           |
| -------------- | -------------- |
| 殷勤怕负三春意 | 潇洒难书一字愁 |
| 如此清秋何吝酒 | 这般明月不须钱 |
| 天朗气清风和畅 | 云蒸霞蔚日光辉 |
| 梦里不知身是客 | 醉时已觉酒为朋 |
| 千秋月色君长看 | 一夜风声我自怜 |

好奇的我也尝试着玩了一下，还蛮有趣的。

![image-20191117164344028](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/duiduilian.png)

> 项目地址：https://github.com/wb14123/seq2seq-couplet