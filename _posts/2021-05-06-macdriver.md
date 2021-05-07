---
layout: post
title: 开发一款 MacOS 应用需要了解哪些知识？
tags: Go
---

大家好。

如果要开发一款 MacOS 应用需要具备哪些知识？要学习 Objective-C？不知如何开始？

今天推荐一个 Go 封装的框架 MacDriver，支持原生的 Mac API，只需要 80 行代码即可实现一个 MacOS 菜单栏的「番茄时钟」应用。

![image-20210506212031408](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210506212031408.png)

目前 MacDriver 框架包含两部分：

1、Objective-C 的绑定

objc 包包含了 Objective-C 运行时，可以动态的与 Objective-C 的对象和类交互。

![image-20210506212249220](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210506212249220.png)

2、框架包

`cocoa`, `webkit`, and `core` 包通过基于 `objc` 包来实现 Apple/Mac 的 APIs。以下是一个简单的示例：

![image-20210506212507910](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210506212507910.png)

 整体使用起来比较简单，我们来看下用 80 行代码实现的番茄时钟应用。

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_macdriver.fanqie.png)

具体效果如下：

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/pomodoro.gif)

是不是还挺简单的？更多项目详情请查看如下链接，快去开启你的 MacOS 应用开发之路吧。

开源项目地址：https://github.com/progrium/macdriver
