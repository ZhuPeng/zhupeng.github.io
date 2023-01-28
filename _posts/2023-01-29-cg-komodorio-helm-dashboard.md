---
layout: post
title: GitHub 开源项目 komodorio/helm-dashboard 介绍，The missing UI for Helm - visualize your releases
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 komodorio/helm-dashboard，该项目在 GitHub 有超过 3.0k Star，用一句话介绍该项目就是：“The missing UI for Helm - visualize your releases”。
![](https://raw.githubusercontent.com/komodorio/helm-dashboard/master/pkg/dashboard/static/logo-header.svg#gh-light-mode-only)
![](https://raw.githubusercontent.com/komodorio/helm-dashboard/master/screenshot.png)

"komodorio/helm-dashboard" 是一个基于 Helm 的 Kubernetes 集群仪表盘。它提供了一个 Web 界面，可以方便地管理和监控集群中的应用程序。该项目支持自动化部署、回滚和扩展等功能，可以帮助用户更轻松地管理和控制他们的应用程序。



### 如何安装使用

该项目的安装需要在 Kubernetes 集群上进行。安装步骤如下：

1. 添加 Helm 仓库：
```sh
helm repo add komodorio https://komodorio.github.io/helm-charts/
```

2. 更新 Helm 仓库：
```sh
helm repo update
```

3. 安装 Helm 包：
```sh
helm install komodorio/helm-dashboard
```

4. 查看安装的状态：
```sh
helm status <RELEASE_NAME>
```

5. 查看安装的 IP 地址：
```sh
kubectl get svc <RELEASE_NAME>-helm-dashboard
```

6. 访问 IP 地址，即可看到管理面板

请注意，这些步骤只是简单的概述，实际操作中可能需要根据自己的环境进行适当的调整。


### 使用示例 DEMO

以下是一个使用 Helm 安装 "komodorio/helm-dashboard" 的示例代码，请按照自己的实际情况进行修改:

1. 添加 Helm 仓库
```sh
helm repo add komodorio https://komodorio.github.io/helm-charts/
```

2. 更新 Helm 仓库
```sh
helm repo update
```

3. 安装 Helm 包，在这里我们将其命名为 "my-dashboard"
```sh
helm install my-dashboard komodorio/helm-dashboard
```

4. 使用下面的命令查看安装的状态:
```sh
helm status my-dashboard
```

5. 使用下面的命令查看安装的 IP 地址:
```sh
kubectl get svc my-dashboard-helm-dashboard
```

6. 打开浏览器,使用上面查询到的 IP 地址访问管理面板

注意: 如果你需要访问管理面板从外部网络,需要将该服务暴露出来.

如果你是在本地开发环境,可以使用下面这个命令将该服务暴露在本地:
```sh
kubectl port-forward svc/my-dashboard-helm-dashboard 8080:80
```

这样就可以在本地访问 http://localhost:8080 查看管理面板了。

请注意，这些代码仅作为示例，实际操作中可能需要根据自己的环境进行适当的调整。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/komodorio/helm-dashboard 

开源项目作者：komodorio

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=komodorio/helm-dashboard)

