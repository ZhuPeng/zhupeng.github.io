---
layout: post
title: pgrok - 针对小团队的多租户反向代理
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在进行软件开发、远程协作和产品测试阶段时，开发团队或许会面临一个问题，如何将本地的开发环境稳定且安全的提供给公网的其他用户进行访问？这其中涉及到了自己搭建反向代理的问题，以及项目如何对接单点登录服务提供商等一系列问题。

![](https://ecloud.eos-guangzhou-1.cmecloud.cn/op-admin-content/dbc290b9b6f049bd96fc167fd3c4b6b3.jpg)

今天要给大家推荐一个 GitHub 开源项目 pgrok/pgrok，该项目在 GitHub 有超过 2.9k Star，用一句话介绍该项目就是：“Poor man's ngrok - a multi-tenant HTTP/TCP reverse tunnel solution through SSH remote port forwarding”。

![](https://user-images.githubusercontent.com/2946214/227126410-3e9dae19-d0c0-4a96-9040-1322e389c8db.png)

###### 项目介绍

pgrok 是一个针对小团队的多租户 HTTP/TCP 反向隧道解决方案，它通过 SSH 的远程端口转发技术实现。pgrok 孵化于这样的困境，针对以上的问题，它不仅可以稳定提供子域名给每一个使用者，更加强大的是它可以通过 OIDC 协议接入你的 SSO。可以认为他是 ngrok 的企业版的简单替代品。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240426230639317.png)

pgrok 所需环境包括公网访问的服务器、具有域名、SSO 提供者和 PostgreSQL 数据库服务器。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240426230657536.png)

以下是 pgrok 的项目流量的交互图：

![](https://user-images.githubusercontent.com/2946214/229048941-cc12139d-f250-49fa-806d-19c27996ee09.png)


###### 如何使用

首先，你需要在你的域名上添加相应的 DNS 记录，然后在服务器上设置，并根据你的实际情况修改网络安全策略来允许从任何地方的 2222 端口请求。然后，在 SSO 上创建一个新的 OIDC 客户端，并将 Redirect URI 设置为 `http://example.com/-/oidc/callback`。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119225452156.png)

在客户端的设置上，首先访问 `http://example.com`，使用你的 SSO 进行认证以获取 token 和 URL ( 例如： `http://unknwon.example.com` )。然后可以通过 homebrew 进行安装：
```
brew install pgrok
```
或者可以从 Releases 页面下载最新的压缩包。最后，使用以下命令初始化一个 `pgrok.yml` 文件：
```
pgrok init --remote-addr example.com:2222 --forward-addr http://localhost:3000 --token {YOUR_TOKEN}
```

然后可以使用 pgrok http 8080 设置代理地址。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119225543080.png)

整体配置会有些复杂，更多的说明请查看官方的介绍。

###### 项目推介

尽管 `pgrok` 项目在开源社区中还不够成熟，但由于它解决了诸多实际痛点，已经在一群倾向使用简单、稳定的反向代理解决方案的小团队中积累了一定的影响力。简单的使用方式使得非开发人员也能快速上手，而基于 SSH 的反向隧道技术以及 SSO 的支持确保了安全性和稳定性，可谓是小团队进行开发测试等操作的优秀选择。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231119225800878.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pgrok/pgrok&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pgrok/pgrok 

开源项目作者：pgrok

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pgrok/pgrok)

关注我们，一起探索有意思的开源项目。

