之前分享过一款去哪儿网开源的[API 可视化管理工具](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984374&idx=1&sn=9f7d49a459683824b685bfaefcf388e3&chksm=88852cbbbff2a5ad51889d80d8ab3d795aa88e84dfeaa7258810a46f556e517f2515127dd6f1&token=313338326&lang=zh_CN#rd)，被很大的公司采纳使用。今天推荐一个类似的工具，由阿里妈妈MUX团队出品，给大家多一个选择。

为什么频繁推荐这些工具呢？因为在我的认识里，效率在工作中真的非常重要，高和低真的相差太多了，不仅仅早下班晚下班的事情，效率低还很影响心情。

一个典型的场景就是前后端联调了，如果没有方便的接口管理工具，前后端联调势必会有很多的沟通、协调，效率低下不说，甚至有可能延迟交付。

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/images/ali.rap.dev.test.png)

阿里妈妈出品的 RAP 通过 GUI 工具帮助 WEB 工程师更高效的管理接口文档，同时通过分析接口结构自动生成 Mock 数据、校验真实接口的正确性，使接口文档成为开发流程中的强依赖。有了结构化的 API 数据，RAP 可以做的更多，而我们可以避免更多重复劳动。

为什么我们信赖 RAP？

- 企业级应用，包括阿里集团在内得 350 多个企业都在使用RAP管理重要的接口文档。
- 快速高效的技术支持，持续的更新，去 Issues 看一看就知道有多热闹。
- 免费、开源，一切尽在掌握中！



该项目目前有两个版本：

https://github.com/thx/RAP 该项目已暂停维护

https://github.com/thx/rap2-delos RAP 第二代，RAP2 是在 RAP1 基础上重做的新项目，它能给你提供方便的接口文档管理、Mock、导出等功能，包含两个组件(对应两个 Github Repository)。

- rap2-delos: 后端数据 API 服务器，基于 Koa + MySQL [link](http://github.com/thx/rap2-delos)
- rap2-dolores: 前端静态资源，基于 React [link](http://github.com/thx/rap2-dolores)

如果想直接体验使用，可以通过网站：**[rap2.taobao.org](http://rap2.taobao.org/)**

![image-20191229212448957](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/images/ali.rap.png)