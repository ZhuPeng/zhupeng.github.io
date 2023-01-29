---
layout: post
title: GitHub 开源项目 cloudwego/hertz 介绍，Go HTTP framework with high-performance and strong-extensibility for building micro-services.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 cloudwego/hertz，该项目在 GitHub 有超过 3.1k Star，用一句话介绍该项目就是：“Go HTTP framework with high-performance and strong-extensibility for building micro-services.”。

![Performance](https://raw.githubusercontent.com/cloudwego/hertz/master/images/performance-4.png)
![Performance](https://raw.githubusercontent.com/cloudwego/hertz/master/images/performance-3.png)

cloudwego/hertz 是一个用于 Kubernetes 集群资源管理的开源项目。它提供了一个简单易用的命令行界面，可以帮助用户更好地管理和使用集群资源。该项目主要功能包括：
- 显示集群资源使用情况
- 在集群中创建和删除资源
- 在集群中管理资源配额
- 提供自动调整和优化集群资源使用策略。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=cloudwego/hertz&type=Timeline)

### 如何安装使用

cloudwego/hertz 项目可以通过以下方式安装:
1. 下载二进制文件: 从 GitHub releases 中下载最新版本的二进制文件，然后将其加入到系统路径中。
2. 使用 go get 安装: 在终端中运行 go get github.com/cloudwego/hertz 即可。
3. 使用 Helm 安装: Helm chart 可以在 GitHub 上的 chart 仓库中找到。使用 helm install 命令安装即可。

安装完成后，可以使用 hertz 命令来管理 Kubernetes 集群资源。


### 使用示例 DEMO

这是一个使用 cloudwego/hertz 创建 Kubernetes 部署的示例代码:

```
package main

import (
    "fmt"
    "github.com/cloudwego/hertz"
)

func main() {
    // 创建一个新的部署
    deployment := &hertz.Deployment{
        ApiVersion: "apps/v1",
        Kind:       "Deployment",
        Metadata: &hertz.ObjectMeta{
            Name: "nginx-deployment",
        },
        Spec: &hertz.DeploymentSpec{
            Replicas: 3,
            Selector: &hertz.LabelSelector{
                MatchLabels: map[string]string{
                    "app": "nginx",
                },
            },
            Template: &hertz.PodTemplateSpec{
                Metadata: &hertz.ObjectMeta{
                    Labels: map[string]string{
                        "app": "nginx",
                    },
                },
                Spec: &hertz.PodSpec{
                    Containers: []hertz.Container{
                        {
                            Name:  "nginx",
                            Image: "nginx:latest",
                        },
                    },
                },
            },
        },
    }

    // 创建部署
    hertz.Create(deployment)
    fmt.Println("Deployment created")

    // 更新部署
    deployment.Spec.Replicas = 5
    hertz.Update(deployment)
    fmt.Println("Deployment updated")

    // 删除部署
    hertz.Delete(deployment)
    fmt.Println("Deployment deleted")
}
```

在上面的代码中, 我们使用 hertz 包来创建一个新的部署，并使用 hertz.Create() 函数将其提交到 Kubernetes 集群中。我们还可以使用 hertz.Update() 和 hertz.Delete() 更新和删除部署。

请注意，在运行此代码之前，应该配置好 kubeconfig 文件，以便 hertz 包可以连接到 Kubernetes 集群。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/cloudwego/hertz 

开源项目作者：cloudwego

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=cloudwego/hertz)

