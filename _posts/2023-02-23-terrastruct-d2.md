---
layout: post
title: 一款用于将文本转化成图表的现代化脚本语言
tags: 图表
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 terrastruct/d2，该项目在 GitHub 有超过 10.3k Star，用一句话介绍该项目就是：“D2 is a modern diagram scripting language that turns text to diagrams.”，一款用于将文本转化成图表的现代化脚本语言。

![](https://raw.githubusercontent.com/terrastruct/d2/master/./docs/assets/banner.png)

使用 D2 只需要使用如下代码就能够直接转换出流程图：

```yaml
# Actors
hans: Hans Niemann

defendants: {
  mc: Magnus Carlsen
  playmagnus: Play Magnus Group
  chesscom: Chess.com
  naka: Hikaru Nakamura

  mc -> playmagnus: Owns majority
  playmagnus <-> chesscom: Merger talks
  chesscom -> naka: Sponsoring
}

# Accusations
hans -> defendants: 'sueing for $100M'

# Offense
defendants.naka -> hans: Accused of cheating on his stream
defendants.mc -> hans: Lost then withdrew with accusations
defendants.chesscom -> hans: 72 page report of cheating
```

![](https://raw.githubusercontent.com/terrastruct/d2/master/./docs/assets/syntax.png)

d2 使用配置化的方式生成流程图的好处就是方便对流程图的历史进行记录，同时对于使用者来说，只需要掌握简单的语法就能快速的进行流程图的制作，另外对于程序员来说，批量生成流程图也是非常的方便的。

以下是一个示例视频：

<iframe width="100%" height="400" src="https://user-images.githubusercontent.com/3120367/206125010-bd1fea8e-248a-43e7-8f85-0bbfca0c6e2a.mp4" frameborder="0" allowfullscreen></iframe>
### 如何安装使用

要安装 d2 项目，您需要执行以下步骤：

```bash
# First, install D2
curl -fsSL https://d2lang.com/install.sh | sh -s --

echo 'x -> y -> z' > in.d2
d2 --watch in.d2 out.svg
```

使用 curl 下载安装脚本，运行 d2 程序后，会打开浏览器展示对应的流程图，而且对 in.d2 文件的修改会进行实时渲染。除此之外 d2 也可以作为依赖库，被你的其他程序引用使用，可以在仓库的 docs/examples/lib 位置查看示例代码。

使用网站 https://play.d2lang.com/ 可以直接进行试用。更多项目详情请查看如下链接。

开源项目地址：https://github.com/terrastruct/d2  (文末可点击阅读原文)

开源项目作者：d2

