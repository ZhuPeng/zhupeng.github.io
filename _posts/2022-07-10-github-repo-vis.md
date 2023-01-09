---
layout: post
title: GitHub 开源项目图形可视化一览，快速了解开源项目利器
tags: GitHub
---

大家好。

不知道大家知道吗？在 GitHub 有这样一个组织，叫 GitHub Next，里面有各种 GitHub 为了探索未来软件开发相关的开源项目。

![image-20220710233322084](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220710233322084.png)

今天要介绍的一个项目就是其中之一，repo-visualizer，它能够将 GitHub 上的任一个开源项目生成可视化的图片，能够帮助我们快速对一个项目的代码组织进行了解，这个工具对于一个初学者来说非常的有帮助。我们来看一下实际效果会比较的直观。

![image-20220710233550195](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220710233550195.png)

上图中将 [paperjs/paper.js](https://github.com/paperjs/paper.js) 这个项目的代码结构进行了可视化，其中白色圆圈代表了文件夹，有颜色的圆圈代表具体的文件，而不同颜色代表了不同的语言的源码文件，圆圈的大小对应的文件夹、文件的大小。

初看这种可视化的图，可能不能直接发现什么规律，但是你一旦熟悉了这样可视化的方式，对你快速了解一个陌生的项目还是非常有帮助的。相比树形结果，以上的可视化效果更加的直观，而且包含的信息量更多。比如文件或者文件夹的大小可以直观的看到；文件夹中的文件类型也能直接看到，从而可以去推断对应的文件夹在项目中的作用，比如如果某个文件夹下都是 Markdown 文件，那一般这个文件夹对应的是文档。

![image-20220710234152547](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20220710234152547.png)

目前可以通过以上 GitHub Action 的方式生成以上可视化图片。

另外还提供了一个不保证一定可用的网站：https://mango-dune-07a8b7110.1.azurestaticapps.net/

使用  https://mango-dune-07a8b7110.1.azurestaticapps.net/?repo=paperjs%2Fpaper.js  （加 repo 参数）即可链接到具体的某个仓库。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/githubocto/repo-visualizer

开源项目作者：GitHub