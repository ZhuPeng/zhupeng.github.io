---
layout: post
title: GitHub 开源项目 xuri/excelize-wasm 介绍，A WebAssembly build of the Go Excelize library
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 xuri/excelize-wasm，该项目在 GitHub 有超过 0.0k Star，用一句话介绍该项目就是：“A WebAssembly build of the Go Excelize library”。

![](https://github.com/xuri/excelize-wasm/raw/main/excelize-wasm.svg)
![](https://raw.githubusercontent.com/xuri/excelize-wasm/main/chart.png)

xuri/excelize-wasm 是一个基于 WebAssembly 的开源项目，它是 Excelize 的一个分支版本。Excelize 是一个用于读写 Excel 文件的库，支持 xlsx、xlsm、xltx、xltm 等多种格式。而 excelize-wasm 则是将 Excelize 编译成 WebAssembly 模块，可在浏览器环境中使用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=xuri/excelize-wasm&type=Timeline)

### 如何安装使用

安装该项目需要使用 Go 和 JavaScript。你需要先安装 Go 环境，然后使用 Go 包管理器进行安装。

在命令行中输入以下命令安装 excelize-wasm:
```
go get -u github.com/xuri/excelize-wasm
```

在 JavaScript 中使用该项目，你需要将编译后的 wasm 文件和 JavaScript 库文件引入到项目中。

使用 npm 安装 
```
npm i excelize-wasm
```

示例代码：

```js
import { Excel } from "excelize-wasm";

const excel = new Excel();

excel.readFile(file)
  .then(() => {
    const sheetName = excel.getSheetName(1);
    const sheetData = excel.getSheet(sheetName);
    console.log(sheetData);
  })
  .catch((error) => {
    console.error(error);
  });
```

上面的代码将读取一个 Excel 文件，然后获取第一个工作表的数据并打印出来。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/xuri/excelize-wasm 

开源项目作者：xuri

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=xuri/excelize-wasm)

