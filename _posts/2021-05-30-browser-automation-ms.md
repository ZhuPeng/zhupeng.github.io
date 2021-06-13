---
layout: post
title: 微软开源浏览器自动化工具
tags: Python
---

大家好。

你们平常用的浏览器自动化工具是什么？比较出名的是 Selenium，用过的大家应该知道。另外还有一个比较出名的是 PhantomJS，针对的是无界面的浏览器。这类工具能够通过代码的形式，控制浏览器自动完成一系列操作，不过是用来做爬虫或者是自动化的测试，都非常的方便。

今天要推荐一个类似的工具，Playwright for Python，它是由微软开源的，毕竟大厂出品，我们一起来看看它有什么神奇的地方。

首先 Playwright 支持以下类型的浏览器，主流的基本都覆盖了。

![image-20210530222717064](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210530222717064.png)

Playwright 使用上非常简单，而且代码也很简洁，目前支持同步和异步调用两种方式。

同步方式：

![image-20210530222847286](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210530222847286.png)

异步方式：

![image-20210530222916027](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210530222916027.png)

最后介绍一下 Playwright 最牛逼的一个功能，它能够自动根据你在浏览器上的操作生成对应的代码，简直不要太好用。以下是一个示例：

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/playwright.python.gif)

大厂出品就是不一样，从我整体的使用来看，Playwright 使用上要比 Selenium 和 PhantomJS 更简单的多，下次工作可以考虑使用 Playwright 了。更多项目详情请查看如下链接。

开源项目地址：https://github.com/microsoft/playwright-python
