---
layout: post
title: 现代化 PHP 应用服务器
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

PHP 是一种广泛应用的开源通用脚本语言，尤其适用于 Web 开发并可嵌入 HTML 中，但是创建和管理 PHP 应用程序服务器可能会非常复杂却又极其重要。尽管有其他一些已有的解决方案可以尽力简化这个过程，但事实并非如此，因为它们往往缺乏完整的功能，例如对 HTTP/2 和 HTTP/3 的支持，以及真正实现自动化 HTTPS 管理等。这就是你需要 FrankenPHP 的原因。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240822225901588.png)

开源项目 FrankenPHP 在 GitHub 有超过 6.6k Star，用一句话介绍该项目就是：“The modern PHP app server”。

![](https://dunglas.dev/wp-content/uploads/2022/10/frankenphp.png)

###### 项目介绍

FrankenPHP 是一款在 [Caddy](https://caddyserver.com/) Web 服务器基础之上构建的现代 PHP 应用服务器。它可以给你的 PHP 应用带来很多牛逼的能力，主要提供了以下几个功能特点：早期提示(Early Hints)，工作模式，实时功能，自动 HTTPS，以及支持 HTTP/2，HTTP/3 等。FrankenPHP 兼容任何 PHP 应用，通过提供的工作模式与 Symfony 集成，使你的 Symfony 项目速度飞快（将支持 Laravel Octane）。它还可以作为一个独立的 Go 库用于在使用 `net/http` 的任何应用中嵌入 PHP。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113211919656.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113212209394.png)

###### 如何使用

如果你既想要快速启动，又喜欢使用 Docker，可以输入一下代码：

```bash
docker run -v $PWD:/app/public \
    -p 80:80 -p 443:443 \
    dunglas/frankenphp
```
然后直接访问 `http://localhost` 即可。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113211944229.png)

若你不想使用 Docker，我们为 Linux 和 macOS 提供了包含 [PHP 8.3](https://www.php.net/releases/8.3/en.php) 和大多数常用 PHP 扩展的 FrankenPHP 二进制文件，在 GitHub 的 Release 页面即可下载。

在服务当前的目录，运行：
```console
./frankenphp php-server
```
你还可以使用下面的方法运行命令行脚本：
```console
./frankenphp php-cli /path/to/your/script.php
```

###### 项目推介

FrankenPHP 是一款非常有潜力与价值的开源项目，且原生支持很多平台，包括如 WordPress, Drupal, Joomla 等。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240113212311981.png)


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=dunglas/frankenphp&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/dunglas/frankenphp 

开源项目作者：dunglas

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=dunglas/frankenphp)

关注我们，一起探索有意思的开源项目。

