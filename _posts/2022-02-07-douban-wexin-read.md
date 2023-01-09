---
layout: post
title: 微信读书必备插件，展示豆瓣可读书籍
tags: Chrome 插件
---

大家好。

微信读书不知道大家用不用，我用的比较多，相比其他读书 APP，我觉得微信读书简直就是神器，而且很多书籍都是可以直接免费阅读的。微信读书通过打卡或者购买包月服务（不贵）就可以无限畅读任意的书籍，简直太爽了。

而老牌的豆瓣读书，各种书籍的推荐榜单，能够帮助我们很好的找到喜欢的书籍。但是豆瓣读书是没办法直接阅读的，需要你自己去找可以阅读的方式。

所以如果微信读书和豆瓣读书能够结合一下，那简直就是神器。今天要推荐的就是这样一个 Chrome 插件 weReaDou，能够在豆瓣读书的网站上直接展示微信读书可读的链接，帮助我们一键快速阅读。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_weixindushu.link.png)

从上图也可以看出来，右侧展示的微信读书链接跟豆瓣读书的网页非常完美的结合在一起，简直就跟网站本身提供的功能一样。

weReaDou 的实现原理是借助微信读书提供的 API，同时依靠 Chrome 插件提供的定制能力，在网页加载后查询对应的图书是否被微信收录。

![image-20220207164954294](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220207164954294.png)

如果图书没有被微信读书收录的话，会展示如下信息。

![image-20220207165212738](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220207165212738.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Sorosliu1029/weReaDou
