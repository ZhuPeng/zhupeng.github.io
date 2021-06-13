---
layout: post
title: 开源轻量化静态代码扫描工具
tags: Python
---

大家好。

静态代码扫描不知道大家了解么？根据我的工作经验，静态代码扫描是众多提高项目质量的工具或者方法中，投入回报比例最高的。如果你的团队还没有开始使用，我强烈建议你将静态代码扫描集成到你们的开发流程中。

所以今天要推荐的开源轻量化静态代码扫描工具绝对不能错过。

![image-20210613214603284](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210613214603284.png)

Semgrep，是一个快速、开源的静态代码扫描工具，能够自动检测代码中的 Bug，同时能够在编辑器、Commit、Ci 的过程中规范项目中的代码。Semgrep 在本地分析你的项目代码，不会上传任何的代码。

Semgrep 定义的检测规则也比较的简单，没有复杂的 DSL，比如如下就是一个检测规则：

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_playground-example.png)

Semgrep 系统包含 CI、Playgroud、Registry、App 几个部分，支持分析各大主流编程语言，比如 Go · Java · JavaScript · JSX · JSON · Python · Ruby · TypeScript · TSX 等。

![](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_image-20210613215039337.png)

Semgrep 目前在 GitHub 标星 4.2K，同时社区也非常的活跃。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/returntocorp/semgrep
