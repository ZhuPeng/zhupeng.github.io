---
layout: post
title: GitHub 开源项目 tellerops/teller 介绍，Cloud native secrets management for developers - never leave your command line for secrets.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 tellerops/teller，该项目在 GitHub 有超过 2.3k Star，用一句话介绍该项目就是：“Cloud native secrets management for developers - never leave your command line for secrets.”。


![](https://raw.githubusercontent.com/tellerops/teller/master/media/providers.png)
![](https://raw.githubusercontent.com/tellerops/teller/master/media/teller.gif)
![](https://user-images.githubusercontent.com/83390/117453797-07512380-af4e-11eb-949e-cc875e854fad.png)
![](https://raw.githubusercontent.com/tellerops/teller/master/media/teller-logo.png)
![](https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=332313&theme=light)



背景介绍：

在开发、测试、构建应用过程中，我们经常会遇到一个问题，如何安全、方便地使用各种秘钥？现如今许多秘钥和敏感信息比如 token，AWS 密钥等都需要被保存在我们的开发环境中。往往我们为了方便，将这些信息导出环境变量或者硬编码在本地的 .env 文件，都可能会导致这敏感信息的泄露。多云秘钥管理更增加了复杂性，我们希望有一套工具，可以集中、安全地对各种密钥进行管理。

项目介绍：

`Teller` 是一个开源的云原生秘钥管理系统，它可以在终端使用，为开发提供了简单便捷的工作流。它不仅可以用于你的本机环境，也能很好为你的团队提供流程和最佳实践。`Teller` 支持多种秘钥存储服务，如 Hashicorp Vault，AWS Secrets Manager，Google Secret Manager 等等。你可以使用 `Teller` 来优化你的环境，也可以为你的团队实施最佳实践。

安装使用：

`Teller` 可以通过 homebrew 进行安装：

```bash
$ brew tap spectralops/tap && brew install teller
```

可以使用 `teller` 或 `tlr` 在终端进行各项操作。

对于使用 Github Actions 的用户，你可以快速的在一次点击过程中在 CI 安装 Teller：

```yaml
- name: Setup Teller 
  uses: spectralops/setup-teller@v1 
- name: Run a Teller task (show, scan, run, etc.) 
  run: teller run [args]
```

运行 `teller new` ，按照向导的提示选择你需要的服务，它会为你生成 `.teller.yml` 文件。或者你可以根据下面的模板进行配置：

```yaml
project: project_name
opts:
  stage: development

# remove if you don't like the prompt
confirm: Are you sure you want to run in {{stage}}?

providers:
  # uses environment vars to configure
  # https://github.com/hashicorp/vault/blob/api/v1.0.4/api/client.go#L28
  hashicorp_vault:
    env_sync:
      path: secret/data/{{stage}}/services/billing

  # this will fuse vars with the below .env file
  # use if you'd like to grab secrets from outside of the project tree
  dotenv:
    env_sync:
      path: ~/billing.env.{{stage}}
```

进行配置后，你可以直接用以下命令运行进程：

```bash
$ teller run node src/server.js
Service is up.
Loaded configuration: Mailgun, SMTP
Port: 5050
```

项目推介：

`Teller` 是一个由 Spectralops 开发和维护的开源项目，该公司在云原生环境下的开发工作流方面有着丰富的经验。项目目前在 Github 上有近百颗星，并维护活跃。如果你在寻找一个能够帮助你安全地管理各种密钥，提供云原生工作流的工具，在此我很高兴向你推荐 `Teller`！


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tellerops/teller&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tellerops/teller 

开源项目作者：tellerops

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tellerops/teller)

关注我们，一起探索有意思的开源项目。

