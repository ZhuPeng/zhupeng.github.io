---
layout: post
title: GitHub Issue 自动翻译机器人
tags: 投稿
---

今天的文章是来自一个读者的投稿，介绍的工具非常的棒。作者：https://github.com/tomsun28

Hi，之前在公众号上看到了个[教大家免费获取一台 Mac 来用，真是机智](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&tempkey=MTA5OV9oNkxlMk9NMmNWVERPWStZTkhRUlpZak9aNUtCZXhvLWtkcjR2N1M4TnFvNlRpY0h3YUVhYTRCWUtsWi1xc3JpbEtQanRZSWRhUlFIYTZ3ZGhibDNnOFdGbGhEOElQWXZFWGNBV3dXOE5Jd2ZOQ0xsMno1VlpSMml1SGFNM0E2SWZXWFdjTFdqcG56ME9ZRXR2dEN6Um50SktKYzBTTmpNd2tGbnBRfn4%3D&chksm=0885131a3ff29a0c696574d69221dd62483f1c1ad32e1e02ae3cb5c586c77268037ec17228e8&__mpa_temp_link_flag=1&token=1243173053#rd)的文章，突然想起了自己之前没事做的自动识别翻译非英文 issues 的 github action。  

有些大佬同学拥有知名的开源项目(显然我还没有)，可能有时候会收到来自泰国新加坡印度尼西亚的同学的母语祝福 issues，显然我们是看不懂需要手动 google 翻译，如果这时候有个机器人能自动识别非英文的 issues 把他翻译出来那感觉还是不错的。

先上效果：

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_issue-demo.png)   

这个 action 的原理也比较简单，issue 动作触发 action，读取 issue comment 内容，对其判断是否是英文，若不是则翻译出来，再调用 github api 评论一条翻译英文 issue，然后再考虑下边界和死循环等。  

咋使用呢，到 github action 市场搜索 Issues Translator，里面就有对应的使用方法。或者直接在项目的`.github/workflows/` 下创建 `issues-translator.yml`，填入以下内容：  

![image-20210203213426744](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210203213426744.png)

以上配置会使用默认提供的账号机器人：@Issues-translate-bot，如果你需要单独设置账号可参考如下方式：

![image-20210203212323267](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210203212323267.png)

配置完就 OK 了，接下来就是要等泰国新加坡印度尼西亚（哈哈，注意音乐节奏，其实是主要的外语都支持）的朋友们来祝福你了哦！  

更多项目详情请查看： https://github.com/marketplace/actions/issues-translator 
