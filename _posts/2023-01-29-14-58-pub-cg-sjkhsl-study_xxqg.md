---
layout: post
title: 再也不用为学习强国积分发愁了
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 sjkhsl/study_xxqg，study_xxqg 是一个自动化学习"学习强国"的工具（有一点绕，懂得都懂），以后再也不用为积分发愁了。该项目基于 [playwright-go](https://github.com/mxschmitt/playwright-go) 开发，支持包括*windows*、linux*、*mac。并且该项目提供了针对不同的系统以及不同的启动方式，需要如下方式进行配置使用。

1、Windows

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230416212350085.png)

2、Linux 或 Mac 下载可执行文件运行

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230416212545301.png)

3、docker 或 docker-compose 运行

docker 命令

```bash
docker run --name study_xxqg -d -p 8080:8080 -v /etc/study_xxqg/:/opt/config/  sjkhsl/study_xxqg:latest
```

docker-compose

```bash
wget https://raw.githubusercontent.com/sjkhsl/study_xxqg/main/docker-compose.yml
docker-compose up -d
```

相比使用可执行文件，docker 的方式不需要解决依赖问题。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230416212724146.png)

4、源码运行

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230416212809103.png)

大家可以根据自己的情况，选择合适的运行方式，但是如果会用 docker 我这边也是推荐使用 docker 的。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=sjkhsl/study_xxqg&type=Timeline)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/sjkhsl/study_xxqg 

开源项目作者：sjkhsl

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=sjkhsl/study_xxqg)



关注我们，一起探索有意思的开源项目。
