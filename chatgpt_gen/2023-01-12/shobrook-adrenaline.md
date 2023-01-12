大家好，又见面了，我是 GitHub 精选君！

最近 ChatGPT 非常的火，而且是火出圈的那种，各个领域的人都知道。但是不得不说程序员做的工具，对程序员还是有些特殊的用途的，比如可以直接用来生成代码、修复代码 bug 等等。

今天就要推荐一个基于 GPT-3 构建的工具 adrenaline，可以用来直接修复代码问题，同时告诉你为什么这是一个 bug 的应用，而 ChatGPT 在 GPT-3 面前就是个弟弟，以下是 ChatGPT 告诉我的，它和 GPT-3 的关系，你们感受一下。

![image-20230112234357558](/Users/zhupeng/Library/Application Support/typora-user-images/image-20230112234357558.png)

简单理解就是 GPT-3 是一个通用的模型，而 ChatGPT 是一个专用的模型，主要用来做聊天对话。

以下就是 adrenaline 的使用 demo，可以 Lint、Debug 以及对应的 Error 解释，体验非常的极致了。

![](./demo.gif)

访问网站可以体验：https://useadrenaline.com/playground ，但比较遗憾的是需要使用 OpenAI 的 Token 才能试用。

![image-20230112234850897](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230112234850897.png)

adrenaline 还有很多不足，但是想法还是非常棒的，adrenaline 更多的是要证实使用 AI 驱动是可以对代码进行 debug 和修复的。未来还有很多可以改进的地方，以下是作者列出来的，如果你感兴趣可以参与共建。

![image-20230112235106875](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20230112235106875.png)

### 如何安装使用

adrenaline 是一个网页应用，你可以将代码 clone 下来在本地做一些改动。以下是安装和使用方法：

```bash
$ npm install
$ npm run start-local
```

更多项目详情请查看如下链接。

开源项目地址：https://github.com/shobrook/adrenaline

开源项目作者：adrenaline

