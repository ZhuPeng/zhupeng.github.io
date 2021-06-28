---
layout: post
title: 高大上的云化系统架构图，写代码就能画出来
tags: Python
---

大家好。

现在越多越多的公司并没有自己自建的机房，都采用了云厂商的服务器，通常我们认为采用类似架构的系统为云化架构的。尤其是现在 Kubernetes 已经被越来越多的公司和云计算公司采用，这样对于采用云化架构的公司来说，使用云计算公司的服务器变得越来越简单，同时从一个云迁移到另一云也没有太多的适配成本。

而使用云化架构的公司如何画自己系统的架构图呢？今天要推荐的一个开源项目 Diagrams，就是帮助大家更好的描绘云化架构，而且不需要使用任何的设计工具，只需要写代码就可以了，对于写代码当然是工程师擅长的。

Diagrams 目前支持主流的云厂商，包括 `AWS`, `Azure`, `GCP`, `Kubernetes`, `Alibaba Cloud`, `Oracle Cloud` 等。同时支持一些内置的架构图组件、SaaS 和主流的编程框架和语言。

我们来看下实际的效果：

![image-20210606230218833](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210606230218833.png)

![image-20210606230229610](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210606230229610.png)

![image-20210606230335031](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210606230335031.png)

由于 Diagrams 采用代码的形式描绘云化架构图，所以所有的变更都可以方便的使用版本控制系统去管理，比如使用 Git 管理。

从代码的结构来看整体使用起来也比较简单，基本是先声明所有的节点，再根据指向关系链接成对应的架构图，非常的方便。

![image-20210606230542062](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210606230542062.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/mingrammer/diagrams
