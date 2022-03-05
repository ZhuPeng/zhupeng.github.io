---
layout: post
title: 用于 API 访问的 TOKEN 设计需要考虑什么
tags: GitHub，安全
---

大家好。

任何一个系统如果有对外提供服务的需求，会选择开放 API，同时也会配套需要管理调用方，通常我们都使用派发 TOKEN 的形式识别不同的调用方。这里面虽然认证方式有很多种，但无疑 TOKEN 的设计也是一门学问。

最近刚好看到 GitHub 在更换之前已经派发的 TOKEN 格式，让调用方修改 TOKEN 是一个极其困难的操作，但是为什么 GitHub 还是要坚持这样做呢？其实最大的原因是很多派发的 TOKEN 已经泄露，甚至很多的开源项目作者将 TOKEN 直接存储在 GitHub 的项目中，这样就等于公开了。你可能不知道，在以前有很多的厂商会监听 GitHub 开源项目的变更，截取项目中暴露的 TOKEN 牟取暴利。

为了安全，GitHub 也在开源项目代码提交后自动检测代码中可能包含的 TOKEN，如果发现 TOKEN 是自家的，就会自动使原 TOKEN 失效。但是因为原来 GitHub 的 TOKEN 是一个完全随机的字符串，这样在识别和检测效率上造成了极大难度，需要在众多的 TOKEN 数据库中比对，这已经恶化到了比较严重的地步。

所以 GitHub 就重新设计了其 TOKEN 格式，我们来看看他们是如何考虑并设计的。

1、可识别的前缀

TOKEN 增加了公司标识的前缀，使得自家 TOKEN 识别变得非常的简单，以下是根据不同的使用场景，定义的不同的前缀。

![image-20220219224518701](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220219224518701.png)

使用 _ 下划线作为 TOKEN 不同部分的连接，下划线有如下好处：下划线不是 base64 字符，所以不用担心与自然生成的 base64 字符重复；下划线连接的字符，在网页上鼠标双击时能够直接选中，而中横线是会自动分词的，大家可以试一下 this-random-text 和 this_random_text 的不同效果。

2、Checksum 校验和

Checksum 能够使得 TOKEN 能够离线验证其正确性，避免每次 TOKEN 的验证都通过数据库，给数据库带来不必要的压力。GitHub 使用 CRC32 算法作为校验和的算法。

3、TOKEN 熵（entropy）

TOKEN 熵是一种计算 TOKEN 组成上信息不确定性的方法，简单一点说，就是将 TOKEN 能够生成的数量规模用一个数字来表示，数值越大表示能够生成规模更大的 TOKEN 数量。GitHub 每天生成的 TOKEN 数量范围在 10K ~ 18K。本次重新设计的 TOKEN 熵从 160 增加到了 178。

![image-20220219225702705](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220219225702705.png)

以上就是 GitHub 重新设计 TOKEN 格式考虑的三点，是否对你有一些启发呢？

更多项目详情请查看如下链接：https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/