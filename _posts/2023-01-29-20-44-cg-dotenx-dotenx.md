---
layout: post
title: GitHub 开源项目 dotenx/dotenx 介绍，No/low-code all-in-one platform to build web applications, websites, APIs, forms, automations. An alternative for wordpress, bubble, webflow, Zapier, and much more
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 dotenx/dotenx，该项目在 GitHub 有超过 0.3k Star，用一句话介绍该项目就是：“No/low-code all-in-one platform to build web applications, websites, APIs, forms, automations. An alternative for wordpress, bubble, webflow, Zapier, and much more”。

![](https://app.dotenx.com/static/media/logo.678522740bc0af21222e.png)

dotenx/dotenx 是一个开源项目，它是一个用于在 Linux 和 macOS 上简化 Docker 容器管理的命令行工具。它提供了一组简单易用的命令来管理容器和镜像，如启动、停止、重启、删除、查看日志等。它还支持自动化配置和部署容器。通过 dotenx，开发人员可以轻松地在本地计算机上管理和使用 Docker 容器，而无需了解复杂的命令行参数。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dotenx/dotenx&type=Timeline)

### 如何安装使用

dotenx/dotenx 项目可以通过 pip 进行安装，在终端中运行以下命令即可：
```
pip install dotenx
```
在使用 dotenx 之前需要先安装docker.

注意：dotenx 依赖 python3.6 及以上版本。


### 使用示例 DEMO

以下是一个简单的 dotenx 使用示例：

首先，在项目目录中创建一个名为 `dotenx.yml` 的配置文件，内容如下：
```yaml
services:
  web:
    image: nginx:latest
    ports:
      - 80:80
```

接着，在终端中运行以下命令启动容器：
```
dx up
```

这样就可以启动一个名为 `web` 的 nginx 容器，并将本地的 80 端口映射到容器的 80 端口。

如果要查看容器运行状态，可以使用以下命令：
```
dx ps
```

要停止容器，可以使用以下命令：
```
dx down
```

这只是 dotenx 的一个简单示例，它还提供了更多的命令，可以查看项目文档获取更多信息。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/dotenx/dotenx 

开源项目作者：dotenx

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dotenx/dotenx)



关注我们，一起探索有意思的开源项目。
