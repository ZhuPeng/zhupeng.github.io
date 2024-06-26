---
layout: post
title: Go 语言整洁架构代码模板
tags: Go 架构设计
---

大家好。

今天推荐的项目跟整洁架构相关，在介绍之前我们先引用以下提出这个概念的作者 Robert C. Marti 的一句话：

“软件架构的目标是最大限度地减少构建和维护所需系统所需的人力资源。” - Robert C. Marti

简单理解就是架构是希望让软件更容易构建，同时随着代码开发的时间增加，依然很容易维护。但是在真实的工作中，以上两项看似简单的要求，其实非常难做到，如果你也维护过像面条一样纠缠不清的项目代码，相信你一定深有体会在老旧项目上加代码有多难。我们对很多老旧项目的要求一再降低，甚至只要求它能够运行即可，但是黑天鹅事件还是会发生，它有一天会突然不能运行了。

整洁架构就试图来解决上面的这些问题，通过将软件进行分层，且层之间依赖的是接口而不是具体的实现，这样使得程序的结构更加的清晰，同时升级和维护也变得非常十分容易，更改某层的具体实现代码，只要接口保持稳定，其他层是不需要更改的。

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_clean.arti.jingdian.png)

以上就是整洁架构中比较经典的示例图。今天要推荐的项目是 go-clean-template，是一个基于 Go 语言搭建的整洁架构的代码模板，go-clean-template 项目试图去解决如下三个问题：

![image-20220605203137911](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220605203137911.png)

简单翻译就是：

1、试图告诉你如何组织一个项目，避免其变成难以维护的面条代码

2、业务逻辑代码应该如何存放，使其能够保持独立、整洁和可扩展

3、当微服务数量爆炸式增长时，如何应对避免失去控制

以下是该模板对应的项目结构：

![image-20220605203510375](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220605203510375.png)

该项目中对具体的目录有单独的解释，同时对依赖的注入有单独的篇章进行介绍。更多项目详情请查看如下链接。

开源项目地址：https://github.com/evrone/go-clean-template

开源项目作者：evrone
