---
layout: post
title: 开箱即用的 MySQL 审核平台
tags: Go
---

大家好。

程序员日常工作接触最多的可能就是 SQL 了，而 SQL 语句的编写是很考验水平的。如果让有问题的 SQL 变更发布到线上，可能会直接造成线上服务的不可用，所以 SQL 经过团队成员的审核校对是很有必要的。

今天要推荐的工具 Yearning，是一个开箱即用的 MySQL Web 审核平台，提供查询审计，SQL审核，SQL回滚，自定义工作流等多种功能。

![image-20220116210054699](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220116210054699.png)

Yearning 拥有以下功能:

1、自动化SQL语句审核,可对SQL进行自动检测并执行

2、 DDL/DML语句执行后自动生成回滚语句

3、 审核/查询 审计功能

4、 支持LDAP登录/钉钉及邮件消息推送

5、 支持自定义审核工作流

6、 支持细粒度权限分配

更全的功能如下图：

![image-20220116210407955](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220116210407955.png)

Yearning 使用 Go 语言开发，同时 Yearning 不依赖于任何第三方 SQL 审核工具作为审核引擎，内部已自己实现审核/回滚相关逻辑，仅依赖 Mysql 数据库存储相应的流程和使用情况。所以 Yearning 安装也很简单，只需要下载官方的二进制包即可启动，开箱即用。以下是 Yearning 的几个常用操作界面：

1、Dashboard

![image-20220116210839868](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220116210839868.png)

2、审核

![image-20220116210907120](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220116210907120.png)

3、SQL 语法及规则检测

![image-20220116210924123](https://7465-test-3c9b5e-1-1301419220.tcb.qcloud.la/images/compress_image-20220116210924123.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/cookieY/Yearning
