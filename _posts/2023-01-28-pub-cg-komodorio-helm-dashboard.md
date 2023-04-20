---
layout: post
title: 如果你使用 Helm，这款可视化工具不可错过
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 komodorio/helm-dashboard，该项目在 GitHub 有超过 3.0k Star，用一句话介绍该项目就是：“The missing UI for Helm - visualize your releases”，你不可错过的 Helm UI，可视化你的发布流程。
![](https://raw.githubusercontent.com/komodorio/helm-dashboard/master/pkg/dashboard/static/logo-header.svg#gh-light-mode-only)
![](https://raw.githubusercontent.com/komodorio/helm-dashboard/master/images/screenshot.png)

helm-dashboard 是一个基于 Helm 的 Kubernetes 集群仪表盘。它提供了一个 Web 界面，可以方便地管理和监控集群中的应用程序。该项目支持自动化部署、回滚和扩展等功能，可以帮助用户更轻松地管理和控制他们的应用程序。

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


更多项目详情请查看如下链接。

开源项目地址：https://github.com/komodorio/helm-dashboard 

开源项目作者：komodorio

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=komodorio/helm-dashboard)



关注我们，一起探索有意思的开源项目。
