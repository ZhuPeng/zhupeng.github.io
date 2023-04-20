---
layout: post
title: 一款云环境利用框架，支持快速的命令行云资源访问
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 teamssix/cf，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“Cloud Exploitation Framework 云环境利用框架，方便安全人员在获得 AK 的后续工作”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230302230617604.png)

![](https://api.star-history.com/svg?repos=teamssix/cf&type=Timeline)



CF 是一个云环境利用框架，适用于在红队场景中对云上内网进行横向、SRC 场景中对 Access Key 即访问凭证的影响程度进行判定、企业场景中对自己的云上资产进行自检等等。以下是目前已支持的云：

![image-20230302230220076](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230302230220076.png)


### 如何安装使用

需要在 GitHub 的 release 页面下载对应的压缩文件，目前支持 MacOS、Linux、Windows 系统。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230302230305239.png)


### 使用示例 DEMO

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230302230442819.png)

执行 cf 命令即可看到项目的介绍，以及目前支持的命令。以下以阿里云作为示例进行介绍。

1、一键接管控制台

```bash
cf alibaba console
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230302230821347.png)

2、一键列出当前访问凭证的云服务资源

```bash
cf alibaba ls
```

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20230302230848671.png)

以下是目前项目支持的命令的最全现状描述：

![](https://cdn.jsdelivr.net/gh/teamssix/BlogImages/imgs/202212132148217.png)


更多项目详情请查看如下链接。

开源项目地址：https://github.com/teamssix/cf 

开源项目作者：teamssix

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=teamssix/cf)



关注我们，一起探索有意思的开源项目。
