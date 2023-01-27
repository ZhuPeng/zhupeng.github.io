
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 ChatGPT-Hackers/ChatGPT-API-server，该项目在 GitHub 有超过 0.0k Star，用一句话介绍该项目就是：“API server for ChatGPT”。



ChatGPT-Hackers/ChatGPT-API-server 是一个开源的 GitHub 项目，它是基于 ChatGPT 模型构建的 API 服务器。它可以让你使用 HTTP 协议访问 ChatGPT 的功能，帮助你在自己的项目中使用 GPT-3 的强大能力。这个项目是由 ChatGPT-Hackers 团队开发维护的，并欢迎任何人参与贡献。



### 如何安装使用

ChatGPT-Hackers/ChatGPT-API-server 项目是一个基于 Python 编写的 API 服务器，因此在安装之前需要确保已经安装了 Python 环境。

1. 从 GitHub 上克隆或下载项目源码。
2. 在命令行中进入项目根目录，运行 `pip install -r requirements.txt` 命令安装项目所需的 Python 依赖库。
3. 在项目根目录下运行`python app.py`，即可启动 API 服务。

安装完成后，就可以通过访问 http://localhost:5000/ 来查看 API 是否正常工作。

需要注意的是，这个项目需要 OpenAI API key 来使用，如果没有请先申请。


### 使用示例 DEMO

在这里给出一份 Python 代码的示例，它使用了 `requests` 库来调用 ChatGPT-API-server：

```python
import requests
import json

# API endpoint
api_url = "http://localhost:5000/predict"

# Input prompt
prompt = "What is the meaning of life?"

# OpenAI API key
api_key = "your_api_key"

# Headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Data to be sent in the API request
data = {
    "prompt": prompt
}

# Send the request
response = requests.post(api_url, headers=headers, json=data)

# Get the response
response_text = json.loads(response.text)
print(response_text["response"])
```

请替换`api_url`和`api_key`为你自己的服务器地址和 API key。这段代码会向 API 发送一个请求，并返回 GPT-3 生成的回答。

需要注意的是，这个代码示例中使用了本地服务器地址，如果你没有搭建本地服务器，请使用你自己的服务器地址。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/ChatGPT-Hackers/ChatGPT-API-server  (文末可点击阅读原文)

开源项目作者：ChatGPT-API-server

