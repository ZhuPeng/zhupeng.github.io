---
layout: post
title: ChatGPT 与命令行的完美结合，极大提升开发效率
tags: ChatGPT
---

大家好，又见面了，我是 GitHub 精选君！

**背景介绍**

在日常开发中，我们经常会遇到需要查找代码、改进代码库以及对代码进行评审的情况。同时，我们也需要进行代码重构、生成测试代码、执行Shell命令等任务。这些操作往往需要借助浏览器查找相关的信息，存在多个软件的切换，可能会花费大量的时间和精力，降低开发效率。为了解决这些问题，今天要介绍一个多功能命令行工具：auto-copilot-cli。

**项目介绍**

auto-copilot-cli 是一个功能丰富的工具，提供了多项功能，包括：

- AI代码交互：帮助您快速查找和改进代码库，并回答与代码相关的问题。
- 代码评审：提供代码评审功能，帮助您发现潜在的问题并提出改进建议。
- 提交前代码检查：生成提交消息的预提交钩子，提供代码质量保证。
- 代码重构和代码风格检查：支持对文件夹或文件的代码重构和代码风格检查。
- 测试代码生成：自动生成测试代码，提高测试覆盖率。
- Shell命令生成与执行：自动生成Shell命令并执行。
- 自然语言转SQL：将自然语言转换为SQL查询语句。

**如何使用**

您可以按照以下步骤安装和使用auto-copilot-cli：

1. 全局安装auto-copilot-cli：
   ```bash
   # 使用npm安装
   npm install -g auto-copilot-cli
   
   # 使用安装脚本
   curl -s https://raw.githubusercontent.com/rsaryev/auto-copilot-cli/main/deployment/deploy.bash | bash
   ```
2. 从[OpenAI](https://platform.openai.com/account/api-keys)获取API密钥。
3. 参考[CLI使用指南](https://github.com/rsaryev/auto-copilot-cli/blob/main/docs/usage.md)了解如何使用该工具。

示例命令：
- `code-chat` - 与AI交互，解决代码问题。

![](https://user-images.githubusercontent.com/70219513/240761672-8deb1865-6ec6-4dc8-a631-344627dabb83.gif)

- `code-review` - 进行代码评审。

![](https://user-images.githubusercontent.com/70219513/238583075-d7abc8d7-9f5e-441c-8662-fe657ee07922.gif)

- `test` - 生成测试代码。

![](https://user-images.githubusercontent.com/70219513/238206691-e405d17f-598c-457e-9827-1f7d8117e2b7.gif)

- `refactor` - 重构代码。

![](https://user-images.githubusercontent.com/70219513/238206512-2c7da6ed-d74a-4aa3-a6d0-33031cc492c0.gif)

- `sql-translator` - 自然语言转SQL。

![](https://user-images.githubusercontent.com/70219513/238206228-aa3c88d0-d747-48be-8406-7dbdab11061e.gif)

- `pre-commit`- 自动根据 code diff 生成 commit message。

![](https://user-images.githubusercontent.com/70219513/238206217-805175ca-2d23-4468-9e11-8e3e1c1174cb.gif)

以下是该项目 Star 趋势图（代表项目的活跃程度）想·：

![](https://api.star-history.com/svg?repos=rsaryev/auto-copilot-cli&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/rsaryev/auto-copilot-cli 

开源项目作者：rsaryev

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=rsaryev/auto-copilot-cli)

关注我们，一起探索有意思的开源项目。

