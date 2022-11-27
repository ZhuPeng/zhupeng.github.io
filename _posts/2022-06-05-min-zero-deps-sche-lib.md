---
layout: post
title: 最小化无外部依赖的调度开源库，非常值得学习
tags: Go&任务调度
---

大家好。

线程调度、任务调度是平常我们写程序经常接触到的概念，但是我们平常使用的一些大型开源项目都自带类似的功能，我们用起来都得心应手，但是，如果要你去自己实现一个任务调度模块，你有信心能够实现出来吗？

今天要推荐的开源项目 go-quartz，是受著名开源项目 quartz 启发，用 Go 语言实现了一个最小化、无外部依赖的任务调度模块。go-quartz 最大的好处就是简单，非常适合用来了解和学习任务调度相关的知识，当然如果你对如何更好的组织一个 Go 项目，go-quartz 也是非常值得学习的。

go-quartz 中核心就三个概念模块，分别是 Scheduler（调度器）、Trigger（触发器）和 Job（任务）。该项目通过接口的形式定义了以上三个模块的行为，其实只要你知道了上述接口，用任何语言也可以实现一个任务调度的模块。

对应的定义如下：

![image-20220605205922233](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220605205922233.png)

![image-20220605205930925](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220605205930925.png)

![image-20220605205937802](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220605205937802.png)

项目中对上述的接口有默认的实现，通过这些实现，可以很容易的去定义一个自己的任务执行系统。比如以下就是一个示例，实现了定时执行脚本命令和访问网站的任务，代码非常的简单。

![image-20220605210027303](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220605210027303.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/reugn/go-quartz

开源项目作者：reugn