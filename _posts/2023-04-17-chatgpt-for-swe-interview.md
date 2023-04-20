---
layout: post
title: ChatGPT 这么厉害，能帮我去面试找个工作嘛？
tags: ChatGPT
---

大家好。

在 2023-02-01 新闻报道 ChatGPT 通过了 Google 的 L3 级别工程师的代码面试题，而 L3 这个级别的年薪是 18.3万美元，如果按汇率换算成人民币的话，年薪百万了兄弟们，羡不羡慕？

但是 ChatGPT 这么厉害，能帮我去面试找个工作嘛？年薪百万的那种。

今天要推荐的开源项目 leetcode-mafia/cheetah，在 GitHub 有超过 1.8K Star，是一个可以帮助你实现年薪百万梦想的工具。cheetah 是一个基于 AI 的 MacOS APP，能够在远程面试中，依赖 OpenAI 开源的语音转文字工具 Whisper，将面试官的问题转化为文字提交到 ChatGPT，实现实时的问答面试辅助，助力每一份梦想。以下是官方演示片段。

https://user-images.githubusercontent.com/106342593/229961889-489e2b36-f3e6-453a-9784-f160bc1c4f8d.mp4

cheetah APP 提供三个按钮，分别是：

1、Answer：针对面试官的问题生成相应的答案

2、Refine：针对面试官补充了问题的信息或者额外限制的情况下，重新生成答案

3、Analyze：针对面试需要在浏览器上写代码的场景，安装相应的浏览器插件，能够实时分析对应的代码

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230417215445534.png)

cheetah 的原理也比较简单，基于电脑中将语音输出到多个设备的功能，实现监听面试官问题的语音。

最后，cheetah 是一个国外程序员开发的，这个点子还是非常不错的，但是在中文语境下效果如何，目前还不是很确定。同时在真实的问题面前，ChatGPT 有时候也会出现回答错误的情况，大家要随机应变。在真实场景下使用非常考验大家的心理素质，感兴趣的小伙伴可以自行去尝试。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/leetcode-mafia/cheetah

开源项目作者：cheetah

关注我们，一起探索有意思的开源项目。
