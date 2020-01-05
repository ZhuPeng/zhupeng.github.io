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



**推荐阅读**

* [腾讯开源又一力作，刚开源，标星已超 3.3k](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984653&idx=1&sn=6f65a44dfc3989b529c6f476bb15fff2&chksm=88852e40bff2a756c6dd4a5509bc3aa06b6614f90e0b4d2a29ba2824993fb3a7f9f15e109310&token=401905435&lang=zh_CN#rd)
* [标星近 2K 的常用正则大全，前后端程序员必备的工具](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984648&idx=1&sn=c91e844ae1a6cc812a36040c0717d464&chksm=88852e45bff2a75302b5efe28d7295eb15a8439fc3f1693279488f2181bbbd79a23cd40fabfe&token=401905435&lang=zh_CN#rd)
* [牛逼，超过 290 家公司使用的开源任务调度系统](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984643&idx=1&sn=b68209f670cb14e5b78e568373263505&chksm=88852e4ebff2a7588c24c2afe9d14a87b3e462c7b82974924e1ba26053f8e249ce6e16a5d362&token=401905435&lang=zh_CN#rd)
* [Android 开发者的福利，介绍几款看源码的工具](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984638&idx=1&sn=a61f07e7aae09813feb6b297abd84f39&chksm=88852db3bff2a4a52417f87d3567fd808422763b04adf4a5f6d9b7e3a31e64f29015690dd006&token=401905435&lang=zh_CN#rd)