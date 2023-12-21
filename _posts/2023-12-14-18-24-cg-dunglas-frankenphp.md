---
layout: post
title: GitHub 开源项目 dunglas/frankenphp 介绍，The modern PHP app server
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 dunglas/frankenphp，该项目在 GitHub 有超过 4.3k Star，用一句话介绍该项目就是：“The modern PHP app server”。


![](https://raw.githubusercontent.com/dunglas/frankenphp/master/frankenphp.png)
![](https://dunglas.dev/wp-content/uploads/2022/10/frankenphp.png)



背景介绍：
在职业开发中，我们经常会碰到服务器配置环节带来的麻烦。PHP（Hypertext Preprocessor）是一种广泛应用的开源通用脚本语言，尤其适用于 Web 开发并可嵌入 HTML 中，但是创建和管理 PHP 应用程序服务器可能会非常复杂却又极其重要。尽管有其他一些已有的解决方案可以尽力简化这个过程，但事实并非如此，因为它们往往缺乏完整的功能，例如对 HTTP/2 和 HTTP/3 的支持，以及真正实现自动化 HTTPS 管理等。这就是你需要 FrankenPHP 的原因。

项目介绍：
FrankenPHP 是一款在 [Caddy](https://caddyserver.com/) web 服务器基础之上构建的现代 PHP 应用服务器。它可以给你的 PHP 应用带来超能力，主要提供了以下几个功能特点：“早期提示(Early Hints)”，工作模式，实时功能，自动 HTTPS，以及支持 HTTP/2，HTTP/3 等。FrankenPHP 兼容任何 PHP 应用，通过提供的工作模式与 Symfony 集成，使你的 Symfony 项目速度飞快（将支持 Laravel Octane）。它还可以作为一个独立的 Go 库用于在使用 `net/http` 的任何应用中嵌入 PHP。

如何使用：
如果你既想要快速启动，又喜欢使用 Docker，可以输入一下代码：
```console
docker run -v $PWD:/app/public \
    -p 80:80 -p 443:443 \
    dunglas/frankenphp
```
然后直接访问 `http://localhost` 即可。

若你不想使用 Docker，我们为 Linux 和 macOS 提供了包含 [PHP 8.3](https://www.php.net/releases/8.3/en.php) 和大多数常用 PHP 扩展的 FrankenPHP 二进制文件：[FrankenPHP 下载](https://github.com/dunglas/frankenphp/releases)。

为了服务当前的目录，运行：
```console
./frankenphp php-server
```
你还可以使用下面的方法运行命令行脚本：
```console
./frankenphp php-cli /path/to/your/script.php
```

项目推介：
FrankenPHP 是一款非常有潜力与价值的开源项目，作者 dunglas 是一名知名的开发者，项目开发活跃，有一个活跃的社区，并有许多知名客户在使用，包括一些知名的 CMS 平台如 WordPress, Drupal, Joomla。因为它的强大功能和简单的使用方式，它正在被更多的开发者认识和使用，如果你正在寻找一个现代、强大且易用的 PHP 应用服务，那么 FrankenPHP 会是你的首选。快来加入我们吧，FrankenPHP 正等待着你的参与和贡献。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dunglas/frankenphp&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dunglas/frankenphp 

开源项目作者：dunglas

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dunglas/frankenphp)

关注我们，一起探索有意思的开源项目。

