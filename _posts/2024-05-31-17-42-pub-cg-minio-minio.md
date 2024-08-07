---
layout: post
title: AI 生产可用的高性能对象存储服务
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当今数字化时代，数据成为了企业和个人最宝贵的资产之一。从图片和视频到机器学习模型、应用程序数据，我们每天都在创造和消费大量的数据。然而，随之而来的是对高效、可靠的数据存储方案的巨大需求，特别是在人工智能（AI）和大数据分析等领域。例如，机器学习项目需要存取大量的训练数据，企业需要储存海量的用户数据并保证数据的安全、高效访问。传统存储方案往往难以应对这种规模的数据处理需求，尤其是在性能、扩展性和兼容性方面。因此，开发者和企业都在寻求更加灵活、高效且成本效益高的解决方案。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-3c6138b8345f1e72dbc526d0d76b4cbc.png)

今天要给大家推荐一个 GitHub 开源项目 minio，该项目在 GitHub 有超过 45.1k Star。

![](https://stats.deeptrain.net/repo/minio/minio/?theme=light)

一句话介绍该项目：The Object Store for AI Data Infrastructure

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618223840638.png)

###### 项目介绍

MinIO 是一个高性能的对象存储服务，遵循 GNU Affero General Public License v3.0 发布。它与 Amazon S3 云存储服务兼容，致力于为机器学习、分析和应用数据工作负载构建高性能基础设施。MinIO 可以部署在裸金属硬件上，包括容器化安装，对于 Kubernetes 环境，则推荐使用 MinIO Kubernetes Operator 。MinIO 支持分布式部署、纠删码存储以及多种企业级功能如版本控制、对象锁定和桶复制。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618223941050.png)

###### 如何使用

1、容器安装：

使用以下命令启动最新稳定版本的 MinIO：

```sh
podman run -p 9000:9000 -p 9001:9001 \
  quay.io/minio/minio server /data --console-address ":9001"
```

MinIO 默认使用 `minioadmin:minioadmin` 作为根凭证，用户可以通过浏览器访问 MinIO 控制台来测试部署，进行创建桶、上传对象等操作。

2、macOS 上的安装推荐使用 Homebrew：

```sh
brew install minio/stable/minio
minio server /data
```

3、在 GNU/Linux 上安装（以 64 位 Intel/AMD 架构为例）：

```sh
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
./minio server /data
```

以下是一些 UI 使用界面示例：

![](https://github.com/minio/minio/blob/master/docs/screenshots/pic1.png?raw=true)

![](https://github.com/minio/minio/blob/master/docs/screenshots/pic2.png?raw=true)

###### 项目推介

MinIO 以其高性能、高可靠性和强大的兼容性成为了大数据和 AI 数据基础设施的理想选择。它不仅适合于早期开发和评估，更适用于扩展的开发和生产环境。MinIO 以开源的方式发布，拥有活跃的开发社区和丰富的文档支持，被全球众多企业和开发者广泛使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240618224226142.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=minio/minio&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/minio/minio 

开源项目作者：minio

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=minio/minio)

关注我们，一起探索有意思的开源项目。

