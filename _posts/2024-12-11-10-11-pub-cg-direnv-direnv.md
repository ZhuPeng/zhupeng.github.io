---
layout: post
title: 基于目录的项目环境变量隔离工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

开发人员常常面临必须在不同项目之间快速切换的需求，每个项目可能因为使用不同的库、依赖或是环境变量而需要一个独立的开发环境。然而，传统的解决方案，如直接在 `~/.profile` 或其他 shell 初始化文件中设置环境变量，不仅繁琐而且容易引起混乱，尤其是当参与多个项目时。此外，直接修改全局配置可能会导致项目间的依赖冲突，增加了环境管理的复杂性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-c487ce109585580c737caacbbf281a51.png)

今天要给大家推荐一个 GitHub 开源项目 direnv，该项目在 GitHub 有超过 12.7k Star。

![](https://stats.deeptrain.net/repo/direnv/direnv/?theme=light)

一句话介绍该项目：unclutter your .profile

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241211233137800.png)

###### 项目介绍

`direnv` 是一个简化 shell 环境管理的开源工具，它提供了一种精巧的方式来根据当前目录动态加载和卸载环境变量。这意味着你可以为每个项目创建一个独立的环境，而不需要更改全局设置，从而解决了项目间依赖和环境变量冲突的问题。

典型使用场景包括如下：

1、为基于 12factor 的应用程序加载环境变量

2、创建针对每个项目隔离的开发环境

3、为部署加载秘密信息或配置

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241211233301174.png)

`direnv` 通过监听 `.envrc` （及可选的 `.env` 文件）在当前以及父目录中的变动，自动加载和卸载对应的环境变量到 shell 中。这个机制保证了环境的灵活性和隔离性，同时通过提供 `direnv stdlib` ，简化了环境变量的设置流程，使得管理项目环境变量变得既高效又轻松。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241211233329364.png)

###### 如何使用

安装流程整体参考如下：

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241211233422422.png)

可使用如下包管理器进行安装

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241211233505802.png)

或者使用命令行安装

```bash
curl -sfL https://direnv.net/install.sh | bash
```

安装后使用方式参考如下：

```shell
$ mkdir ~/my-project
$ cd ~/my-project
$ echo export FOO=foo > .envrc
$ direnv allow .
$ echo ${FOO-nope}
foo
# Exit the project
$ cd ..
direnv: unloading
# And now FOO is unset again
$ echo ${FOO-nope}
nope
```

###### 项目推介

由于 direnv 其简化和高效的环境管理能力，已经被许多知名的技术公司和开源项目所采纳。此外，其跨语言的适用性使得 `direnv` 可以支持各种编程语言的环境管理，比如 Ruby、Python、PHP 等。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=direnv/direnv&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/direnv/direnv 

开源项目作者：direnv

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=direnv/direnv)

关注我们，一起探索有意思的开源项目。

