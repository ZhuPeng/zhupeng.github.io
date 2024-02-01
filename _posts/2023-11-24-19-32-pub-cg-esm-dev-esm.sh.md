---
layout: post
title: esm.sh - 一个为现代（es2015+）Web 开发设计的快速、智能、全球覆盖的 CDN
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

随着现代 web 开发的复杂性不断提升，我们需要一种快速、智能、全球覆盖的内容交付网络 ，遗憾的是，目前大多数的 CDN 都不够智能，并且在全球覆盖方面还存在不足。而这些问题，都可以通过今天推荐的项目来解决。

GitHub 开源项目 esm-dev/esm.sh 在 GitHub 有超过 2.5k Star，用一句话介绍该项目就是：“A fast, smart, & global CDN for modern(es2015+) web development.”。

![](https://raw.githubusercontent.com/esm-dev/esm.sh/master/./server/embed/assets/og-image.svg)

###### 项目介绍

esm.sh 是一个为现代（es2015+） web 开发设计的快速、智能、全球覆盖的 CDN。你可以通过一个 URL 就能够导入 es6 模块，不仅仅如此，你还可以构件一个带有自定义输入（代码）的模块。

例如：

```js
import Module from "https://esm.sh/PKG@SEMVER[/PATH]";
```

另外，esm.sh 还拥有强大的使用 npm 或者 GitHub 导入功能，使得模块的调用和使用异常轻松。以下是一个示例代码：

![](https://raw.githubusercontent.com/esm-dev/esm.sh/master/./server/embed/assets/sceenshot-deno-types.png)

###### 如何使用

使用 esm.sh 极其简单，导入模块只需要一句简单的代码：

```js
import Module from "https://esm.sh/PKG@SEMVER[/PATH]";
```

它还支持多种代码构建方式，例如使用自定义输入构建模块：

```js
import { esm } from "https://esm.sh/build";

const { render } = await esm`
  /* @jsx h */
  import { h } from "npm:preact@10.13.2";
  import { renderToString } from "npm:preact-render-to-string@6.0.2";
  export const render () => renderToString(Hello world!);
`;
console.log(render()); // "Hello world!"
```

或使用 npm 方式导入模块：

```js
import React from "https://esm.sh/react@18.2.0";
```

当然，它还支持使用 GitHub 导入模块：

```js
import tslib from "https://esm.sh/gh/microsoft/tslib@2.6.0";
```

###### 项目推介

esm.sh 是现代 web 开发工具中不可或缺的一部分，它提供了一种快速，智能且全球分布的内容传递方法，可极大提高开发效率和应用性能。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231219214828935.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=esm-dev/esm.sh&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/esm-dev/esm.sh 

开源项目作者：esm-dev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=esm-dev/esm.sh)

关注我们，一起探索有意思的开源项目。

