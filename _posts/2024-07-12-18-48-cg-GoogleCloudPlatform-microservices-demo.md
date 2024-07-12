---
layout: post
title: GitHub 开源项目 GoogleCloudPlatform/microservices-demo 介绍，Sample cloud-first application with 10 microservices showcasing Kubernetes, Istio, and gRPC.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 GoogleCloudPlatform/microservices-demo，该项目在 GitHub 有超过 16.3k Star。

![](https://stats.deeptrain.net/repo/GoogleCloudPlatform/microservices-demo/?theme=light)

一句话介绍该项目：Sample cloud-first application with 10 microservices showcasing Kubernetes, Istio, and gRPC.




![Screenshot of store homepage](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/master//docs/img/online-boutique-frontend-1.png)

![Screenshot of checkout screen](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/master//docs/img/online-boutique-frontend-2.png)

![](https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/master//src/frontend/static/icons/Hipster_HeroLogoMaroon.svg)


###### 项目介绍

### 背景介绍

在数字化时代，微服务架构因其高度的模块化和灵活性成为现代企业应用开发的首选。通过将一个大型应用拆分为小型、独立服务，企业能够更灵活地开发和部署应用，使得迭代更快、扩展更简单，同时也便于实现敏捷开发和持续集成。然而，微服务架构的实施面临着众多挑战，包括服务之间的通信、数据一致性、服务发现、负载均衡以及如何全面地监控和跟踪微服务等问题。这些挑战需求一个全面的方案和示例来指导开发人员如何在实际环境中解决。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-34b9936b7e48f117142fe2ddfb8b263b.png)

项目介绍

**Online Boutique** 是一个展示了使用 Google Cloud 产品现代化企业应用的云原生微服务演示应用程序。这款基于 Web 的电子商务应用允许用户浏览商品、添加到购物车并进行购买。它由 11 个用不同语言编写的微服务组成，这些服务通过 gRPC 进行通信。该项目涵盖了使用 [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine)、[Anthos Service Mesh (ASM)](https://cloud.google.com/service-mesh)、[gRPC](https://grpc.io/)、[Cloud Operations](https://cloud.google.com/products/operations) 等 Google Cloud 产品的使用。

凭借其全面的服务和技术栈示例，包括前端、购物车服务、产品目录服务、货币服务等，**Online Boutique** 展示了一个如何构建和部署全栈微服务架构的实用案例。此外，通过模拟真实的用户购物流程，**Online Boutique** 同时也是了解微服务性能、可靠性和可伸缩性挑战的绝佳资源。

### 如何使用

要在 Google Kubernetes Engine (GKE) 上部署 **Online Boutique**，请遵循以下快速入门指南：

1. 准备必需的要求，包括 [Google Cloud 项目](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project)、`gcloud`、`git` 和 `kubectl` 工具。

2. 克隆仓库并进入项目目录：

   ```sh
   git clone --depth 1 --branch v0 https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/
   ```
   
3. 设置 Google Cloud 项目和区域，并启用 Google Kubernetes Engine API：

   ```sh
   export PROJECT_ID=<您的项目ID>
   export REGION=us-central1
   gcloud services enable container.googleapis.com --project=${PROJECT_ID}
   ```

4. 创建 GKE 集群并获取其凭据：

   ```sh
   gcloud container clusters create-auto online-boutique --project=${PROJECT_ID} --region=${REGION}
   ```

5. 将 **Online Boutique** 部署到集群上：

   ```sh
   kubectl apply -f ./release/kubernetes-manifests.yaml
   ```

6. 等待 Pods 准备就绪：

   ```sh
   kubectl get pods
   ```

### 项目推介

**Online Boutique** 是一个由 Google Cloud 平台推出的项目，得到了业内广泛的认可和使用。该项目不仅展示了微服务架构的最佳实践，同时也是学习和实验 Google Cloud 产品的绝佳资源。无论是刚接触云原生应用的新手，还是希望深入理解微服务架构的专家，都能从这个项目中获得丰富的知识和实践经验。

此外，由于 **Online Boutique** 涵盖多种语言和技

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=GoogleCloudPlatform/microservices-demo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/GoogleCloudPlatform/microservices-demo 

开源项目作者：GoogleCloudPlatform

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=GoogleCloudPlatform/microservices-demo)

关注我们，一起探索有意思的开源项目。

