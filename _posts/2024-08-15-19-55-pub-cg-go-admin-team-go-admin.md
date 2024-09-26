---
layout: post
title: 3分钟构建前后端分离权限管理系统
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

前后端分离已成为 Web 开发的重要范式。然而，搭建一个具备完整权限管理系统的前后端分离应用，并非易事。开发者需要面临诸如用户鉴权、数据权限控制、界面布局、后端服务搭建等一系列复杂问题。尤其是在多租户、RBAC（基于角色的访问控制）资源控制等更为高级的功能需求面前，开发的难度和耗时会成倍增加。这些核心痛点常常让开发者和团队感到苦恼。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-f794f296ce250656172e4bebac99824c.png)

今天要给大家推荐一个 GitHub 开源项目 go-admin，该项目在 GitHub 有超过 11.2k Star。

![](https://stats.deeptrain.net/repo/go-admin-team/go-admin/?theme=light)

一句话介绍该项目：基于 Gin + Vue + Element UI &  Arco Design & Ant Design 的前后端分离权限管理系统脚手架，3分钟构建自己的中后台项目

![](https://doc-image.zhangwj.com/img/go-admin.svg)


###### 项目介绍

go-admin 是一个基于 Gin + Vue + Element UI 或 Arco Design 搭建的前后端分离权限管理系统脚手架。它解决了上述提到的一系列痛点，提供了多租户支持、基础用户管理功能、jwt 鉴权、代码生成器、RBAC 资源控制、表单构建、定时任务等一系列高效的功能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909220656471.png)

go-admin 的目标是帮助开发者和企业能在 3 分钟内构建属于自己的中后台项目，极大地缩短开发时间，提高开发效率。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240909220632603.png)

###### 如何使用

安装和使用 `go-admin` 项目需要有 Go、Node.js 和 Git 环境。以下是具体的安装与启动教程。

1、创建开发目录并获取代码：

```bash
# Create develop dir
mkdir goadmin
cd goadmin

git clone https://github.com/go-admin-team/go-admin.git

# ui code
git clone https://github.com/go-admin-team/go-admin-ui.git
```

2、启动后端服务器：

```bash
cd go-admin

# update deps
go mod tidy

# compile
go build

# modify go-admin/config/settings.yml, set database config
vi ./config/settings.yml
```

3、启动前端项目

```bash
# Installation dependencies
npm install   # or cnpm install

# Start service
npm run dev
```

###### 项目推介

`go-admin` 由于其强大的功能及易用性，已经吸引了大量开发者和企业的关注。目前项目保持活跃状态，持续接受社区的贡献和改进。它不仅仅是一个后台管理系统的脚手架，更是一个整套前后端解决方案的实现，可以显著降低企业和个人开发成本。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-admin-team/go-admin&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-admin-team/go-admin 

开源项目作者：go-admin-team

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-admin-team/go-admin)

关注我们，一起探索有意思的开源项目。

