---
layout: post
title: GitHub 开源项目 houko/wechatgpt 介绍，wechatgpt golang版 chatgpt机器人(可docker部署)，目前支持微信(wechat)，telegram（可直接加@xiaomo_chatgpt_bot体验）
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 houko/wechatgpt，该项目在 GitHub 有超过 0.2k Star，用一句话介绍该项目就是：“wechatgpt golang版 chatgpt机器人(可docker部署)，目前支持微信(wechat)，telegram（可直接加@xiaomo_chatgpt_bot体验）”。
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/docker\xe9\x83\xa8\xe7\xbd\xb2.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3837.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3840.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3850.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3845.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3847.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3844.png)
![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3843.png)

![](https://raw.githubusercontent.com/houko/wechatgpt/master/screenshots/IMG_3991.png)

"wechatgpt" 是由 houko 开发的一个 GitHub 开源项目，它是基于 OpenAI GPT-3 模型的微信公众号机器人。它可以通过微信公众号与用户进行交互，并提供自然语言处理、问答等功能。该项目是用 Python 编写的，并且可以在服务器上部署和运行。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=houko/wechatgpt&type=Timeline)

### 如何安装使用

GitHub 开源项目 houko/wechatgpt 是一个微信聊天机器人，基于 OpenAI 的 GPT-3 模型。该项目使用 Python 编写，使用者可以使用 pip 进行安装。

安装步骤：

1. 安装 Python 3
2. 安装 pip (Python 包管理器)
3. 在命令行中输入: `pip install wechatgpt`
4. 使用以上命令安装项目所需依赖

安装完成后，您可以使用以下示例代码来运行项目：

```python
from wechatgpt import WechatGPT

bot = WechatGPT()
bot.start()
```

在运行该代码之前，您需要先配置项目中的 API key 和 secret key。

更多项目详情请查看如下链接。

开源项目地址：https://github.com/houko/wechatgpt 

开源项目作者：houko

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=houko/wechatgpt)

