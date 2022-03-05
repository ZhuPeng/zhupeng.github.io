---
layout: post
title: 实时中文语音克隆，让声音模仿如此简单
tags: Python，机器学习
---

大家好。

现在的人工智能越来越发达，而现阶段很多的智能系统的语音效果还是比较差的，比如一般的客服系统，语音非常的冷漠和刻板。

今天要推荐的开源项目 MockingBird，拟声鸟能够使用 5 秒的真实语音录音，即可通过机器学习的方式，对声音进行克隆，从而实现按相同声音说出任意的文本。

点击如下链接可查看 DEMO 效果：https://www.bilibili.com/video/BV17Q4y1B7mY/

通过借助 MockingBird 能够很轻松的克隆一个声音并应用到人工智能系统中，从而改善系统的音乐的拟人声的效果。

MockingBird 使用 PyTorch 开发，能够在 Windows 和 Linux 系统中运行，MockingBird 现在是可以开箱即用的，如果你想要自己做定制开发，作者也简单介绍了如下项目的代码结构：

![image-20220207204342795](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220207204342795.png)

除了训练相应的模型意外，MockingBird 还提供了一个可供使用的 Web 页面，运行命令 python web.py 即可查看。

![image-20220207204459863](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220207204459863.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/babysor/MockingBird
