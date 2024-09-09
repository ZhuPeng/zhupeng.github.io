---
layout: post
title: 提供多种身份验证的反向代理工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今的数字化时代，保护企业和个人数据的重要性日益增加。随着越来越多的服务和应用程序转移到云端，确保安全访问变得极其关键。面对多样的身份提供者和复杂的网络架构，开发人员和企业面临着如何简化身份验证流程以确保数据安全的挑战。这其中的痛点包括：如何集成多种身份验证服务、管理不同平台的访问控制、同时又不牺牲用户体验。

今天要给大家推荐一个 GitHub 开源项目 oauth2-proxy，该项目在 GitHub 有超过 9.2k Star。

![](https://stats.deeptrain.net/repo/oauth2-proxy/oauth2-proxy/?theme=light)

一句话介绍该项目：A reverse proxy that provides authentication with Google, Azure, OpenID Connect and many more identity providers.

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240829223842540.png)


###### 项目介绍

oauth2-proxy 是一个反向代理和静态文件服务器，使用不同的提供商（比如 Google、Keycloak、GitHub 等）来验证账户，通过电子邮件、域名或群组实现认证。起源于 `bitly/OAuth2_Proxy`，`oauth2-proxy` 自 2018 年分叉后，项目不断发展完善，提供了更为广泛的功能和更好的维护。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240829223819886.png)

该项目的主要功能包括：

1、多种身份验证提供商支持：通过不同的提供商，如 Google、Azure、OpenID Connect，实现灵活的身份验证方案。

2、简易安装部署：支持多种部署方式，包括预构建的二进制文件、Docker 镜像、Go 安装，甚至提供官方的 Kubernetes Helm 包。

3、高度可配置：可以通过配置文件、命令行选项或环境变量配置 `oauth2-proxy`，适应不同的部署环境。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240829224103659.png)

###### 如何使用

1、安装: 根据你的需求选择一个部署方式，比如使用预构建的 Docker 镜像：

```bash
docker pull quay.io/oauth2-proxy/oauth2-proxy
```

2、注册并配置 OAuth 应用：根据你选择的身份提供商，注册 OAuth 应用并获取必要的配置信息。

3、配置 `oauth2-proxy`：使用配置文件或命令行选项来配置代理，示例命令如下：

```bash
oauth2-proxy --provider=google \
  --email-domain=*your-domain.com \
  --cookie-secret=<YOUR_SECRET> \
  --client-id=<YOUR_CLIENT_ID> \
  --client-secret=<YOUR_CLIENT_SECRET>
```

4、部署：将 `oauth2-proxy` 部署到你的环境中，并确保它作为你的应用前端的反向代理。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240815212632343.png)

###### 项目推介

oauth2-proxy 自从分叉以来已成功发布多个版本，目前最新的版本为 `v7.6.0`。该项目不但拥有活跃的开发社区，还对安全性给予了高度重视，推荐升级到最新版本以避免安全漏洞。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=oauth2-proxy/oauth2-proxy&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/oauth2-proxy/oauth2-proxy 

开源项目作者：oauth2-proxy

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=oauth2-proxy/oauth2-proxy)

关注我们，一起探索有意思的开源项目。

