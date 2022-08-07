---
layout: post
title: 统一免费 API 访问方式的工具，让 API 使用更简单
tags: API
---

大家好。

之前给大家分享过[免费开放的 API 大全](https://mp.weixin.qq.com/s?__biz=MzAwMzE5NzM2Nw==&mid=2247485355&idx=1&sn=9a4d792a35c3548a4d9243469e2b8744&chksm=9b3f9773ac481e655592a9366dcad80679891627e269b20278c7e684ef15002b2e6d8bd122cf&token=184134385&lang=zh_CN#rd)，各种免费的 API 种类非常的全，是用来快速开发应用软件的利器。但是有一个问题，每一类的 API 的访问方式、加密授权方式、返回体类型等都不太一样，这就造成了使用每一类的 API 都要单独编写代码，这还是很麻烦的。

今天要推荐的一个开源项目 m3o，借助网关建设的相关能力，将开放免费的 API 的访问进行统一，这样让使用方可以很轻松的用统一的方式对 API 进行请求和返回的解析，绝对是生产力的提升，对应 API 的使用方来说，就如同使用同一个产品的 API 一样，如丝般顺滑。

![image-20220711001532581](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220711001532581.png)

目前 m3o 支持了超过 60+ API，覆盖了软件开发的方方面面，包括云基础设施、地理位置、通信工具等。

![image-20220711001839518](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220711001839518.png)

对 API 的使用和访问都是统一的方式，如下就是其中 Go 的一个例子。

![image-20220711002009478](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220711002009478.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/m3o/m3o

开源项目作者：m3o