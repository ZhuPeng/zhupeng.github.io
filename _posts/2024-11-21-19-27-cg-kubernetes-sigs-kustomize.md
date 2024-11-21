---
layout: post
title: GitHub 开源项目 kubernetes-sigs/kustomize 介绍，Customization of kubernetes YAML configurations
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 kubernetes-sigs/kustomize，该项目在 GitHub 有超过 11.1k Star。

![](https://stats.deeptrain.net/repo/kubernetes-sigs/kustomize/?theme=light)

一句话介绍该项目：Customization of kubernetes YAML configurations





###### 项目介绍

背景介绍：

在现代软件开发中，特别是在云原生应用的部署场景下，我们常常面临配置管理的挑战。随着部署环境的增多，手动管理成百上千的 Kubernetes YAML 配置文件变得既低效也容易出错。单一的配置文件难以满足多环境、多场景的部署需求，比如为开发、测试和生产环境配置不同的参数。此外，重复和冗余的配置信息增加了维护成本，且直接修改原生 YAML 文件会破坏其通用性和可重用性。如何高效且灵活地定制 Kubernetes 配置文件，是每个云原生开发者都要面临的问题。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-b649cb3864bcb161596f8e475afa0cbf.png)

项目介绍：

`kustomize` 是一个开源工具，专为解决 Kubernetes 配置管理的挑战而设计。通过对原生、无模板的 YAML 文件进行定制，`kustomize` 允许用户针对多个目的编辑 YAML 文件，同时保持原始文件的不变和可用性。`kustomize` 理解并能够修补 Kubernetes 风格的 API 对象。它的工作原理类似于 `make` 和 `sed`，通过在文件中声明操作内容，并输出编辑后的文本。该项目由 [sig-cli] 小组赞助。

主要功能包括资源声明、自定义标签和注释添加、配置文件的生成等，支持通过简单的声明式配置文件（称为 `kustomization` 文件）来实现复杂的定制需求。`kustomize` 的设计让配置管理变得更加简洁、模块化和易于维护。

如何使用：

1. 安装 `kustomize`。可以通过访问其 [官方安装指南](https://kubectl.docs.kubernetes.io/installation/kustomize/) 来了解不同平台的安装方法。
2. 创建一个包含 Kubernetes 资源文件（如 deployments、services、configmaps 等）的目录，并在该目录中创建一个 `kustomization.yaml` 文件。
3. 单独列出管理及定制资源的配置到 `kustomization.yaml` 文件中，如需为所有资源添加一个通用标签，可以在此文件中进行配置。
   
示例 `kustomization.yaml` 文件内容：

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
commonLabels:
  app: myapp
resources:
  - deployment.yaml
  - service.yaml
configMapGenerator:
  - name: myapp-map
    literals:
      - KEY=value
```

4. 使用 `kustomize build` 命令在该目录下运行，来应用对资源的定制并输出结果。

项目推介：

`kustomize` 是 Kubernetes 社区广泛认可的配置管理工具。自从集成进 `kubectl`（从版本 1.14 开始）以来，它的影响力和使用范围大幅增加。不仅如此，由于其设计理念与 Kubernetes 原生生态紧密结合，许多重要的云原生项目和知名公司都在使用 `kustomize` 来管理他们的 Kubernetes 配置文件。此工具的开发活跃，社区支持强大，定期更新和维护，确保与 Kubernetes 生态的兼容性和进步。无论你是 Kubernetes 新手还是资深用户，`kustomize` 都是管理复杂配置的强大工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=kubernetes-sigs/kustomize&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/kubernetes-sigs/kustomize 

开源项目作者：kubernetes-sigs

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=kubernetes-sigs/kustomize)

关注我们，一起探索有意思的开源项目。

