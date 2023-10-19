---
layout: post
title: GitHub 开源项目 appleboy/CodeGPT 介绍，A CLI written in Go language that writes git commit messages or do a code review brief for you using ChatGPT AI (gpt-4, gpt-3.5-turbo model) and automatically installs a git prepare-commit-msg hook.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 appleboy/CodeGPT，该项目在 GitHub 有差不多 1000 Star，用一句话介绍该项目就是：“A CLI written in Go language that writes git commit messages or do a code review brief for you using ChatGPT AI (gpt-4, gpt-3.5-turbo model) and automatically installs a git prepare-commit-msg hook.”。

![cover](https://raw.githubusercontent.com/appleboy/CodeGPT/master/./images/cover.png)
![flow](https://raw.githubusercontent.com/appleboy/CodeGPT/master/./images/flow.svg)
![code review](https://raw.githubusercontent.com/appleboy/CodeGPT/master/./images/code_review.png)
![register](https://raw.githubusercontent.com/appleboy/CodeGPT/master/./images/register.png)
![azure01](https://raw.githubusercontent.com/appleboy/CodeGPT/master/./images/azure_01.png)
![azure02](https://raw.githubusercontent.com/appleboy/CodeGPT/master/./images/azure_02.png)





背景介绍：
在日常的代码开发过程中，我们经常会遇到需要编写 git commit 信息或进行代码审查的情况。然而，这些任务往往需要花费大量的时间和精力，而且在编写 commit 信息时，我们还需要遵循一定的规范，这无疑增加了我们的工作负担。此外，对于代码审查，我们需要对代码的改动进行详细的分析和理解，这对我们的专业知识和经验要求非常高。

项目介绍：
CodeGPT 是一个用 Go 语言编写的命令行工具，它可以帮助我们编写 git commit 信息或进行代码审查。该项目使用了 ChatGPT AI（包括 gpt-4，gpt-3.5-turbo 模型）进行自然语言处理，并自动安装 git prepare-commit-msg hook。CodeGPT 支持 Azure OpenAI 服务或 OpenAI API，支持常规提交规范，支持 Git prepare-commit-msg Hook，支持自定义生成带有 n 行上下文的差异，支持从 git diff 命令中排除文件，支持将提交信息翻译成其他语言（支持 en，zh-tw 或 zh-cn），支持 socks 代理或自定义网络 HTTP 代理，支持如 gpt-4，gpt-3.5-turbo 等模型列表，支持进行简要的代码审查。

如何使用：
在 MacOS 上，目前只支持通过 Homebrew 安装 CodeGPT。安装方法如下：

    brew tap appleboy/tap
    brew install codegpt

预编译的二进制文件可以从发布页面下载。将二进制文件的权限更改为 755，并将二进制文件复制到系统 bin 目录。然后可以使用 codegpt 命令，如下所示：

    $ codegpt version
    version: v0.4.3 commit: xxxxxxx

在使用 CodeGPT 之前，需要先创建你的 OpenAI API Key。然后，你可以将 API Key 存储在环境变量或自定义配置文件中。具体设置方法如下：

    export OPENAI_API_KEY=sk-xxxxxxx

或

    codegpt config set openai.api_key sk-xxxxxxx

项目推介：
CodeGPT 是一个非常活跃的开源项目，由知名开发者 appleboy 开发并维护。该项目的设计思路新颖，功能强大，能够极大地提高我们的开发效率。如果你在寻找一个能够帮助你编写 git commit 信息或进行代码审查的工具，那么 CodeGPT 无疑是一个非常好的选择。




以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=appleboy/CodeGPT&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/appleboy/CodeGPT 

开源项目作者：appleboy

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=appleboy/CodeGPT)

关注我们，一起探索有意思的开源项目。

