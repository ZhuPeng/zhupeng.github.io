---
layout: post
title: 根据写代码的状态播放符合心情的音乐
tags: 插件
---

大家好。

有人喜欢上午写代码、有人喜欢下午或者晚上，有人喜欢写代码的时候听着音乐，有人喜欢安静。每个人有自己的喜欢无可厚非，但是对于写代码来说，不同的状态写的代码还是有差别的。比如心情不好的时候可能写的代码 Bug 比较多，不过这只是小编的个人猜测。

今天要推荐的开源项目非常厉害了，能根据你写代码的状态，播放合适的音乐，这对于喜欢写代码的时候听音乐的小伙伴应该会喜欢，毕竟至少我不能一直听单一的歌单。

这个工具是一款 VSCode 插件，以下是操作界面的介绍，不过有点可惜的是这个工具需要你有一个 Spotify 账户，因为音乐都是通过 Spotify 获取的。

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_music.vscode.png)

不过这个想法还是很牛逼的，感兴趣的同学可以试着看能不能适配一下国内的一些音乐播放软件。

这款插件依赖一个代码时间（Code Time）插件，代码时间通过将你使用 VSCode 的数据记录下来，并分析你的工作状态。以下是一些示例：

![Code Time programming metrics](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_measure-progress-2.5.0.png)

![Code Time web app](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_visualize-everything.png)

项目通过机器学习的方式分析了超过 15 万开发者的听音乐习惯，并结合你的代码时间，向你推荐能够提高你效率的歌曲。听起来就很牛逼对不对，不管推荐的歌曲你是否喜欢，我觉得这是一个值得尝试的工具。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/swdotcom/swdc-vscode-musictime
