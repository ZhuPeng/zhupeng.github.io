---
layout: post
title: 跨平台支持软件快速安装并切换管理的工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当下繁忙的项目开发中，我们会在不同的开发项目间切换，这些项目可能需要不同的运行环境或者库。同时，这些环境的配置可能极其复杂，我们需要分别进行配置。这一系列的问题使我们的开发过程变得枯燥无趣，且极度消耗时间和精力。

今天要给大家推荐一个 GitHub 开源项目 version-fox/vfox，该项目在 GitHub 有超过 1.7k Star，一句话介绍该项目：A cross-platform and extendable version manager with support for Java, Node.js, Flutter, .Net & more

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406181040574.png)

###### 项目介绍

`vfox`支持跨平台操作系统（包括 Windows，Linux，macOS）并通过插件进行扩展的版本管理器 ( 类似于 `nvm`，`fvm`，`sdkman`，`asdf-vm`等）。它能够在切换不同的开发环境，并对环境进行安装的过程中，为你提供快速的命令行操作。平时我们在切换版本时，需要进行全局、项目、会话的版本切换，而这个过程在 `vfox` 中可以得到高效的解决。同时，`vfox` 同样提供了简单的插件系统，以便你添加支持选择的语言。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/650100.gif)

###### 如何使用

首先进行 `vfox` 的安装，然后将其放入你的 shell 中。注意选择适合你的 shell 的代码。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406181345976.png)

然后，你需要添加一个适应你需求的 SDK 插件。整个过程就完成了，简单快捷！具体使用示例如下:

```bash
$ vfox add nodejs/nodejs
$ vfox install nodejs@21.5.0
$ vfox use nodejs@21.5.0
$ node -v
21.5.0
```

以下是该项目的 RoadMap:

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240406181522527.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=version-fox/vfox&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/version-fox/vfox 

开源项目作者：version-fox

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=version-fox/vfox)

关注我们，一起探索有意思的开源项目。

