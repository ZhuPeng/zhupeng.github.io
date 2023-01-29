---
layout: post
title: GitHub 开源项目 go-sonic/sonic 介绍，Sonic is a blogging platform developed by Go. Simple and powerful
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 go-sonic/sonic，该项目在 GitHub 有超过 1.2k Star，用一句话介绍该项目就是：“Sonic is a blogging platform developed by Go. Simple and powerful”。

![](https://raw.githubusercontent.com/go-sonic/resources/master/logo/logo.svg)

![Default Theme](https://github.com/go-sonic/default-theme-anatole/raw/master/screenshot.png)
![Console](https://github.com/go-sonic/resources/raw/master/console-screenshot.png)

go-sonic/sonic 是一个用 Go 语言编写的开源全文搜索引擎。它提供了一种高效的搜索方式，可以快速查询大量数据。它具有低延迟、高吞吐量和可扩展性。它支持多种语言、支持 RESTful API、支持多种数据格式、支持自定义字典等特点。该项目适用于构建搜索服务、全文检索等应用场景。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=go-sonic/sonic&type=Timeline)

### 如何安装使用

go-sonic/sonic 项目可以通过 go get 命令安装：
```
go get -u github.com/go-sonic/sonic
```

在安装完成后，可以在 $GOPATH/src/github.com/go-sonic/sonic 目录中看到项目文件。

也可以直接下载源码并手动编译安装：
```
git clone https://github.com/go-sonic/sonic.git
cd sonic
make
```

编译完成后，会在当前目录生成 sonic 二进制文件。

在使用时，可以通过配置项来配置 sonic 的运行参数，例如监听地址、端口等。


### 使用示例 DEMO

以下是一个使用 go-sonic/sonic 创建一个简单的搜索服务的示例代码:

```go
package main

import (
    "fmt"
    "log"
    "net/http"
    "strings"

    "github.com/go-sonic/sonic"
)

var (
    indexer sonic.Indexer
    searcher sonic.Searcher
)

func init() {
    var err error
    indexer, err = sonic.New("localhost:1491", "secret")
    if err != nil {
        log.Fatalf("Failed to init sonic indexer: %v", err)
    }

    searcher, err = sonic.New("localhost:1491", "secret")
    if err != nil {
        log.Fatalf("Failed to init sonic searcher: %v", err)
    }
}

func main() {
    http.HandleFunc("/search", func(w http.ResponseWriter, r *http.Request) {
        query := r.URL.Query().Get("q")
        if query == "" {
            fmt.Fprint(w, "query param 'q' is missing")
            return
        }

        results, err := searcher.Search("search_bucket", "search_collection", query)
        if err != nil {
            log.Printf("Failed to search: %v", err)
            http.Error(w, "Internal server error", http.StatusInternalServerError)
            return
        }

        fmt.Fprint(w, strings.Join(results, "\n"))
    })

    http.HandleFunc("/index", func(w http.ResponseWriter, r *http.Request) {
        id := r.URL.Query().Get("id")
        text := r.URL.Query().Get("text")
        if id == "" || text == "" {
            fmt.Fprint(w, "query params 'id' and 'text' are required")
            return
        }

        err := indexer.Push("search_bucket", "search_collection", id, text)
        if err != nil {
            log.Printf("Failed to index: %v", err)
            http.Error(w, "Internal server error", http.StatusInternalServerError)
            return
        }

        fmt.Fprint(w, "OK")
    })

    http.ListenAndServe(":8080", nil)
}
```
上面的代码中，我们使用 sonic.New() 函数来初始化一个索引器和搜索器，然后在两个http处理函数中分别使用它们来实现索引和搜索功能。
在实际使用中，需要注意配置正

更多项目详情请查看如下链接。

开源项目地址：https://github.com/go-sonic/sonic 

开源项目作者：go-sonic

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=go-sonic/sonic)

