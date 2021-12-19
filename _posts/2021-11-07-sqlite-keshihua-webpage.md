---
layout: post
title: 简单好用的开源 SQLite 查询工具
tags: 前端
---

大家好。

今天推荐一个开源的 SQLite 可视化查询工具 sqliteviz，sqliteviz 是一个单页的网页应用（PWA），可以离线使用，完全可以当成一个本地的 APP 来使用。

使用 sqliteviz 可以对本地的 SQLite 数据进行查询、使用  [Plotly](https://github.com/plotly/plotly.js) 画图等。从我的使用来看，sqliteviz 非常的轻巧，而且该有的功能都有，使用起来也没什么负担，随手就可以使用，不用安装任何应用。

以下是作者录制的使用视频，非常详细的介绍了 sqliteviz 各种特性。

<iframe width="100%" height="400" src="https://user-images.githubusercontent.com/24638357/128249848-f8fab0f5-9add-46e0-a9c1-dd5085a8623e.mp4" frameborder="0" allowfullscreen></iframe>
如果你想直接使用的话，完全不用自己去研究进行本地化部署，打开网站 https://lana-k.github.io/sqliteviz/ 即可开始使用。

![image-20211107234203726](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211107234203726.png)

除了可以自己创建单独的 SQLite 数据库外，也可以加载你本地已经有的数据库，而且是完全本地化的操作，不存在数据库被上传。点击如下图所示按钮可以加载本地数据库：

![image-20211107234320489](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211107234320489.png)

加载后就能直接使用 sql 进行查询了。

![image-20211107234536305](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20211107234536305.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lana-k/sqliteviz
