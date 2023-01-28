---
layout: post
title: GitHub 开源项目 m1guelpf/chatgpt-telegram 介绍，Run your own GPTChat Telegram bot, with a single command!
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 m1guelpf/chatgpt-telegram，该项目在 GitHub 有超过 2.5k Star，用一句话介绍该项目就是：“Run your own GPTChat Telegram bot, with a single command!”。



m1guelpf/chatgpt-telegram 是一个基于 Telegram 和 OpenAI 的 GPT-3 语言模型的开源项目。它允许用户通过 Telegram 应用程序与 GPT-3 进行交互，并使用 GPT-3 的自然语言处理能力进行各种任务。该项目易于部署和使用，可以让用户更轻松地访问 GPT-3 的强大功能。



### 如何安装使用

m1guelpf/chatgpt-telegram 项目可以使用以下步骤安装:

1. 在 GitHub 上克隆该项目：`git clone https://github.com/m1guelpf/chatgpt-telegram.git`

2. 进入项目目录：`cd chatgpt-telegram`

3. 创建并激活虚拟环境（可选）：`python -m venv env` 和  `source env/bin/activate`

4. 安装所需的 Python 依赖：`pip install -r requirements.txt`

5. 创建一个 Telegram bot，并获取 bot token

6. 创建 .env 文件，并设置 Telegram bot token: `echo "TELEGRAM_TOKEN=YOUR_TOKEN" > .env`

7. 在 OpenAI 上创建一个 API key

8. 设置 OpenAI API key 和 session ID: `echo "OPENAI_API_KEY=YOUR_KEY" >> .env` and `echo "OPENAI_SESSION_ID=YOUR_SESSION_ID" >> .env`

9. 运行项目：`python bot.py`

安装完成后，您可以使用 Telegram 与 GPT-3 进行交互。


### 使用示例 DEMO

以下是一个使用 m1guelpf/chatgpt-telegram 项目的简单示例：

```python
import openai_secret_manager

# 获取 OpenAI API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")

print(secrets)

import openai
openai.api_key = secrets["api_key"]

# 设置 GPT-3 模型和提问
model_engine = "text-davinci-002"
prompt = (f"write a short story with a beginning, middle, and end.")

# 使用 GPT-3 生成文本
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# 输出生成的文本
message = completions.choices[0].text
print(message)
```

这段代码使用 OpenAI 的 API key 从 GPT-3 模型中生成了一段长度为 1024 个词的文本，并将其打印出来。可以根据需要调整提问和其他参数。

注意：本例中使用的是试用版 API key, 你需要登录 OpenAI 官网创建你自己的 API key,并使用它来调用 GPT-3 API


更多项目详情请查看如下链接。

开源项目地址：https://github.com/m1guelpf/chatgpt-telegram

开源项目作者：m1guelpf

