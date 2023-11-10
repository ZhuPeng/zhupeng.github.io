---
layout: post
title: 交互式命令行工具开发神器
tags: Go 命令行
---

大家好。

程序员难免要跟命令行工具打交道，命令行工具除了基本的输入和输出结果以外，有时候还需要一些必要的交互，比如选择、进度条等，如果要自己去开发类似的功能，困难还是非常大的。

今天要推荐一个工具库 infinite，提供了开箱即用的命令行交互式组件库，它提供了一些常用的交互式组件，比如说`progress`，`progress group`，`mulit select`，`input text`，`confirm`等。同时也提供了一些更基础的组件，方便用户进行组合使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/infinite.demo.gif)

以上就是具体的使用效果，而要实现上面的效果，具体的代码也非常的简单，以下就是一个实现多选交互的代码，差不多 10 行代码。

![image-20220821202319067](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220821202319067.png)

infinite 的功能还是非常强大的，以下是项目提供的功能列表：

![image-20220821202355512](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220821202355512.png)

infinite 目前还是一个新项目，使用 Go 语言开发，虽然 Star 数量不多，但是亮点就是易于使用，定制化能力强，线程安全。更多项目详情请查看如下链接。

开源项目地址：https://github.com/fzdwx/infinite

开源项目作者：[fzdwx](https://github.com/fzdwx)

关注我们，一起探索有意思的开源项目。
