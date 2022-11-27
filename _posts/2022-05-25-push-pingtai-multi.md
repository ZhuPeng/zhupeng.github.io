---
layout: post
title: 真强大，多渠道消息推送平台推荐
tags: Java
---

大家好。

个人开发者或者公司如果维护了一些客户系统，一定有很多的消息需要推送，但是现在可以接受消息的系统真的太多了，比如邮件、短信、IM、微信等。如果都是自己去开发对应的消息推送系统，对个人开发者来说不太现实，个人开发者的做事方式也是能复用绝对不造一个新轮子。

今天要推荐的开源项目 austin，就是一个能够使用统一的接口发送各种类型消息，对消息生命周期全链路追踪的系统。

![image-20220529234516843](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220529234516843.png)

这个项目的意义是：只要公司内有发送消息的需求，都应该要有类似 austin 的项目，对各类消息进行统一发送处理。这有利于对功能的收拢，以及提高业务需求开发的效率。

以下是 austin 的项目架构：

![image-20220529234638470](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220529234638470.png)

austin 使用 Java 进行开发，有独立的管理界面，同时支持多种消息类型，比如定时等，目前支持的消息推送应用包括如下：企业微信、短信、邮件、IM、小程序、钉钉等，基本覆盖了市面上常见的应用。

以下是对应的管理界面，包括消息的模板管理、消息的链路追踪等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_austin.temp.admin.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_austin.trace.msg.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/ZhongFuCheng3y/austin

开源项目作者：ZhongFuCheng3y