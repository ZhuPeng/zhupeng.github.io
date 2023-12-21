---
layout: post
title: GitHub 开源项目 FalconForceTeam/FalconHound 介绍，FalconHound is a blue team multi-tool. It allows you to utilize and enhance the power of BloodHound in a more automated fashion. It is designed to be used in conjunction with a SIEM or other log aggregation tool. 
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 FalconForceTeam/FalconHound，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“FalconHound is a blue team multi-tool. It allows you to utilize and enhance the power of BloodHound in a more automated fashion. It is designed to be used in conjunction with a SIEM or other log aggregation tool. ”。


![Discord Shield](https://discordapp.com/api/guilds/715302469751668787/widget.png?style=shield)
![logo](https://raw.githubusercontent.com/FalconForceTeam/FalconHound/master/docs/falconhound-logo.png)



背景介绍：
在网络安全防御中，我们面临的挑战之一是要及时了解和追踪我们环境的组织结构和用户关系等关键信息，这对于准确有效的应对攻击尤为重要。然而，这非常困难，因为有时候，当我们需要这些信息时，常常因为环境的持续变化和信息的沉淀而无法得到最新的环境快照。更为糟糕的是，有些信息，比如本地组成员关系和会话信息，这些都需要我们从日志中提取。这种情况使得我们对于组织环境的安全看警变得困难重重。

项目介绍：
FalconHound项目为此问题提供了一种解决方案。这是一个多功能的蓝队工具，主要被设计为与 SIEM 或其​他日志聚合工具一同使用。其主要三个功能区为：环境实时模型构建、日志信息图形化表示以及警报和丰富图的生成。 

FalconHound 的设计使得环境的状态图一直处于最新状态，无论环境如何变化，它都能够捕捉到。另外，它还支持将本地组成员关系和会话信息等等，提取出这些信息并将其添加到环境的状态图中。 F​alconHound 还可以利用图形触发警报或者生成丰富的统计信息，比如某个用户被添加进一个特定的组， FalconHound会查找这个用户到一个敏感组或者高权限组的最短路径，如果存在这样的路径，就记入SIEM或者生成警报。

如何使用：
由于 FalconHound 是用 Go 语言写成的，所以无须安装，只需下载已编译的二进制文件并运行，系统支持包括 Windows、Linux 和 MacOS。您还需要创建一个配置文件，配置文件的样例已经在项目的根目录提供 

默认运行，使用如下命令：
```bash
./falconhound -go
```
列出所有启用的操作，使用如下命令：
```bash
./falconhound -actionlist -go
```
使用选择的操作运行，使用如下命令：
```bash
./falconhound -ids action1,action2,action3 -go
```
项目推介：
FalconHound 是 FalconForceTeam 的开源项目，该团队在网络安全领域具有很高的知名度和实力。该项目的源码活跃，同时也有详细的使用说明文档和示例，有问题也可在 issue 区提问，得到及时的解答。虽然 FalconHound 是新开源的项目，但因其设计的独特性以及强大的功能已经吸引了 Github 社区的注意，愿更多的开发者和使用者对其进行关注和试用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=FalconForceTeam/FalconHound&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/FalconForceTeam/FalconHound 

开源项目作者：FalconForceTeam

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=FalconForceTeam/FalconHound)

关注我们，一起探索有意思的开源项目。

