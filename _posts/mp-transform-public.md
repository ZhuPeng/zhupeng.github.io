大家都知道我们的公众号文章会插入 GitHub 小程序，可以直接点击跳转，提升阅读体验？那么你们知道我们是如何添加的么？如果你想在你的文章中添加小程序链接，你知道如何操作么？

微信公众号后台编辑文章的过程中可以添加小程序，数了一下至少需要经过 6 步才能添加完成，有时候都不知道小程序的访问路径而不知道怎么操作。

今天要推荐的小程序排版小助手，帮助大家更方便的在公众号文章中添加小程序，借助 Chrome 插件提供一键轻松添加和排版小程序链接。你只需要在文章中填写浏览器上的链接，小助手将自动转化为小程序可以识别的链接，比如：`https://github.com/ZhuPeng/mp-githubtrending`

下载 Chrome 插件（阅读原文）：[下载链接](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/common/mp-transform.zip)，解压zip 压缩包，将 crx 后缀文件拖入 Chrome 浏览器，参考离线安装方法：[图文详解Chrome插件离线安装方法 - 2019最新终极指南](<http://chromecj.com/utilities/2019-01/1791.html>)，安装完成后，浏览器右上角将出现如下 Logo。

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/common/link-128.png)

安装完成之后，进入微信公众号文章编辑页面，操作效果如下：

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/common/wechat-editor.PNG)
![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/common/wechat-xiaoguo.PNG)


## 已支持的小程序列表

* [GitHub Trending Hub](<https://github.com/ZhuPeng/mp-githubtrending>)
* [Readhub](https://readhub.cn/topics)
* [哔哩哔哩](https://www.bilibili.com/)
* [腾讯视频](https://v.qq.com/)
* [CSDN](https://blog.csdn.net/)
* [简书](https://www.jianshu.com/)
* [知乎热榜](https://www.zhihu.com)、[知乎专栏](https://zhuanlan.zhihu.com)
* [什么值得买](https://www.smzdm.com)
* [百度网盘](https://pan.baidu.com): 分享链接为 https://pan.baidu.com/s/<随机字符串>，需要在末尾添加 #提取码#0#0，例如：https://pan.baidu.com/s/1EuJiHB-q2Lggrt28cjQISA#3tb7#0#0 
* [36氪Lite](https://36kr.com)
* [掘金第三方版](https://juejin.im)
* [V2EX For You](https://www.v2ex.com)

其他小程序的支持正在开发中，如果你的小程序希望接入，欢迎提交 PR。



##  小程序跳转

如果你是小程序开发人员，希望自己的小程序也能跳转如上小程序，可以复制仓库中的 [multimp.js](multimp.js) 到你的小程序源码中，具体使用方式可以参考：[链接代码](https://github.com/ZhuPeng/mp-githubtrending/blob/master/pages/component/md/md.js#L94)，同时你需要在小程序的 `app.json` 中添加允许跳转的小程序列表参数 `navigateToMiniProgramAppIdList`，[参考链接代码](https://github.com/ZhuPeng/mp-githubtrending/blob/master/app.json#L60)。



> 项目地址：[https://github.com/ZhuPeng/mp-transform-public](https://github.com/ZhuPeng/mp-transform-public)