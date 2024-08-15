---
layout: post
title: GitHub 开源项目 go-admin-team/go-admin 介绍，基于Gin + Vue + Element UI &  Arco Design & Ant Design 的前后端分离权限管理系统脚手架（包含了：多租户的支持，基础用户管理功能，jwt鉴权，代码生成器，RBAC资源控制，表单构建，定时任务等）3分钟构建自己的中后台项目；项目文档》：https://www.go-admin.pro   V2 Demo： https://vue2.go-admin.dev V3 Demo： https://vue3.go-admin.dev Antd 订阅版：https://antd.go-admin.pro
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 go-admin-team/go-admin，该项目在 GitHub 有超过 11.2k Star。

![](https://stats.deeptrain.net/repo/go-admin-team/go-admin/?theme=light)

一句话介绍该项目：基于Gin + Vue + Element UI &  Arco Design & Ant Design 的前后端分离权限管理系统脚手架（包含了：多租户的支持，基础用户管理功能，jwt鉴权，代码生成器，RBAC资源控制，表单构建，定时任务等）3分钟构建自己的中后台项目；项目文档》：https://www.go-admin.pro   V2 Demo： https://vue2.go-admin.dev V3 Demo： https://vue3.go-admin.dev Antd 订阅版：https://antd.go-admin.pro




![](https://doc-image.zhangwj.com/img/go-admin.svg)

![](https://raw.githubusercontent.com/wenjianzhang/image/master/img/wx.png)

![](https://doc-image.zhangwj.com/img/qrcode_for_gh_b798dc7db30c_258.jpg)

![](https://raw.githubusercontent.com/wenjianzhang/image/master/img/qq2.png)

![](https://pub.idqqimg.com/wpa/images/group.png)

![](https://raw.githubusercontent.com/panjf2000/illustrations/master/jetbrains/jetbrains-variant-4.png)

![](https://raw.githubusercontent.com/wenjianzhang/image/master/img/pay.png)


###### 项目介绍

背景介绍：
在当今快速发展的互联网时代，前后端分离已成为 web 开发的重要范式。然而，搭建一个具备完整权限管理系统的前后端分离应用，并非易事。开发者需要面临诸如用户鉴权、数据权限控制、界面布局、后端服务搭建等一系列复杂问题。尤其是在多租户、RBAC（基于角色的访问控制）资源控制等更为高级的功能需求面前，开发的难度和耗时会成倍增加。这些核心痛点常常让开发者和团队感到苦恼。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f794f296ce250656172e4bebac99824c.png)

项目介绍：
`go-admin` 是一个基于 Gin + Vue + Element UI 或 Arco Design 搭建的前后端分离权限管理系统脚手架。它解决了上述提到的一系列痛点，提供了多租户支持、基础用户管理功能、jwt 鉴权、代码生成器、RBAC 资源控制、表单构建、定时任务等一系列高效的功能。`go-admin` 的目标是帮助开发者和企业能在 3 分钟内构建属于自己的中后台项目，极大地缩短开发时间，提高开发效率。

如何使用：
安装和使用 `go-admin` 项目需要有 Go、Node.js 和 Git 环境。以下是具体的安装与启动教程。

1. 首先，创建开发目录并获取代码：

    ```bash
    # 创建开发目录
    mkdir goadmin
    cd goadmin

    # 获取后端代码
    git clone https://github.com/go-admin-team/go-admin.git

    # 获取前端代码
    git clone https://github.com/go-admin-team/go-admin-ui.git
    ```

2. 启动后端服务器：

    ```bash
    # 进入 go-admin 后端项目
    cd go-admin

    # 更新依赖
    go mod tidy

    # 编译项目
    go build

    # 修改配置文件 go-admin/config/settings.yml, 设置数据库等信息
    vi ./config/settings.yml
    ```

3. 启动前端项目，参考 `go-admin-ui` 的 README 文档进行依赖安装和项目启动。

项目推介：
`go-admin` 由于其强大的功能及易用性，已经吸引了大量开发者和企业的关注。目前项目保持活跃状态，持续接受社区的贡献和改进。它不仅仅是一个后台管理系统的脚手架，更是一个整套前后端解决方案的实现，可以显著降低企业和个人开发成本。

无论是刚入门的初学者，还是在寻找快速搭建项目框架的开发者，`go-admin` 都是一个不错的选择。项目提供了丰富的在线演示和详细的文档教程，包括视频教学和步骤指引，帮助用户快速掌握和应用。

此外，`go-admin` 因其优良的设计和强大的功能，在开源社区也收获了不少好评。如果你在寻找一个高效、灵活、功能全面的后台管理系统脚手架，`go-admin` 绝对值得考虑。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-admin-team/go-admin&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-admin-team/go-admin 

开源项目作者：go-admin-team

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-admin-team/go-admin)

关注我们，一起探索有意思的开源项目。

