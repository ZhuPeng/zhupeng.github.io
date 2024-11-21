---
layout: post
title: GitHub 开源项目 stakater/Reloader 介绍，A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig – [✩Star] if you're using it!
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 stakater/Reloader，该项目在 GitHub 有超过 7.7k Star。

![](https://stats.deeptrain.net/repo/stakater/Reloader/?theme=light)

一句话介绍该项目：A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated Deployment, StatefulSet, DaemonSet and DeploymentConfig – [✩Star] if you're using it!




![Reloader-logo](https://raw.githubusercontent.com/stakater/Reloader/master/assets/web/reloader-round-100px.png)

![Get started with Stakater](https://stakater.github.io/README/stakater-github-banner.png)

![Join Slack](https://stakater.github.io/README/stakater-join-slack-btn.png)

![Chat](https://stakater.github.io/README/stakater-chat-btn.png)


###### 项目介绍

在当今动态的 Kubernetes 环境中，配置的实时更新和管理成为了许多开发者和运维团队的一大挑战。尤其是在微服务架构中，一个小小的配置变更，比如 `ConfigMap` 或 `Secret` 的更新，就需要手动重新部署相关的 Pods 以确保配置生效，这不仅耗费时间而且容易出错。这一常见痛点正是 Reloader 项目诞生的背景。

**Reloader** 是一个开源项目，旨在为 Kubernetes 提供一个优雅的解决方案，以监听 `ConfigMap` 和 `Secret` 的变化，并对相关联的 `DeploymentConfig`、`Deployment`、`DaemonSet`、`StatefulSet` 和 `Rollout` 实施滚动更新。这样，一旦有任何配置更新，就能自动触发 Pods 的更新，无需手动干预，大大提高了自动化程度和系统的灵活性。

主要功能如下：
- 自动侦测 `ConfigMap` 和 `Secret` 的改变，并进行滚动更新。
- 支持多种 Kubernetes 资源对象，包括 `DeploymentConfigs`、`Deployments`、`Daemonsets` `Statefulsets` 以及 `Rollouts`。
- 实现配置更新的即时生效而不需要重新部署 Pod。
- 提供企业版，包括 SLA 支持、Slack 支持和认证镜像。

**如何使用 Reloader：**

首先，确保你的 Kubernetes 版本 >= 1.19。接下来，通过添加相应的注解到资源的 `metadata` 中即可使用。例如，如果你有一个 `Deployment` 叫 `foo`，并且有一个 `ConfigMap` 或 `Secret`（例如 `foo-configmap` 或 `foo-secret`），只需在 `Deployment` 的 `metadata` 中添加如下注解：

```yaml
kind: Deployment
metadata:
  name: foo
  annotations:
    reloader.stakater.com/auto: "true"
```

这样，当 `foo-configmap` 或 `foo-secret` 发生变化时，Reloader 就会自动触发滚动更新。

对于特定的 `ConfigMap` 或 `Secret` 触发滚动更新，可以使用以下注解：

```yaml
kind: Deployment
metadata:
  annotations:
    configmap.reloader.stakater.com/reload: "foo-configmap"
    secret.reloader.stakater.com/reload: "foo-secret"
```

此外，Reloader 还支持通过设置 `--auto-reload-all` 标志来启用对所有资源的自动重载。

**为什么推荐 Reloader?**

Reloader 的开发活跃，得到了社区的广泛支持和认可。其简单而强大的功能，使得它成为 Kubernetes 环境中不可或缺的工具之一。该项目不仅适用于追求高自动化和敏捷开发的小团队，同样满足企业级应用的稳定性和可靠性要求。无论是小规模项目还是大型企业，Reloader 都能显著提高开发效率和系统的响应能力，是 Kubernetes 环境下管理配置更新的优选方案。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=stakater/Reloader&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/stakater/Reloader 

开源项目作者：stakater

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=stakater/Reloader)

关注我们，一起探索有意思的开源项目。

