---
layout: post
title: GitHub 星标 14.7K！本地运行 GitHub Actions 的明星项目
tags: GitHub
---

大家好。

GitHub Actions 不知道大家是否了解，其实之前我们有过一些项目的介绍，比如：[教大家免费获取一台 Mac 来用，真是机智](https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455988057&idx=1&sn=9f55f456ab17ff29891e863624a26037&chksm=88851314bff29a0276f935d44057c624c2d5a21d83fb34f6168799c5cb110929477257de9b71&token=1018459310&lang=zh_CN#rd)。

简单来说 GitHub Actions 是 GitHub 提供的直接与开源项目深度结合的持续集成服务，大概是 2018 年就推出了，当时那时候一直不温不火，我觉得很多人开始用起来应该是今年。以往 GitHub 上常用的持续集成服务是 Travis CI。

想必大家能看出来，对于一个开源项目 GitHub Actions 是非常重要的，能够帮助更好的开发和维护项目。但是如果你直接使用 GitHub Actions，在配置和运行时都需要一些 GitHub 上的操作，比如提交代码、Pull Request，没有很好的办法在本地进行 Actions 的调式工作，在配置或者修改一个 Actions 都显得有点麻烦。

今天要推荐的项目 act 就是能够帮助大家在本地调式 GitHub Actions 的明星项目。正如 act 项目的理念一样：Think globally, `act` locally。act 有如下两个特点：

1、快速反馈：避免通过 commit/push 来测试 .github/workflows/ 中的文件改动，直接使用 act 可以本地运行，快速验证；

2、本地执行器：有本地执行的加持，act 也能替换 make 来自动化本地的一些操作，可以使用 .github/workflows/ 替换 Makefile。

以下是一个使用的例子：

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/act-quickstart-2.gif)

act 使用 Go 进行开发，安装和使用都非常的简单，而且是全平台支持，这里就不做过多介绍了。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/nektos/act
