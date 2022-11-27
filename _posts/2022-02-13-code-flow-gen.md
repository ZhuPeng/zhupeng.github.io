---
layout: post
title: 动态语言调用关系生成器，阅读代码效率大提升
tags: 效率
---

大家好。

动态编程语言有很多的好处，但是一旦项目越来越大，维护成本就会变动越来越高。同时如果项目上的调用关系变得复杂起来之后，不管是改动旧代码或者新同学上手都比较困难。而要优化以上问题，对项目的调用关系有清晰的认识是非常重要的。

今天要推荐的项目 code2flow，能够自动分析项目的代码，并生成清晰优雅的函数调用关系。

![image-20220213223134125](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220213223134125.png)

Code2flow 目前支持 Python, Javascript, Ruby, and PHP 语言。大致原理是分析源码并生成 AST 语法树，再找到函数的定义，并将函数的调用进行连接。

![image-20220213223317455](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220213223317455.png)

那么 Code2flow 能用来干什么呢？总结下来主要有以下三大用处：

1、理清项目中的调用关系

2、识别孤儿（未被调用的）函数

3、帮助新同学快速上手项目

以下是通过 Code2flow 生成的一个项目函数调用示例图：

![code2flow running against a subset of itself](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_alive.process.demo.png)

大家对 Code2flow 感兴趣的话，可以了解 Code2flow 的生成算法是怎样，如下描述：

![image-20220213223702183](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220213223702183.png)

虽然 Code2flow 工具非常的棒，但是因为其作用的是动态语言，Code2flow 依然是有非常多的限制的，在这些情况下会造成 Code2flow 不能正常的工作。总结包含如下限制：

![image-20220213223848184](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220213223848184.png)

以上的限制其实都是来源于动态语言本身的特性，对分析调用关系造成了极大的难度。比如匿名函数，使用起来很方便，但是其跟正常的代码混合在一起，对调用关系的分析就很不友好。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/scottrogowski/code2flow
