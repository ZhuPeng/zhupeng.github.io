---
layout: post
title: 一款简单上手的开源 2D 游戏引擎
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

对于开发者们来说，创建一款跨平台的 2D 游戏开发项目是一项令人头疼的挑战。他们常常需要面对多种程序语言和框架的学习曲线，以及不同平台间复杂的兼容性问题。此外，为了实现丰富的游戏效果和流畅的用户体验，高效的图形渲染和输入处理机制成为了核心痛点。这些问题无不增加了开发者们在游戏开发过程中的负担。

今天要给大家推荐一个 GitHub 开源项目 ebiten，该项目在 GitHub 有超过 11.2k Star。

![](https://stats.deeptrain.net/repo/hajimehoshi/ebiten/?theme=light)

一句话介绍该项目：Ebitengine - A dead simple 2D game engine for Go

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241113232455086.png)

###### 项目介绍

Ebitengine 是一个基于 Go 语言的开源 2D 游戏引擎，以其简洁的 API 和出色的跨平台兼容性脱颖而出，使得开发者能够轻松快速地开发和部署跨平台 2D 游戏。**Ebitengine** 支持包括 **Windows、macOS、Linux、FreeBSD、Android、iOS、WebAssembly**，乃至 **Nintendo Switch 和 Xbox** 在内的多个平台，充分展示了其强大的跨平台功能。

![](https://ebitengine.org/images/overview2.png)

**Ebitengine** 的特点集中在其丰富的 2D 图形能力，如通过矩阵实现的几何和颜色变换、不同的组合模式、离屏渲染、文本渲染等，以及支持各种输入（鼠标、键盘、游戏手柄、触摸）和音频格式（Ogg/Vorbis、MP3、WAV、PCM）的处理。此外，**Ebitengine** 提供自动批处理、自动纹理地图和自定义着色器功能，极大简化了游戏开发中的图形渲染流程。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241113232610760.png)

###### 如何使用

通过以下命令安装 **Ebitengine**：

```bash
go get github.com/hajimehoshi/ebiten/v2
```

以下是一个简单的代码示例，展示了如何创建一个窗口并在其中绘制图形：

```go
package main

import (
	"log"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

type Game struct{}

func (g *Game) Update() error {
	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	ebitenutil.DebugPrint(screen, "Hello, World!")
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
	return 320, 240
}

func main() {
	ebiten.SetWindowSize(640, 480)
	ebiten.SetWindowTitle("Hello, World!")
	if err := ebiten.RunGame(&Game{}); err != nil {
		log.Fatal(err)
	}
}
```

这个简单的例子展示了 **Ebitengine** 的一些基本用法。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241113232918246.png)

###### 项目推介

凭借其开放源代码的特点和 Apache license 2.0 许可，**Ebitengine** 吸引了全球许多开发者的关注和贡献，是开发 2D 游戏的优秀选择。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20241113233045186.png)

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=hajimehoshi/ebiten&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/hajimehoshi/ebiten 

开源项目作者：hajimehoshi

开源协议：Apache License 2.0

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=hajimehoshi/ebiten)

关注我们，一起探索有意思的开源项目。

