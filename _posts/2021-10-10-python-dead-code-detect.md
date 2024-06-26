---
layout: post
title: 这里有一个办法，为历史遗留的项目减负！
tags: Python
---

大家好。

大家应该知道，一个项目存在的时间越长，其因历史原因导致的问题就越多，而且很多可能都无从追溯当时的背景。从我多次接手其他人项目的经验来看，我发现一个显著的特点，项目虽然很复杂，但是往往项目中有很多的历史代码可能并没有在使用，它只是安静的躺在那里，反而增加了项目的复杂度。

当然删除没有在使用的历史代码并没有那么容易，可能会引发一些不必要的问题。但是如果不删除的话，当你在了解这个项目的时候可能也会非常的费劲，所以有没有自动化的方式来检测一个项目历史未使用代码的大致数量，然后在保证安全的前提下，最大可能的删除不用的代码，减轻项目的负担。

今天要推荐的项目 vulture 就是一个 Python 的 Dead Code 自动化监测工具，Dead Code 可以理解为就是项目中根本没有在使用的代码。vulture 除了可以用在对历史的大仓库进行检查外，也可以集成到你的日常持续集成流程中，因为每一次的 Dead Code 的生成都是因为修改导致的一些代码变成了违背引用的孤岛，所以保证没有增量 Dead Code 是很有必要的。

vulture 也是一个 Python 的项目，所以使用 Pip 即可安装，安装后使用也比较简单，如下：

![image-20211010221933730](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20211010221933730.png)

以下是一个使用例子。

![image-20211010221955349](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20211010221955349.png)

从例子可以看出来能够比较方便的检测出来未被使用的模块、函数和变量等，这些如果不及时的删除，都是未来项目的技术债。

vulture 的原理是这样，通过使用 ast 库对制定源码文件构建抽象语法树，然后遍历所有的语法树，记录使用的对象，这样就可以找到未被使用的对象。整体来看大致的扫描规则有点像垃圾回收算法，原理都是相通的，但是具体的场景会有些差异。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/jendrikseipp/vulture
