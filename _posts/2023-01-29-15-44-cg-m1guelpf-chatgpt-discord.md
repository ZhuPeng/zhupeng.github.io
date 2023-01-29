---
layout: post
title: GitHub 开源项目 m1guelpf/chatgpt-discord 介绍，Run your own GPTChat Discord bot, with a single command!
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 m1guelpf/chatgpt-discord，该项目在 GitHub 有超过 0.2k Star，用一句话介绍该项目就是：“Run your own GPTChat Discord bot, with a single command!”。


m1guelpf/chatgpt-discord 是一个使用 OpenAI 的 GPT-3 模型在 Discord 上进行自然语言处理的开源项目。它提供了一个简单的接口，可以让用户在 Discord 中轻松地与 GPT-3 进行交互，实现自然语言问答、对话等功能。这个项目可以帮助开发者快速构建自己的聊天机器人或自然语言处理应用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=m1guelpf/chatgpt-discord&type=Timeline)

### 如何安装使用

安装这个项目需要几个步骤：

1. 下载并安装 Node.js（如果你尚未安装）。
2. 在终端中使用 npm 安装 chatgpt-discord 库。
```sh
npm install chatgpt-discord
```
3. 在你的 Discord 应用中创建一个新机器人，并获取它的 token。
4. 在你的项目中创建一个新文件，并在其中导入 chatgpt-discord 库。
```js
const ChatGpt = require("chatgpt-discord");
```
5. 使用你的 OpenAI API Key 和 Discord 机器人 token 初始化 ChatGpt 实例。
```js
const chatGpt = new ChatGpt(apiKey, botToken);
```
6. 连接到 Discord 服务器并启动机器人。
```js
chatGpt.connect();
```

需要注意的是，在使用该项目需要有 OpenAI API Key，并且每月需要支付费用。

下面是一个使用 chatgpt-discord 的简单示例：

```js
const Discord = require("discord.js");
const ChatGPT = require("chatgpt-discord");

const client = new Discord.Client();

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on("message", async msg => {
  if (msg.content === "ping") {
    const chatgpt = new ChatGPT();
    const response = await chatgpt.send(msg.content);
    msg.reply(response);
  }
});

client.login(YOUR_DISCORD_TOKEN);
```

这个示例中，当用户在 Discord 中输入 "ping" 时，聊天机器人会使用 GPT-3 模型回复 "pong"。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/m1guelpf/chatgpt-discord 

开源项目作者：m1guelpf

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=m1guelpf/chatgpt-discord)

