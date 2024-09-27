---
layout: post
title: 追求极致构建速度的 Web 打包工具
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在当前的 Web 开发过程中，构建工具的性能往往成为了一个不容忽视的瓶颈。由于项目的复杂度日益增加，依赖的模块数量剧增，传统的构建工具如 webpack、Rollup 等虽然功能强大，但在构建速度上往往无法满足开发者追求高效的需求。构建慢不仅影响开发者的开发体验，也间接影响了项目的迭代速度。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-105fbc290958dd22edc9b7fe901804d8.png)

今天要给大家推荐一个 GitHub 开源项目 esbuild，该项目在 GitHub 有超过 37.8k Star。

![](https://stats.deeptrain.net/repo/evanw/esbuild/?theme=light)

一句话介绍该项目：An extremely fast bundler for the web


![](https://raw.githubusercontent.com/evanw/esbuild/master/./images/wordmark-light.svg)

![](https://raw.githubusercontent.com/evanw/esbuild/master/./images/benchmark-light.svg)


###### 项目介绍

esbuild 是一个追求极致构建速度的 Web 打包工具，它通过利用 Go 语言的高性能特点，解决了现有 Web 构建工具速度慢的问题，使构建速度提升了 10-100 倍。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240908221733542.png)

esbuild 的主要功能包括：

1、不依赖缓存实现极速构建

2、内置对 JavaScript、CSS、TypeScript 以及 JSX 的支持

3、提供了简单直观的 API，支持 CLI、JS 和 Go

4、支持打包 ESM 和 CommonJS 模块

5、支持 CSS 构建，包括 CSS 模块

6、支持 Tree shaking、代码压缩(minification) 和源码映射(source maps)

7、提供本地服务器、监听模式(watch mode) 和插件系统

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240908221840827.png)

###### 如何使用

可以通过 npm 来安装 esbuild：

```shell
npm install esbuild --save-dev
```

通过简单的命令行指令即可进行构建，例如，将一个 JavaScript 文件构建成一个打包文件：

```shell
npx esbuild app.js --bundle --outfile=bundle.js
```

对于更复杂的使用场景，esbuild 提供了详细的 [API Document](https://esbuild.github.io/api/) 文档，可以通过这些 API 来实现高度定制化的构建过程。

###### 项目推介

esbuild 凭借其惊人的构建速度和易用性，迅速在开发者中获得了广泛的认可和好评。尽管是一个相对较新的项目，esbuild 已经被众多知名公司和项目采用，表明了其稳定性和实用性。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240908222005797.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=evanw/esbuild&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/evanw/esbuild 

开源项目作者：evanw

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=evanw/esbuild)

关注我们，一起探索有意思的开源项目。

