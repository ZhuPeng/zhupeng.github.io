---
layout: post
title: GitHub 开源项目 1Password/shell-plugins 介绍，Seamless authentication for every tool in your terminal.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 1Password/shell-plugins，该项目在 GitHub 有超过 0.2k Star，用一句话介绍该项目就是：“Seamless authentication for every tool in your terminal.”。

![](https://user-images.githubusercontent.com/7430639/205342015-46801fd8-6701-482f-9da9-e21e7e39b3a1.svg)
![](https://user-images.githubusercontent.com/7430639/205337855-41604aca-0ddb-4eab-a5f0-fb9107e09d8d.gif)

"1Password/shell-plugins" 是 1Password 公司在 GitHub 上开源的一个项目，该项目提供了一系列 shell 插件，可以与 1Password 命令行客户端配合使用，帮助用户在命令行中管理和使用 1Password 密码。这些插件可以实现如自动填充密码、查找密码等功能，大大提高了命令行下的密码管理效率。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=1Password/shell-plugins&type=Timeline)

### 如何安装使用

安装这个项目需要先在你的设备上安装 1Password 应用程序，然后再安装 shell-plugins。

可以使用以下命令安装:
```
# 安装op
brew cask install 1password

# 安装shell-plugins
op install shell
```
然后在命令行输入 `op` 就可以使用了。

具体使用可以参考项目的文档，或者使用 `op help` 查看帮助文档。


### 使用示例 DEMO

由于 1Password/shell-plugins 是一个 shell 插件库，其安装和使用方式因具体插件而异。请确保您已经安装了 1Password 客户端并且已经在 shell 中配置好了 1Password。

下面是一个使用 1Password/shell-plugins 中的 op 插件的示例代码：

```
# 从 1Password/shell-plugins 中安装 op 插件
curl -s https://raw.githubusercontent.com/1Password/shell-plugins/main/install.sh | bash

# 使用 op 插件登录 1Password
op signin my@email.com

# 使用 op 插件获取名为 "example-item" 的条目的密码
password=$(op get item example-item | jq -r '.details.password')

# 使用获取的密码进行其他操作
echo "The password for example-item is $password"
```

请注意，在上面的示例代码中，我们使用了 jq 工具来解析 op 命令的输出。如果您的系统中没有安装 jq，请先安装它。

在上面的示例代码中，我们使用了 op 插件来获取条目的密码，但是您还可以使用其他的插件来进行其他操作，例如搜索、创建、更新等。请阅读 1Password/shell-plugins 的文档以获取更多信息。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/1Password/shell-plugins 

开源项目作者：1Password

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=1Password/shell-plugins)

