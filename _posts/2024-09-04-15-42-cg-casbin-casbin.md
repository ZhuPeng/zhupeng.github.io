---
layout: post
title: GitHub 开源项目 casbin/casbin 介绍，An authorization library that supports access control models like ACL, RBAC, ABAC in Golang: https://discord.gg/S5UjpzGZjN
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 casbin/casbin，该项目在 GitHub 有超过 17.4k Star。

![](https://stats.deeptrain.net/repo/casbin/casbin/?theme=light)

一句话介绍该项目：An authorization library that supports access control models like ACL, RBAC, ABAC in Golang: https://discord.gg/S5UjpzGZjN




![casbin Logo](https://raw.githubusercontent.com/casbin/casbin/master/casbin-logo.png)

![golang](https://casbin.org/img/langs/golang.png)

![java](https://casbin.org/img/langs/java.png)

![nodejs](https://casbin.org/img/langs/nodejs.png)

![php](https://casbin.org/img/langs/php.png)

![python](https://casbin.org/img/langs/python.png)

![dotnet](https://casbin.org/img/langs/dotnet.png)

![c++](https://casbin.org/img/langs/cpp.png)

![rust](https://casbin.org/img/langs/rust.png)

![model editor](https://hsluoyz.github.io/casbin/ui_model_editor.png)


###### 项目介绍

背景介绍：
随着信息技术的快速发展，软件应用变得日益庞大和复杂，特别是在权限和访问控制方面。传统的硬编码权限管理方法不仅难以维护，而且无法灵活应对快速变化的业务需求，这就使得开发者和组织面临着巨大的挑战。如何高效、灵活地管理用户权限，实现细粒度的访问控制成为了一个迫切需要解决的问题。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-d533b048d8da96b2f8aeacc039fa58bf.png)

项目介绍：
Casbin 是一个强大且高效的开源访问控制库，适用于 Golang 项目。它支持基于多种访问控制模型如 ACL（访问控制列表）、RBAC（基于角色的访问控制）、ABAC（基于属性的访问控制）等执行授权。Casbin 的设计允许用户通过修改配置文件来切换或升级授权机制，从而无需改变代码就可适应不同的访问控制需求。它的特点包括但不限于支持多种内置模型、简易的策略规则定义、高性能的匹配和决策等。此外，Casbin 还支持 RESTful 风格的路径和 HTTP 方法控制，提供了丰富的文档和教程来支持开发者快速入门和使用。

如何使用：
要在 Golang 项目中使用 Casbin，首先需要安装 Casbin：
```
go get github.com/casbin/casbin/v2
```
然后，您可以按照 Casbin 提供的文档和示例来定义访问控制模型（.conf 文件）和策略（.csv 文件）。例如，使用 RBAC 模型：
```go
package main

import (
    "github.com/casbin/casbin/v2"
    _ "github.com/casbin/casbin/v2/persist/file-adapter"
)

func main() {
    e, _ := casbin.NewEnforcer("path/to/model.conf", "path/to/policy.csv")

    // 检查权限
    if e.Enforce("alice", "data1", "read") {
        // 允许访问
    } else {
        // 拒绝访问
    }
}
```
项目推介：
Casbin 在 GitHub 上的活跃度很高，拥有一个稳定并日渐增长的社区。不仅如此，Casbin 已被多家知名公司采用，其生产就绪的应用范围覆盖了多种编程语言，包括 Java、Node.js、PHP、Python、.NET、CPP 以及 Rust，展现了其强大的跨语言支持能力。此外，Casbin 也得到了业界诸多知名人士的推荐。无论是从功能丰富性、易用性、还是从社区活跃度和企业采纳率来看，Casbin 都是一个值得投入和使用的访问控制解决方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=casbin/casbin&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/casbin/casbin 

开源项目作者：casbin

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=casbin/casbin)

关注我们，一起探索有意思的开源项目。

