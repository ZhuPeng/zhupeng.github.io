---
layout: post
title: Go OpenAI - 一款开源的 OpenAI API 的 Go 语言客户端
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在我们的工作和日常生活中，人工智能已经渗透入了各个角落。从智能手机的语音助手，到各种自动化的客户服务。然而，工作来接入这些人工智能应用的过程，特别是涉及复杂的对话模型和生成模型时，常常会让开发者头疼。既要保证模型的性能和准确性，又必须处理众多的与接口相关的细节问题。而 Go 语言因其简洁、现代和快速的特点，已被广泛应用在各类高并发的服务开发中。所以，如果能有一款 Go 语言版本的 OpenAI API 客户端，将会极大方便众多 Go 开发者。

今天要给大家推荐一个 GitHub 开源项目 sashabaranov/go-openai，该项目在 GitHub 有超过 6.9k Star，用一句话介绍该项目就是：“OpenAI ChatGPT, GPT-3, GPT-4, DALL·E, Whisper API wrapper for Go”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20231203175155351.png)

###### 项目介绍

Go OpenAI 是一款开源的 OpenAI API 的 Go 语言版客户端，主要支持 ChatGPT, GPT-3, GPT-4, DALL·E 以及 Whisper 这几个常用的模型。项目的主要设计初衷，就是将多种 OpenAI 模型的功能以简洁、易用的形式，封装在一套 Go 语言接口中。这样，Go 开发者在使用这些复杂的 AI 模型时，无需操心底层的细节问题，只需要专注于自己的业务逻辑。

###### 如何使用

安装 **Go OpenAI **非常简单，只需要执行 `go get github.com/sashabaranov/go-openai`，即可在 Go 版本在 1.18 或更高的环境中，快速将其添加到项目中。

使用示例如下：
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/sashabaranov/go-openai"
)

func main() {
	client := openai.NewClient("your token")
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT3Dot5Turbo,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "Hello!",
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```
当然，除了上述例子中的 ChatGPT 的应用，README 还为你提供了 GPT-3, GPT-4, Whisper, DALL·E 等模型的使用示例，真正帮你一站式解决各类 AI 模型的接入问题。

###### 项目推介

Go OpenAI 和其他开源项目相比，最大的亮点是它将复杂的 AI 工具以最友好的方式呈现给开发者。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sashabaranov/go-openai&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/sashabaranov/go-openai 

开源项目作者：sashabaranov

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sashabaranov/go-openai)

关注我们，一起探索有意思的开源项目。

