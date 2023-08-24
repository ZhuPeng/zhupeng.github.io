---
layout: post
title: GitHub 开源项目 rulego/rulego 介绍，RuleGo is a lightweight, high-performance, embedded rule engine based on Go language.  It can aggregate, distribute, filter, transform, enrich and execute various actions on input messages.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 rulego/rulego，该项目在 GitHub 有超过 93 Star，用一句话介绍该项目就是：“RuleGo is a lightweight, high-performance, embedded rule engine based on Go language.  It can aggregate, distribute, filter, transform, enrich and execute various actions on input messages.”。


![](https://raw.githubusercontent.com/rulego/rulego/master/doc/imgs/logo.png)
![](https://raw.githubusercontent.com/rulego/rulego/master/doc/imgs/rulechain/img_1.png)
![](https://raw.githubusercontent.com/rulego/rulego/master/doc/imgs/rulechain/img_1.png)
![](https://raw.githubusercontent.com/rulego/rulego/master/doc/imgs/rulechain/img_2.png)
![](https://raw.githubusercontent.com/rulego/rulego/master/doc/imgs/rulechain/img_3.png)
![](https://raw.githubusercontent.com/rulego/rulego/master/doc/imgs/rulechain/img_4.png)







背景介绍：
在处理大量数据时，我们经常需要对数据进行聚合、分发、过滤、转换、丰富和执行各种操作。而RuleGo是一个基于Go语言的轻量级、高性能、嵌入式规则引擎，可以帮助我们解决这些问题。它可以在低成本设备上高效地处理和链接数据，适用于物联网边缘计算。同时，RuleGo还是一个灵活、高度可定制的事件处理框架，可以满足高度个性化或频繁变化的业务场景需求。

项目介绍：
RuleGo是一个基于编排的规则引擎，最擅长解耦系统。它采用协程池和对象池等技术，结合Go语言的高性能特性，可以在10W数据处理JS脚本过滤->JS脚本数据处理->HTTP推送的情况下，平均处理时间为9秒。同时，RuleGo支持将自己嵌入到现有项目中，非侵入式地利用其特性。所有业务逻辑都是组件化的，可以灵活配置和重用。你可以灵活地组合和重用不同的组件，以实现高度可定制和可扩展的业务流程。支持规则链的动态编排，你可以将你的业务封装成RuleGo组件，通过构建块实现高度变化的业务需求。同时，RuleGo提供了丰富灵活的扩展接口和钩子，如：自定义组件、组件注册管理、规则链DSL解析器、协程池、规则节点消息流入/流出回调、规则链处理结束回调等。支持通过Go插件动态加载组件和扩展组件。内置常用组件包括：消息类型切换、JavaScript切换、JavaScript过滤器、JavaScript转换器、HTTP推送、MQTT推送、发送电子邮件、日志记录等组件。你也可以自己扩展其他组件。同时，RuleGo还具有可靠的上下文隔离机制，无需担心高并发情况下的数据流问题。

如何使用：
你可以通过以下步骤安装和使用RuleGo：
1. 安装Go语言环境
2. 执行命令：go get github.com/rulego/rulego
3. 在你的代码中引入RuleGo包
4. 编写规则链，进行业务处理
如果你想了解更多使用方法，可以参考项目文档中的示例代码。

项目推介：
RuleGo是一个非常优秀的开源项目，它的开发活跃度很高，已经获得了很多开发者的认可和使用。它还被一些知名公司和业内知名人士推荐使用，如：美团、华为、阿里巴巴等。如果你需要一个高性能、灵活、可定制的规则引擎，RuleGo将是一个非常好的选择。





以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=rulego/rulego&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/rulego/rulego 

开源项目作者：rulego

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=rulego/rulego)

关注我们，一起探索有意思的开源项目。

