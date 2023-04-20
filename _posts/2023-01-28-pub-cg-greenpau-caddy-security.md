---
layout: post
title: Caddy 安全配置插件，配置更安全的 Web 服务
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 greenpau/caddy-security，该项目在 GitHub 有超过 700 Star。

caddy-security 是一个基于 Caddy Web Server 的安全配置项目。它提供了一组 Caddy 的配置规则，可以帮助您配置更安全的网络服务。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230218205306446.png)

该项目包含了一些安全功能，如:
- HTTP 安全头
- 防止点击劫持
- 防止跨站脚本攻击
- 防止跨站请求伪造
- 限制访问
- 限制爬虫
- 限制目录浏览
- 强制HTTPS
- 等等

使用这个项目可以很容易的配置一个更安全的网站，而不需要任何代码编写。


### 如何安装使用

安装这个项目需要先安装 Caddy server，然后在 Caddy 配置文件中引用这个项目的配置文件。

安装 caddy-security 项目需要以下步骤:

1. 安装 Caddy Web Server，请参考 Caddy 官网的说明。
2. 下载 caddy-security 项目的配置文件。可以通过以下命令下载：
```bash
git clone https://github.com/greenpau/caddy-security.git
```
3. 修改 Caddy 配置文件(Caddyfile)，引用 caddy-security 项目的配置文件。
在 Caddyfile 最前面添加如下代码
```bash
import caddy-security/security.conf
```
4. 重启 Caddy 服务，使配置生效。
```bash
sudo systemctl restart caddy
```


### 使用示例 DEMO

以下是一个使用 caddy-security 项目的 demo 代码示例:

```bash
# Caddyfile

import caddy-security/security.conf

example.com {
    proxy / localhost:8080 {
        header_upstream -X-Real-IP
    }
}
```

上述代码中，我们首先通过 `import` 命令引用了 caddy-security 项目的配置文件。然后我们配置了一个名为 example.com 的站点，并将其代理转发到本地的 8080 端口。通过配置项 `header_upstream -X-Real-IP`, 来清除代理服务器发送的 X-Real-IP 头。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/greenpau/caddy-security 

开源项目作者：greenpau

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=greenpau/caddy-security)



关注我们，一起探索有意思的开源项目。
