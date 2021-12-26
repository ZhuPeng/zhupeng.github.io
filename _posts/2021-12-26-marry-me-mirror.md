---
layout: post
title: 程序员的浪漫 - Marry Me 魔镜
tags: Python
---

大家好。

程序员一直被人说是直男，不够浪漫，但是我一直认为浪不浪漫其实跟职业关系不大，更多的是跟人有关，每个行业都有浪漫的人。

今天的推送就是一个关于程序员的浪漫，这个程序员做了一面魔镜，经过光的照射可以反射出 Marry Me，如果用来求婚是非常的浪漫了。以下是效果图：

![image-20211226205539381](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211226205539381.png)

作者同时是一个喜欢开源的程序员，所以他把自己如何制作这块魔镜的原理，以及对应的 3D STL 文件都开源了，如果大家家里有 3D 打印机是可以直接下载下来打印的。

我这边简单介绍一下大致的原理，太阳光经过镜子的反射可以形成一个光点，下面就是对应的反射原理，这个还是比较好理解的。

![image-20211226210010534](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211226210010534.png)

而多个镜子的不同角度的组合，对应形成的光点就可以进行组合。

![image-20211226210203180](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211226210203180.png)

最终经过严格的计算，就能实现通过亮点组合成文字的效果。

![image-20211226210238583](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211226210238583.png)

是不是还挺有趣的？

更多项目详情请查看如下链接。

开源项目地址：https://github.com/bencbartlett/3D-printed-mirror-array
