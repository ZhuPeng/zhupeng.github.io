---
layout: post
title: 个人开发者必备：快速开发框架 PocketBase 推荐
tags: 开发框架
---

大家好。

如果你是一个个人开发者，需要快速的完成服务的原型开发，你肯定不希望过度的关注数据库、用户、API、管理端的 UI 等怎么管理，快速实现业务价值才是最重要的。所以你一定希望有一个开箱即用，包含所有基础类管理工具的开发框架。

今天要推荐的开源工具 PocketBase，就是一个集合数据库、用户管理、管理 UI 和内建的 API 等工具的后端开发框架。

如果你没有特殊的 API 定制需要的话，你甚至可以直接下载 PocketBase 的二进制文件，直接启动一个后端服务，自带管理界面。

![image-20220924204403398](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220924204403398.png)

在以上管理界面，你可以直接完成数据管理、用户管理等操作，新建数据后，有原生自带的 API，可以轻松完成 CURD，而且有自带的 SDK，完全不需要任何的代码开发。

![image-20220924204523899](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220924204523899.png)

用户和认证都是可以自定义直接使用的。

![image-20220924204556931](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220924204556931.png)

![image-20220924204613338](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220924204613338.png)

除此之外 PocketBase 还提供了服务端的日志查看的功能，方便实时对服务的状态进行了解。

![image-20220924204716184](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220924204716184.png)

如果你希望在 PocketBase 的基础上，进行部分的定制，定制的流程也是比较简单的。以下就是单独开发一个 API 的代码，编译好后替换原来下载的原生二进制即可，原来的用户管理、数据库等都是可以再使用的。

![image-20220924204827163](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220924204827163.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pocketbase/pocketbase

开源项目作者：[pocketbase](https://github.com/pocketbase)