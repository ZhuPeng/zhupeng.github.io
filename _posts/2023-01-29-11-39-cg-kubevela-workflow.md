---
layout: post
title: GitHub 开源项目 kubevela/workflow 介绍，Declarative Workflow of KubeVela which can run as standalone.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 kubevela/workflow，该项目在 GitHub 有超过 0.1k Star，用一句话介绍该项目就是：“Declarative Workflow of KubeVela which can run as standalone.”。

![](https://static.kubevela.net/images/1.6/workflow-arch.png)

kubevela/workflow 是一个开源的 Kubernetes 工作流编排工具。它可以帮助用户在 Kubernetes 集群中管理和调度工作流。该项目提供了一组灵活的 API 和命令行工具，可以轻松地编排、部署和管理工作流。

它还提供了一个可视化的 Web 界面，可以帮助用户直观地了解工作流的运行状态和历史记录。

kubevela/workflow 可以通过 kubectl 插件的形式集成到 Kubernetes 集群中，并支持多种工作流语言，如 YAML、JSON、HCL 和 JSONnet。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubevela/workflow&type=Timeline)

### 如何安装使用

kubevela/workflow 可以通过两种方式安装:

1. 使用 kubectl plugin 安装:
```
$ kubectl kubectl plugin install workflow
```

2. 使用 Helm 安装:
```
$ helm repo add kubevela https://charts.kubevela.io
$ helm install kubevela/workflow --name my-release
```

请确保在安装前已经安装了 kubectl 与 kubectx 以及对 Kubernetes 集群有操作权限。

安装完成后可以使用 kubectl workflow 命令来管理工作流。


### 使用示例 DEMO

以下是一个使用 kubevela/workflow 创建一个简单工作流的示例代码:

```
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: hello-world-
spec:
  entrypoint: hello-world
  templates:
  - name: hello-world
    container:
      image: alpine:3.6
      command: [echo, "hello world"]
```

该代码定义了一个名为 "hello-world" 的工作流，该工作流的入口点是 "hello-world" 模板。在 "hello-world" 模板中，使用了一个名为 "alpine:3.6" 的镜像，该镜像运行了 "echo "hello world"" 命令。

可以使用 kubectl apply 命令将该工作流部署到 Kubernetes 集群中:
```
$ kubectl apply -f workflow.yaml
```

然后使用 kubectl get 命令查看工作流的状态:
```
$ kubectl get wf
```

您也可以使用 kubectl logs 命令查看工作流的日志:
```
$ kubectl logs -f <workflow-name> -n <namespace>
```

请注意，您需要替换 <workflow-name> 和 <namespace> 为实际的值。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubevela/workflow 

开源项目作者：kubevela

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubevela/workflow)

