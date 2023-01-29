---
layout: post
title: GitHub 开源项目 helmfile/helmfile 介绍，Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases. Generate all-in-one manifests for use with ArgoCD.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 helmfile/helmfile，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“Declaratively deploy your Kubernetes manifests, Kustomize configs, and Charts as Helm releases. Generate all-in-one manifests for use with ArgoCD.”。


helmfile 是一个用来管理 Kubernetes Helm Chart 的开源工具。它使用类似于 Helm 命令的语法，可以在多个 Chart 之间做依赖管理，并允许用户使用配置文件来统一管理 Chart 的安装、升级和删除。使用 helmfile 可以更好地组织和管理复杂的 Kubernetes 集群部署。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=helmfile/helmfile&type=Timeline)

### 如何安装使用

helmfile 项目可以通过多种方式安装。

1. 通过 Homebrew（macOS）或 Linuxbrew（Linux）进行安装：
```
brew install helmfile
```

2. 通过 curl 和 tar 方式安装：
```
curl -L https://github.com/roboll/helmfile/releases/download/v0.131.0/helmfile_linux_amd64 -o helmfile
chmod +x helmfile
sudo mv helmfile /usr/local/bin/
```

3. 通过 go get 安装：
```
go get -u github.com/roboll/helmfile
```

4. 通过 Helm Chart 安装：
```
helm repo add roboll https://roboll.github.io/charts
helm install roboll/helmfile
```

请确保安装了kubectl和helm.


### 使用示例 DEMO

这是一份示例 helmfile.yaml 配置文件：

```
releases:
- name: myapp
  chart: stable/mysql
  namespace: default
  values:
    mysqlRootPassword: password
    replicaCount: 3

- name: myapp2
  chart: stable/nginx-ingress
  namespace: ingress
  values:
    controller:
      service:
        type: LoadBalancer
```

使用 helmfile 命令来安装和管理 charts：

- 安装 charts：
```
helmfile apply
```

- 更新 charts：
```
helmfile apply
```

- 删除 charts：
```
helmfile delete
```

- 查看 charts 当前状态：
```
helmfile status
```

请确保在kubectl已经配置好了对应的集群，并且已经配置好了helm与集群的连接。

这只是一个简单的例子，helmfile 支持很多其他的配置选项和命令，可以参考官方文档来了解更多。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/helmfile/helmfile 

开源项目作者：helmfile

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=helmfile/helmfile)

