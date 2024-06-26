---
layout: post
title: GitHub 精选开源项目周刊第0期
tags: 每周精选
---

前两天我们抱着忐忑的心情建了一个群，想试试看能不能帮助大家推广开源项目，我们也不知道能不能实现这个目标。不管怎么样，我们走出了这一步，不试试怎么知道呢。

所以，今天是一个特别的推送，推荐的开源项目来自我们的粉丝推荐。

## 人工生命

**项目介绍：**

这是一个人工生命试验项目，最终目标是创建“有自我意识表现”的模拟生命体，技术架构基于02年提出的 一个人工脑模型。  这个项目永远没有结束的时候，开始于模拟一个简单的生命体，然后是青蛙、狗......，结束于有“自我意识表现”的人工脑，或者说，结束于被机器人代替人类的那一天。



**功能描述:**

点击可直接观看：https://www.bilibili.com/video/BV1xp4y1C7he/

**项目地址：**https://github.com/drinkjava2/frog

**项目作者：**[Drinkjava2 / 朱勇](https://github.com/drinkjava2)



## 深度学习框架

**项目介绍：**

一个基于 C++ 的自实现深度学习框架，可实现全连接层的前向传播和反向传播，详细已实现功能：

-  全连接层前向传播和反向传播接口,支持自动求导
-  矩阵微分和自动求导接口封装
-  矩阵广播机制,实现 padding 接口

实现的功能还有很多，反正就是功能超级多。目前项目还在开发阶段，希望有更多有兴趣的小伙伴加入我们，一起学习一起尝试。



**功能描述：**

构建全连接层：第一层的权重自定义,而后调用 forward 函数前向传播一层,自动求出激活以后的值,激活函数可自定义。

首先定义一个权重矩阵和偏置矩阵,第一个矩阵的维度大小使用数据列去定义:

Matrix bias1 = CreateRandMat(2,1);

Matrix weight1 = CreateRandMat(2,data.col);

之后可以输出第一层前向传播的值,同时可以定义下一层的bias的维度, row使用第一层的权重矩阵的行,第二层的权重矩阵的行使用了第一层的输出的行, 而列自行定义即可, 这一点体现了前向传播算法的维度相容。

非常高大上，咱也不敢问。



**项目地址：**https://github.com/AllenZYJ/Edge-Computing-Engine

**项目作者：[Edge](https://github.com/AllenZYJ)** 



## 能不能好好说话？

**项目介绍：**

一款拼音首字母缩写翻译工具。社交平台上通过拼音首字母缩写指代特定词句的情况越来越多，为了让常人勉强能理解这一门另类沟通方式、做了这一个划词翻译油猴脚本。对我们这种跟不上时代潮流的人来说，这个工具能够减少很多尴尬。

![image-20200416185102627](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20200416185102627.png)

我没有要开车~

项目地址：https://github.com/itorr/nbnhhsh

项目作者：[itorr](https://github.com/itorr)



## Json 数据生成代码工具

**项目介绍：**

JSONConverter 是MAC上iOS开发的辅助小工具，可以快速的把json数据转换生成对应的模型类属性，目前支持 Objective-C、Swift、Flutter 以及目前流行的第三方库: [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) 、[HandyJSON ](https://github.com/alibaba/HandyJSON)、[ObjectMapper ](https://github.com/Hearst-DD/ObjectMapper)，可以灵活选择构建class/struct，并支持配置类名前缀等,省去手敲模型的麻烦，借此提高我们的开发效率。详情看如下图：

![](https://camo.githubusercontent.com/154dc0908b90d75365463faacb69597ee5249488/68747470733a2f2f75706c6f61642d696d616765732e6a69616e7368752e696f2f75706c6f61645f696d616765732f323234303534392d383263353965646665326237383364312e706e673f696d6167654d6f6772322f6175746f2d6f7269656e742f7374726970253743696d61676556696577322f322f772f31323430)

项目地址：https://github.com/iosyaowei/JSONConverter

项目作者：[iosyaowei](https://github.com/iosyaowei)



以上就是本次推荐的全部项目。GitHub精选 公众号致力于为大家分享和宣传优质的开源项目，让更多的人了解和知道，乃至去使用大家的开源项目，一方面可以帮助大家提高影响力，另外一方面还有助于大家收获更多粉丝的支持。如果你有开项目需要分享，欢迎扫码进群或者直接在 https://www.yuque.com/loonggg/febxd7/wvs0z6 分享。

![image-20200416185439028](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20200416185439028.png)



