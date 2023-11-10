---
layout: post
title: 有了这个工具前端项目再也不用漫长的等待 npm install 
tags: Node.js 前端
---

大家好。

我做为一个后端程序员，有时候会需要接触前端的项目，经常问题出现在前置的一些配置上，比如安装依赖包，npm install 需要等比较长时间，有时候可能还会失败。所以如果给我的前端项目都能一键启动起来，直接就能测试跟后端的一些联调效果，效率一定会高很多。

今天要推荐的开源项目 pkg，就是一个能够将前端的 Node.js 项目打包成一个可执行的文件，可以不依赖 Node.js 直接启动，简直太棒了。

![image-20220417202659091](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220417202659091.png)

项目 pkg 有如下使用场景：

![image-20220417202753161](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220417202753161.png)

总结来看还是非常多的使用场景的，毕竟很多情况下源码的分发存在商业机密的泄露，依赖包的安装除了慢的因素外，还可能有依赖的复杂问题，出现失败的情况，增加了不必要的麻烦。所以如果你也有碰到上面的这些场景，不妨使用 pkg 将你的项目打包成一个可以直接执行的文件，你的用户也能更好的使用。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/vercel/pkg
