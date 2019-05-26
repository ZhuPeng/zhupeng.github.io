GitHub 上的很多开源项目都会在 Readme 的开头增加徽章标识一些信息，如 CI 是否通过、代码覆盖率等等。除了徽章，还有一些图表，比如项目的 Star 趋势图。他们都是怎么添加的呢？接下来将会一一介绍。



## Travis-CI 状态徽章

使用 GitHub 账号登陆了 Travis CI 之后，可以对账户下面的任意项目关联 Travis，同时在项目的右上角有一个徽章，点击就可以获取徽章的链接，直接添加到仓库的 Readme 即可。

![image-20190526215451899](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/githubbadge/travisci.png)



## 任意徽章

![image-20190526215633525](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/githubbadge/badge.png)

[Shields.io](https://shields.io/) 提供了很多定制化徽章的功能，比如持续集成状态，包的上传和分发，社交网络，代码覆盖率等等，该网站目前每个月会有 4.7 亿次徽章图片的请求。你可以在网站 <https://shields.io/> 定制任意你喜欢的徽章。

![image-20190526220010988](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/githubbadge/shields.png)

> 项目地址：<https://github.com/badges/shields>



## Star 趋势图

一个项目的 Star 数一定程度上说明了该项目的受欢迎程度，而对应的 Star 的增长趋势则可以看出项目的发展历程，比如已经持续开发时长、最近是否活跃等。

![image-20190526220121418](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub%E7%B2%BE%E9%80%89/githubbadge/star_change.png)

使用地址 ```https://starchart.cc/<用户名>/<仓库名>.svg``` 可以生成任意项目的 svg 图。

> 项目地址：<https://github.com/caarlos0/starcharts>



## 个人贡献板

在 GitHub 的账户 Profile 页面能看到个人最近一年的社区贡献情况，但是对应的贡献板是没有办法分享给其他人的。通过地址 ```https://ghchart.rshah.org/<用户名>``` 生成 svg 图片链接可以在任何地方分享。

![](https://camo.githubusercontent.com/119d567c70c8a919f4d698c57458936761ffd969/687474703a2f2f676863686172742e72736861682e6f72672f323031367273686168)

之前看到有通过机器人自动提交代码，来生成酷炫的贡献板，下图需要连续提交一年才会有如此效果，真是服气。

![](https://user-images.githubusercontent.com/19748456/50627104-dff87f00-0f6c-11e9-8c27-c158bd3c7288.png)

> 项目地址：<https://github.com/2016rshah/githubchart-api>