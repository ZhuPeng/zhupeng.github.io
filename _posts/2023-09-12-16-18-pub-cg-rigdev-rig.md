---
layout: post
title: Rig.dev - 一个专为 Kubernetes 设计的开发者中心化应用平台
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在现代的开发环境中，Kubernetes 已经成为了云原生应用的首选平台。然而，对于开发者来说，Kubernetes 的复杂性却是一大挑战。如何简化应用的部署、管理、调试和扩展，如何提供用户管理、认证、存储和数据库集成等基础 API，这些都是开发者在使用 Kubernetes 时常常会遇到的问题。

今天要给大家推荐一个 GitHub 开源项目 rigdev/rig，该项目在 GitHub 有超过 583 Star，用一句话介绍该项目就是：“Rig.dev is a developer-centric application platform for Kubernetes”。


![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006220849149.png)

###### 项目介绍

Rig.dev 是一个专为 Kubernetes 设计的开发者中心化应用平台。它通过提供开发者友好的部署引擎，简化了应用的上线、管理、调试和扩展过程。同时，它还提供了用户管理、认证、存储和数据库集成等基础 API。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231006221349179.png)

Rig.dev 的主要特点包括：

1、容器镜像的抽象，便于部署；

2、完全支持 Docker 的本地开发；

3、提供认证和用户管理功能，提供数据库和存储集成；

4、基于 gRPC 的 API，提供 Golang 和 Typescript/Javascript 的 SDK。

###### 如何使用

Rig.dev 提供了详细的入门指南，可以帮助你在本地机器或生产环境的 Kubernetes 集群上进行设置。如果你在使用过程中遇到任何问题，都可以在 Rig.dev 的 Discord 服务器上寻求帮助。

可以使用 Helm 或者本地的 Docker compose 进行安装启动。

Helm 参考如下：

```bash
helm repo add rig https://charts.rig.dev
helm upgrade --install rig rig/rig \
  --version v1.1.3 \
  --namespace rig-system \
  --create-namespace \
  --set mongodb.enabled=true
```

Docker Compose 参考如下：

```yaml
services:
  rig:
    image: ghcr.io/rigdev/rig:1.1.3
    environment:
      RIG_AUTH_JWT_SECRET: mysecret
      RIG_CLIENT_MONGO_HOST: mongo:27017
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "4747:4747"

  mongo:
    image: "mongo:latest"
    volumes:
    - mongo-data:/data'

volumes:
  mongo-data:

networks:
  default:
    name: rig
```

保存以上配置到文件 docker-compose.yaml 中，然后使用命令 docker compose up -d 即可启动。

###### 项目推介

Rig.dev 已经在 Apache 2.0 许可下开源，这意味着你可以自由地使用和修改它。如果你在使用过程中发现任何问题，或者有任何改进的建议，都可以通过提交 bug 报告或者创建 Pull Request 来为 Rig.dev 做出贡献。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=rigdev/rig&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/rigdev/rig 

开源项目作者：rigdev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=rigdev/rig)

关注我们，一起探索有意思的开源项目。

