---
layout: post
title: 将任意程序转换为 WebSocket 的牛逼工具
tags: Go
---

大家好。

WebSocket 不知道大家了解吗？**WebSocket **是一种在单个TCP 连接上进行全双工通信的协议。简单来说就是，WebSocket 能够允许服务端主动向客户端推送数据。一般的 HTTP 交互，如果要从服务端获取数据（尤其是状态类型的数据），一般需要客户端（比如前端）轮询请求来获取，即使服务端数据没有变更，也是需要定期去轮询的，比较浪费资源，而 WebSocket 比较好的解决了这个问题。

今天要推荐的工具 websocketd，能够将任意的程序转换为 websocketd 的输入输出，对外提供服务，意味着你不需要理解 WebSocket 的原理自己去开发 WebSocket 服务，只需要关注你的业务逻辑即可享受 WebSocket 的优势。

![image-20220103184507075](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220103184507075.png)

以上就是一个简单的示例，其中 count.sh 定时的输出数字，使用 websocketd 封装后，客户端就可以通过 8080 端口按 WebSocket 的形式进行数据的获取。是不是非常的简单呢？

或许你接着就会有这样的疑问，websocketd 可以用来做什么？

![image-20220103184723461](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220103184723461.png)

上面就是使用 websocketd 开发的几个比较优秀的开源项目。比如实时监控 Linux 主机的工具、实时展示 Linux 的文件系统等。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/joewalnes/websocketd
