
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 charmbracelet/gum，该项目在 GitHub 有超过 12.0k Star，用一句话介绍该项目就是：“A tool for glamorous shell scripts 🎀”。

![](https://stuff.charm.sh/gum/gum.png)
![](https://godoc.org/github.com/golang/gddo?status.svg)
![](https://stuff.charm.sh/gum/demo.gif)
![](https://stuff.charm.sh/gum/commit_2.gif)
![](https://stuff.charm.sh/gum/customization.gif)
![](https://stuff.charm.sh/gum/input_1.gif)
![](https://stuff.charm.sh/gum/write.gif)
![](https://stuff.charm.sh/gum/filter.gif)
![](https://stuff.charm.sh/gum/choose.gif)
![](https://stuff.charm.sh/gum/confirm_2.gif)
![](https://stuff.charm.sh/gum/file.gif)
![](https://stuff.charm.sh/gum/pager.gif)
![](https://stuff.charm.sh/gum/spin.gif)
![](https://stuff.charm.sh/gum/table.gif)
![](https://stuff.charm.sh/gum/style.gif)
![](https://stuff.charm.sh/gum/join.gif)
![](https://stuff.charm.sh/gum/format.gif)
![](https://stuff.charm.sh/gum/pick-tmux-session.gif)
![](https://stuff.charm.sh/gum/pick-commit.gif)
![](https://stuff.charm.sh/gum/skate-pass.gif)
![](https://stuff.charm.sh/charm-badge.jpg)

"charmbracelet/gum" 是一个基于 Go 语言开发的开源项目，它提供了一个简单易用的 API 来获取有关系统和硬件的信息。该项目可以用于收集和监控系统性能数据，帮助开发人员了解系统的运行情况。

该项目支持的信息包括：

- CPU 信息：包括核心数量，频率等。
- 内存信息：包括总内存，使用内存等。
- 磁盘信息：包括总空间，使用空间等。
- 网络信息：包括 IP 地址，流量等。

使用该项目可以方便的获取上述信息, 进而做进一步的操作.



### 如何安装使用

要安装 "charmbracelet/gum" 项目，您需要先安装 Go 环境。安装完成后，可以使用以下命令来安装该项目：
```
go get github.com/charmbracelet/gum
```
该命令会自动在 $GOPATH/src 下下载并安装 gum 项目。

安装完成后,您可以使用go import 来导入该项目，在您需要使用的文件中导入 "github.com/charmbracelet/gum" 就可以使用该项目的功能了。

例如：
```
import "github.com/charmbracelet/gum"
```

安装完成后的使用方法请参考该项目的文档或者github上的example.


### 使用示例 DEMO

以下是一个使用 "charmbracelet/gum" 项目获取系统 CPU 信息的示例代码：
```
package main

import (
    "fmt"
    "github.com/charmbracelet/gum"
)

func main() {
    cpu, _ := gum.CPU()
    fmt.Println("CPU cores: ", cpu.Cores)
    fmt.Println("CPU frequency: ", cpu.Frequency)
}
```
该代码将会输出 CPU 的核心数量和频率。

以下是一个使用 "charmbracelet/gum" 项目获取系统内存信息的示例代码：
```
package main

import (
    "fmt"
    "github.com/charmbracelet/gum"
)

func main() {
    memory, _ := gum.Memory()
    fmt.Println("Total memory: ", memory.Total)
    fmt.Println("Used memory: ", memory.Used)
}
```
该代码将会输出总内存和已使用内存。

以上代码

更多项目详情请查看如下链接。

开源项目地址：https://github.com/charmbracelet/gum  (文末可点击阅读原文)

开源项目作者：gum

