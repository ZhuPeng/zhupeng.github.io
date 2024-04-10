---
layout: post
title: 支持日志添加色彩的轻量级工具库
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在日常的开发过程中，控制台日志是我们调试问题、了解系统运行状态的重要手段之一，然而众所周知，传统的控制台日志都是单调的黑白文本，分析和查看起来费时费力，同时也缺乏美观性。对于编程者来说，如果有丰富多彩的日志输出，不仅可以提升查看体验，也更有利于我们快速定位和理解关键信息。

今天要给大家推荐一个 GitHub 开源项目 lmittmann/tint，该项目在 GitHub 有差不多 1000 Star，一句话介绍该项目： slog.Handler that writes tinted (colorized) logs

![](https://github.com/lmittmann/tint/assets/3458786/3d42f8d5-8bdf-40db-a16a-1939c88689cb)

###### 项目介绍

`tint` 是一个开源的 `slog.Handler`，可以实现给日志添加色彩的功能。它的输出格式深受 `zerolog.ConsoleWriter` 和 `slog.TextHandler` 的影响。并提供自定义的 `Options`，让你可以根据需要调整日志格式。

###### 如何使用

你可以通过 `go get` 命令轻松获取 `tint`：

```
go get github.com/lmittmann/tint
```

使用起来非常简单，你只需在新建 `logger` 时，用 `tint` 作为它的 Handler 即可：

```go
w := os.Stderr

// create a new logger
logger := slog.New(tint.NewHandler(w, nil))
```

你也可以自定义一些属性，比如不展示时间：

```go
// create a new logger that doesn't write the time
w := os.Stderr
logger := slog.New(
    tint.NewHandler(w, &tint.Options{
        ReplaceAttr: func(groups []string, a slog.Attr) slog.Attr {
            if a.Key == slog.TimeKey && len(groups) == 0 {
                return slog.Attr{}
            }
            return a
        },
    }),
)
```

比如自动展示颜色：

```go
w := os.Stderr
logger := slog.New(
    tint.NewHandler(w, &tint.Options{
        NoColor: !isatty.IsTerminal(w.Fd()),
    }),
)
```

###### 项目推介

`tint` 是一个功能强大，使用方便的日志代理库。它无依赖，轻量级，非常适合在各类 Golang 项目中使用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=lmittmann/tint&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/lmittmann/tint 

开源项目作者：lmittmann

开源协议：MIT License

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=lmittmann/tint)

关注我们，一起探索有意思的开源项目。

