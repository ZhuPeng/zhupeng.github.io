---
layout: post
title: GitHub 精选开源项目周刊第1期
tags: 其他
---

今天又是一个特别的推送，之前我们尝试推了一次: 。
我们暂且把名字定为 GitHub 精选开源项目推荐周刊，争取每周发布一次，欢迎自荐或者推荐自己发现的好玩的东西。
按程序员的思维，尝试的那次成为第 0 期，所以今天的是我们推送的第 1 期。坐稳，要发车了。

## 为 Restful API 设计的权限认证库
**项目介绍：**
目前 Java 主流的权限框架有shiro，spring security。但是shiro 对于 Restful API 原生支持不是太友好,需要改写一些代码；Spring Security 很强大,与 Spring 深度集成, 离开 Spring,比如 Google 的精简 guice,之前用过的 osgi 框架 karaf 就用不了了。
Sureness 是作者在使用 Java 权限框架shiro 之后,吸取其良好的设计加上一些自己想法实现的全新认证鉴权项目。

**功能描述:**
面对 Restful API 的认证鉴权，基于 RBAC 主要关注于对Restful API 的保护
原生支持 Restful API, Websocket protection
原生支持动态权限(权限配置的动态加载)
原生支持 jwt, Basic Auth ... 可扩展自定义支持的认证方式
基于改进的字典匹配树大大提高性能

sureness的低配置，易扩展，不耦合其他框架，能使开发者对自己的项目多场景快速安全的进行保护。

**项目地址：**https://github.com/tomsun28/sureness
**项目作者：**[tomsun28](https://github.com/tomsun28)

## 后台管理基础框架
**项目介绍：**
一套基于SpringBoot、Shiro、Mybatis 的RBAC后台管理基础框架。
项目特点：安全、稳定、持续更新的基础平台与解决方案，避免重复造轮子，专注于业务逻辑，后台技术基于SpringBoot，MyBatis，Shiro等主流框架开发，前端页面采用 LayUi 开发。本系统技术栈选型专门面向后台开发人员快速上手而选，开箱即用。

**功能描述：**
资源管理：系统中的菜单，按钮，功能权限，查询权限等元素统称为系统资源。
角色管理：精细化资源授权和数据授权，实现菜单，按钮，自定义数据权限的控制。
用户管理：登录系统的帐号亦称“系统用户”，用户可以关联一个或多个角色。
机构管理：机构也可以称为“部门”，是将系统用户进行组织架构划分的模块。
字典管理：系统字典管理，常量管理。
日志管理：系统业务操作日志，API调用日志，用户登录日志等。
监控管理：系统链路监控，主机监控，SQL连接池监控等。
代码生成：自定义模块信息一键生成全流程代码，拿来即用，减少80%重复工作量。
演示地址：http://coral.gemframework.com:8088/admin/login

![image-20200423194352042](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/mac_github_images/compress_image-20200423194352042.png)


**项目地址：**https://gitee.com/gemteam/coral


## 简单漂亮的博客系统
**项目介绍：**
该博客是基于 SSM(Spring+SpringMVC+Mybatis)实现的一个个人博客系统，适合初学 SSM 和个人博客制作的同学学习。 主要涉及技术包括的包括 Maven、Spring、SpringMVC、MyBatis、Redis、JSP等。 前端采用 Layui 框架和扒了一个网站的前台样式。

**功能描述：**
详细介绍：https://liuyanzhao.com/6347.html

![](https://raw.githubusercontent.com/saysky/ForestBlog/master/uploads/home.png)

项目地址：https://github.com/saysky/ForestBlog
项目作者：[saysky](https://github.com/saysky/ForestBlog)

以上就是本次推荐的全部项目。GitHub精选 公众号致力于为大家分享和宣传优质的开源项目，让更多的人了解和知道，乃至去使用大家的开源项目，一方面可以帮助大家提高影响力，另外一方面还有助于大家收获更多粉丝的支持。如果你有开项目需要分享，欢迎扫码进群或者直接在 [共享文档](https://www.yuque.com/g/loonggg/febxd7/wvs0z6/collaborator/join?token=bVhhgBw5Rw0xM0Qj) 分享。

![image-20200423210812474](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/mac_github_images/compress_image-20200423210812474.png)



