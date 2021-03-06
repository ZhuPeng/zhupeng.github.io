---
layout: post
title: GitHub 精选开源项目周刊第2期
tags: 每周精选
---

大家好，我是你们的章鱼猫。今天推送的是 GitHub 精选开源项目推荐周刊第 2 期，周刊内推荐的项目来自 GitHub 精选公众号粉丝的自荐，我们希望能够帮助更多的同学更好的开发和推广开源项目。

## 财经数据接口库 akshare
**项目介绍：**

AkShare 是基于 Python 的财经数据接口库，目的是实现对股票、期货、期权、基金、外汇、债券、指数、数字货币等金融产品的基本面数据、实时和历史行情数据、衍生数据等从数据采集、数据清洗到数据落地的一套工具。目前已经提供数百个数据接口

**功能描述:**

简单的使用代码如下：

import akshare as ak
hist_df = ak.stock_us_daily(symbol="AMZN")  # Get U.S. stock Amazon's price info
print(hist_df)

### 结果输出
```
               open     high      low    close   volume
date                                                   
1997-05-15    29.25    30.00    23.13    23.50  6013000
1997-05-16    23.63    23.75    20.50    20.75  1225000
1997-05-19    21.13    21.25    19.50    20.50   508900
1997-05-20    20.75    21.00    19.63    19.63   455600
1997-05-21    19.63    19.75    16.50    17.13  1571100
             ...      ...      ...      ...      ...
2020-02-24  2003.18  2039.30  1987.97  2009.29  6546997
2020-02-25  2026.42  2034.60  1958.42  1972.74  6219094
2020-02-26  1970.28  2014.67  1960.45  1979.59  5240402
2020-02-27  1934.38  1975.00  1882.76  1884.30  8143993
2020-02-28  1814.63  1889.76  1811.13  1883.75  9493797
[5731 rows x 5 columns]
```

**项目地址：**https://github.com/jindaxiang/akshare

**项目作者：** [Albert King](https://github.com/jindaxiang)

## Mars-java 声明式API框架
**项目介绍：**

Mars 是一个声明式 API 编程框架，可以帮助你很快的建立后端服务接口
你可以专注在业务逻辑上，而不需要花太多的时间去写 Controller 和 DAO
同时我们依然支持传统 Controller

**功能描述：**

* 声明式 API：只需要在 service 的父接口上加上一个注解，即可对外提供一个接口，并且还支持传统的Controller写法
* 组件化：目前正在开发一个新的项目Mars-component，提供了Mars-cloud，mars-extends，mars-users三个组件，可以完成分布式开发，工具包以及用户的基础操作，最终目标是打造一个完整的组件库，就像前端的bootstrap，elementUI一样，把不变的东西都写好，用的时候直接搭积木就好了
* 开放组件开发：除了我正在开发的官方组件，同时我们也把API开放给大家，欢迎所有人基于Mars-java来开发组件，一起完善这个生态
* 简洁的数据库操作：单表的增删改查，不需要写sql
* 数据校验：一个注解搞定
* 目前已经可用的生态：基于Mars-java开发后端服务，基于Mars-cloud组件开发微服务。其他组件尚未完善
官网地址：https://www.mars-framework.com/

**项目地址：**https://github.com/yuyenews/Mars

**项目作者：**[yuye](https://github.com/yuyenews)

## RT-THREAD 嵌入式操作系统
**项目介绍：**

RT-Thread诞生于2006年，是一款以开源、中立、社区化发展起来的物联网操作系统。 RT-Thread主要采用 C 语言编写，浅显易懂，且具有方便移植的特性（可快速移植到多种主流 MCU 及模组芯片上）。RT-Thread把面向对象的设计方法应用到实时系统设计中，使得代码风格优雅、架构清晰、系统模块化并且可裁剪性非常好。
RT-Thread有完整版和Nano版，对于资源受限的微控制器（MCU）系统，可通过简单易用的工具，裁剪出仅需要 3KB Flash、1.2KB RAM 内存资源的 NANO 内核版本；而相对资源丰富的物联网设备，可使用RT-Thread完整版，通过在线的软件包管理工具，配合系统配置工具实现直观快速的模块化裁剪，并且可以无缝地导入丰富的软件功能包，实现类似 Android 的图形界面及触摸滑动效果、智能语音交互效果等复杂功能。

**功能描述：**

RT-Thread是一个集实时操作系统（RTOS）内核、中间件组件的物联网操作系统，有如下特点：

* 资源占用极低，超低功耗设计，最小内核（Nano版本）仅需1.2KB RAM，3KB Flash。
* 组件丰富，繁荣发展的软件包生态 。
* 简单易用 ，优雅的代码风格，易于阅读、掌握。
* 高度可伸缩，优质的可伸缩的软件架构，松耦合，模块化，易于裁剪和扩展。
* 强大，支持高性能应用。
* 跨平台、芯片支持广泛。

**项目地址：**https://github.com/RT-Thread/rt-thread

**项目作者：**[BernardXiong](https://github.com/RT-Thread/rt-thread)

## BUIDL-区块链开发IDE
**项目介绍：**

BUIDL 是一站式的区块链应用开发工具。BUIDL 集合智能合约与Dapp（去中心化的应用）开发于一体，使区块链开发更加容易上手。BUIDL 默认连接Second State Devchain，极大地缩短了区块链确认时间，无 gas 费支出。
BUIDL 使区块链开发变得更加简单，提升了开发者效率。
使用地址：https://buidl.secondstate.io/
![](https://cdn.nlark.com/yuque/0/2020/png/1385017/1588736874591-6b7c00de-54b5-46f0-9f07-3b9b5191869c.png)

**功能描述：**
* 支持编写，编译和部署智能合约，支持编程语言：Solidity＆Lity
* 内置规则引擎，可以开发基于规则的智能合约
* 内置智能合约搜索引擎
* 以智能合约为基础，开发和运行JavaScript DApp, 且支持一键发布
* 内置区块链账号管理系统，为开发者省去大量准备工作
* 用户可以直接与BUIDL 开发出的 DApp 互动，无需下载区块链钱包
* 支持用户根据 RPC节点与 ChainId 自定义区块链系统

**项目地址：**https://github.com/second-state/buidl

**项目作者：**[wangshishuo](https://github.com/wangshishuo)

以上就是本次推荐的全部项目。GitHub精选 公众号致力于为大家分享和宣传优质的开源项目，让更多的人了解和知道，乃至去使用大家的开源项目，一方面可以帮助大家提高影响力，另外一方面还有助于大家收获更多粉丝的支持。如果你有开项目需要分享，欢迎点击 [共享文档](https://www.yuque.com/g/loonggg/febxd7/wvs0z6/collaborator/join?token=bVhhgBw5Rw0xM0Qj) 或底部阅读原文直接投稿分享。

**上期推荐：**

[GitHub 精选开源项目周刊第 1 期](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984989&idx=1&sn=aaec500b7374fd6dca20c539f0d6a8b7&chksm=88852f10bff2a606fd3da4bc6e177d4b02b1f8033adfd9a88ce718163947a0f576d2ffe7450a&token=148059737&lang=zh_CN#rd)

[GitHub 精选开源项目周刊第 0 期](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984989&idx=2&sn=ff43140e282ebe3640d713113fabfa3e&chksm=88852f10bff2a60671b08bcec38f406e5cd7ce029f3b57b5af2abcaffb3ea8f0fa2d2bc609be&token=148059737&lang=zh_CN#rd)