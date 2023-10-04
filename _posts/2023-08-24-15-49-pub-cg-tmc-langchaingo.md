---
layout: post
title: LangChain 的 Go 语言实现
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

LangChain 是大模型应用的明星项目，但是其使用的是 Python 进行开发的，可能很多的公司并不是正在使用 Python，这样就很难融入到已有的基础设施之上，比如现在有不少公司使用 Go 语言开发，那如果也要使用 LangChain 这样的项目，应该怎么办？

今天要给大家推荐一个 GitHub 开源项目 tmc/langchaingo，该项目在 GitHub 有超过 1k Star，用一句话介绍该项目就是：“LangChain for Go”。

LangChain Go 是一个通过组合实现 LLMs 的 Go 语言实现。在自然语言处理中，LLMs（Language Model Microservices）是一种常见的技术，用于实现文本生成、文本分类、语音转换等功能。但是，LLMs 的实现通常需要大量的代码和复杂的架构，这使得它们难以重用和扩展。LangChain Go 通过提供一种简单的组合方式，使得 LLMs 可以更加容易地重用和扩展。

使用 LangChain Go，您可以轻松地创建自己的 LLMs，同时也可以使用其他人创建的 LLMs。LangChain Go 提供了一些常见的 LLMs 实现，您可以使用这些实现来生成文本、分类文本、转换语音等。

要使用 LangChain Go，您需要先安装它。您可以通过以下命令来安装：

```bash
go get github.com/tmc/langchaingo
```

安装完成后，您可以使用以下代码来调用 OpenAI LLMs：

```go
import (
    "context"
    "log"
    "github.com/tmc/langchaingo/llms/openai"
)

func main() {
    llm, err := openai.New()
    if err != nil {
        log.Fatal(err)
    }
    prompt := "What would be a good company name for a company that makes colorful socks?"
    completion, err := llm.Call(context.Background(), prompt)
    if err != nil {
        log.Fatal(err)
    }
    log.Println(completion)
}
```

LangChain Go 是一个非常有用的开源项目，它可以帮助您更轻松地实现 LLMs，并且可以提高您的工作效率。如果您正在寻找一个简单而强大的 LLMs 实现，那么 LangChain Go 绝对值得一试。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=tmc/langchaingo&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/tmc/langchaingo 

开源项目作者：tmc

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=tmc/langchaingo)

关注我们，一起探索有意思的开源项目。

