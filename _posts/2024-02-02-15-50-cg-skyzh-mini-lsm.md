---
layout: post
title: GitHub 开源项目 skyzh/mini-lsm 介绍，A tutorial of building an LSM-Tree storage engine in a week!
tags: 
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 skyzh/mini-lsm，该项目在 GitHub 有超过 1.9k Star，用一句话介绍该项目就是：“A tutorial of building an LSM-Tree storage engine in a week!”。


![banner](https://raw.githubusercontent.com/skyzh/mini-lsm/master/./mini-lsm-book/src/mini-lsm-logo.png)
![Tutorial Roadmap](https://raw.githubusercontent.com/skyzh/mini-lsm/master/./mini-lsm-book/src/lsm-tutorial/00-full-overview.svg)



项目介绍文案：

1、背景介绍：
对于计算机科学学习者或是具有相关项目需求的开发者来说，想要自己动手构建一个具有良好作者讲解的存储引擎可能并不易实现。尤其是 LSM 树（Log-structured Merge-tree）存储引擎，为了适配大数据和高写入量场景，设计和实现上都需要投入较大的精力来完成。此时，如果有一个详细的项目教程引导你走过这个复杂的过程，那将是一件大事。

2、项目介绍：
"LSM in a Week" 是一个开源的教学项目，旨在指导用户在一个星期之内构建一个简单的 LSM 树存储引擎。项目为有志于专研 LSM 存储引擎的开发者提供了极好的学习机会。它通过详细的教程文档，指导开发者从入门到实现整个存储引擎。三周的教程安排合理，每一天的学习任务清晰，使得用户学习的过程不会过于困难。

3、如何使用：
首先，用户需要将项目 clone 到本地：`git clone https://github.com/skyzh/mini-lsm.git`。
接着，跟随给出的教程在 `mini-lsm-starter` 目录下开始编写你的 code：
```
cargo x install-tools
cargo x copy-test --week 1 --day 1
cargo x scheck
cargo run --bin mini-lsm-cli
cargo run --bin compaction-simulator
```
同时，项目还提供了成品的参考解决方案供开发者参考：
```
cargo run --bin mini-lsm-cli-ref
cargo run --bin mini-lsm-cli-mvcc-ref
```
并有一个压实算法模拟器供开发者使用来实验你的压实算法：
```
cargo run --bin compaction-simulator-ref
cargo run --bin compaction-simulator-mvcc-ref
```
教程书籍可供在线阅读：[https://skyzh.github.io/mini-lsm](https://skyzh.github.io/mini-lsm) 。

4、项目推介：
"LSM in a Week" 是一个非常活跃的开源项目，尽管该项目是由个人作者 skyzh 设计并主导维护的，但其丰富的内容和明确的教程安排吸引了大量的学习者。利用这个项目，你能够以较小的成本取得显著的学习效果。作者 skyzh 在项目中返回贡献者的 pr ，如果你也希望加入开源贡献者的行列，这个项目将是你的良好起点。结合项目教程的详细程度以及作者对项目的细心维护，我们强烈推荐这个迷你 LSM 存储引擎构建教程项目给有相关需求的开发者。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=skyzh/mini-lsm&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/skyzh/mini-lsm 

开源项目作者：skyzh

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=skyzh/mini-lsm)

关注我们，一起探索有意思的开源项目。

