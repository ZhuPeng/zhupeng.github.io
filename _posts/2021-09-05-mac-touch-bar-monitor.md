---
layout: post
title: 牛逼，在 Mac 的键盘触摸屏上实现一个监控系统
tags: 前端
---

大家好。

如果大家关注 Mac 的话，大家应该知道在 Mac Pro 的键盘区域是有一个可以触摸的 Touch Bar 的，在一般的使用情况下，这个小显示屏会显示当前软件下支持的快捷化操作。从我个人的使用经验来看，我使用的很少，倒是经常会看这个 Touch  Bar 会显示什么状态，有可能是我的使用方式不对。

总感觉这个地方很有用，但是没有发挥出来作用，有没有小伙伴和我一样的想法？

直到我看到今天要推荐的开源项目：touchbar-systemmonitor，它将 Touch Bar 改造成一个小型监控系统，真是深得我心。

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/touchbar_systemmonitor3.gif)

这个项目会展示当前电脑的运行情况，极大的发挥了 Touch Bar 的作用，物尽其用。这个项目使用 [Electron](https://github.com/atom/electron) 进行开发，安装和使用都非常简单，克隆代码后运行 npm install、npm start 即可。

如果你的 Touch Bar 也没有发挥什么作用，不妨安装这个小工具试用一下。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/spagnuolocarmine/touchbar-systemmonitor
