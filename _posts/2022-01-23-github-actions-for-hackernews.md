---
layout: post
title: 使用 GitHub Actions 自动生成 HackerNews 每日 TOP10 话题
tags: GitHub
---

大家好。

今天先给大家介绍一个不需要使用自己的服务器，而是使用 GitHub Actions 来自动生成 HackerNews 每日 TOP10 话题的开源项目，hackernews-daily 借助 GitHub Actions 提供的定时运行的能力，每天通过 API 获取 HackerNews 热门的十大话题，并自动更新到项目的 Issue 中，用户可以通过 GitHub 提供的 Watch 功能来订阅更新（当然也可以通过其他的 RSS 工具）。

![image-20220123123107200](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220123123107200.png)

![image-20220123123204045](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220123123204045.png)

hackernews-daily 的实现也是非常的简单，借助 Actions 极强的扩展能力，以下就是对应的配置：

![image-20220123123329109](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220123123329109.png)

以上核心的运行逻辑对应的是 run: node index.js，会通过 API 获取十大话题，并创建新的 Issue 更新到项目中。

过往其实我们介绍过比较多 GitHub Actions 的妙用了，如果你还是不太懂，这次我们再简单介绍一下 GitHub Actions。

Acitons 是 GitHub 提供的自动化流程的功能，自然是跟 GitHub 强相关的，核心是通过触发事件和具体的执行任务进行关联。

![image-20220123124106571](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220123124106571.png)

对应上图中的 Event 和 Job，而 Runner 是实际运行 Job 的环境，Event 可以是 Issue 创建、PR 创建、定时等，而 Job 可以设置单个和多个，并行或者串行执行。每一个 Job 内部有相应的运行 Step，按顺序执行。

以上的 Event 和 Job 配置会以 yaml 文件进行存储，放在项目的 .github/workflows/ 位置，配置如下所示：

![image-20220123124520417](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220123124520417.png)

GitHub Actions 一般常规的用法是帮助运行开源项目的测试自动化流程，但是由于其扩展性比较强，很多的开源爱好者发现了非常多有趣的玩法，比如我们今天分享的 hackernews-daily 就是其中一个。

更多项目详情请查看如下链接，如果你也有新奇的 GitHub Actions 玩法欢迎和我们分享。

开源项目地址：https://github.com/headllines/hackernews-daily
