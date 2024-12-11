---
layout: post
title: GitHub 开源项目 direnv/direnv 介绍，unclutter your .profile
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 direnv/direnv，该项目在 GitHub 有超过 12.7k Star。

![](https://stats.deeptrain.net/repo/direnv/direnv/?theme=light)

一句话介绍该项目：unclutter your .profile





###### 项目介绍

### 背景介绍

开发人员常常面临必须在不同项目之间快速切换的需求，每个项目可能因为使用不同的库、依赖或是环境变量而需要一个独立的开发环境。然而，传统的解决方案，如直接在 `~/.profile` 或其他 shell 初始化文件中设置环境变量，不仅繁琐而且容易引起混乱，尤其是当参与多个项目时。此外，直接修改全局配置可能会导致项目间的依赖冲突，增加了环境管理的复杂性。

### 

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-c487ce109585580c737caacbbf281a51.png)

项目介绍

`direnv` 是一个简化 shell 环境管理的开源工具，它提供了一种精巧的方式来根据当前目录动态加载和卸载环境变量。这意味着你可以为每个项目创建一个独立的环境，而不需要更改全局设置，从而解决了项目间依赖和环境变量冲突的问题。

核心功能包括但不限于：

- 为基于 [12factor](https://12factor.net/) 的应用程序加载环境变量；
- 创建针对每个项目隔离的开发环境；
- 为部署加载秘密信息或配置。

`direnv` 通过监听 `.envrc` （及可选的 `.env` 文件）在当前以及父目录中的变动，自动加载和卸载对应的环境变量到 shell 中。这个机制保证了环境的灵活性和隔离性，同时通过提供 `direnv stdlib` ，简化了环境变量的设置流程，使得管理项目环境变量变得既高效又轻松。

### 如何使用

首先，安装 `direnv` 可能需要通过你的操作系统的包管理器进行，具体安装说明参考 [安装文档](https://github.com/direnv/direnv/blob/master/docs/installation.md)。对于大多数 Unix 类系统和常见的 shell 环境如 bash、zsh、tcsh 和 fish，安装后需要执行与所用 shell 相关的 hook 设置命令。

```shell
$ mkdir ~/my-project
$ cd ~/my-project
$ echo export FOO=foo > .envrc
$ direnv allow .
```

在上面的例子中，我们创建了一个名为 `my-project` 的文件夹，并在其中创建了 `.envrc` 文件来导出环境变量 `FOO`。使用 `direnv allow .` 命令授权 `direnv` 加载 `.envrc` 文件，之后 `direnv` 会自动处理环境变量的加载和卸载。

### 项目推介

`direnv` 拥有活跃的开发社区，其源代码管理在 GitHub 上，这保证了项目的持续更新和改进。由于其简化和高效的环境管理能力，`direnv` 已经被许多知名的技术公司和开源项目所采纳。此外，其跨语言的适用性使得 `direnv` 成为各种编程语言开发者的首选工具，无论是 Ruby、Python 还是 PHP 的环境管理，`direnv` 都能够提供优秀的支持。

结合其简单的安装过程、强大的功能以及社区给出的广泛支持，`direnv` 是任何希望优化开发环境和提高生产效率的开发人员的必备工具。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=direnv/direnv&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/direnv/direnv 

开源项目作者：direnv

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=direnv/direnv)

关注我们，一起探索有意思的开源项目。

