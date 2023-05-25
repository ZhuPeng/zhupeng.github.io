---
layout: post
title: GitHub 开源项目 apigee/apigeecli 介绍，This is a tool to interact with Apigee APIs. The tool lets you manage (create, del, get, list) environments, proxies, etc.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 apigee/apigeecli，该项目在 GitHub 有超过 0.0k Star，用一句话介绍该项目就是：“This is a tool to interact with Apigee APIs. The tool lets you manage (create, del, get, list) environments, proxies, etc.”。


ApigeeCLI 是 Apigee 公司推出的一个开源项目，它是一个命令行工具，可以帮助用户在本地管理 Apigee Edge 的 API 网关。它支持多种功能，如部署 API 网关配置、创建和管理 API 产品和应用程序等。使用 ApigeeCLI 可以在本地环境中开发和测试 API 网关配置，最终将其部署到 Apigee Edge 上。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=apigee/apigeecli&type=Timeline)

### 如何安装使用

安装这个项目需要先安装 Node.js 和 npm。可以通过以下命令在终端中安装 apigeecli：
```
npm install -g apigeecli
```

安装完成后，可以通过以下命令验证安装是否成功：
```
apigeecli --version
```
在使用之前，还需要配置访问 Apigee Edge 的凭据，可以通过以下命令完成配置：
```
apigeecli configure
```

配置完成后，就可以使用 apigeecli 命令管理 Apigee Edge 了。例如，可以使用以下命令查看环境列表：
```
apigeecli environments list
```

更多用法详见官方文档。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/apigee/apigeecli 

开源项目作者：apigee

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=apigee/apigeecli)



关注我们，一起探索有意思的开源项目。
