---
layout: post
title: 牛逼，快速为静态数据生成 API
tags: Python
---

大家好。

我们日常会有不少的静态数据，格式也有很多的种类，比如 excel、csv、json、sqlite 等，如果数据量很少的话，用默认软件打开是没什么问题的。但是只要数据量稍微多一点，比如 excel 有几万条数据，使用软件打开就会很慢很慢了，尤其有的时候还需要做一些复杂的查询操作。另外一个不方便的地方就是，如果这些静态数据你希望开放给其他人使用，或者是自己开发一个前端的展示网页，都需要对这些数据提供暴露的 API，单独去开发的话还是比较费时费力的。

今天要推荐的一个工具 roapi，能为静态数据快速的生成可读的开放 API，其中 API 的查询形式支持种类非常多，比如 rest API、SQL 查询、GraphQL。下图就是工具 roapi 的整体的交互流程图。

![image-20211205230509461](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20211205230509461.png)

roapi 工具主要分为 4 部分，分别是查询层、查询计划执行层、数据层和数据返回层。大致的流程是前端的查询层通过不同的查询方式，会在查询计划执行层生成不同的执行计划，并最终在数据上执行查询。而不同的数据格式都会统一抽象为单独的数据抽象层，以便屏蔽不同的数据格式的差异。

使用 pip install roapi-http 就可以安装开始使用。下图就是具体的使用方式了，可以说是非常的简洁和方便了。

![image-20211205231229305](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20211205231229305.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/roapi/roapi
