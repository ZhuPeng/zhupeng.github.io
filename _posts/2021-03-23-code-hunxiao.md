---
layout: post
title: 这款工具通过混淆代码防止代码外泄问题，点子很正
tags: Python
---

大家好。

大家应该知道，一般网站上使用的 JavaScript 的代码都做了不同程度的混淆，基本上就算你拿到了源码，也看不懂具体是干什么的，当然执行是没问题的。这种方式一定程度上能够防止代码的泄露，对于 JavaScript 这样的语言，也没有别的好的办法了。

以上问题对于 Python 来说，也是一个难题。虽然开放源码并不是不可以，但是有些代码还是希望能做到保密，所以在软件的分发上，确保代码不被泄露还挺难的。

今天要推荐的一个项目恰巧就能够解决上述问题。

pywhlobf 是一个 Python 代码混淆工具，该工具的输入为 wheel 格式分发包(也就是说，您首先得执行如 `python -m build --wheel` 的命令将项目打成 wheel 包，然后才能使用本工具；而正常的 wheel 包被解压后就能直接看到源码)，输出为混淆后的 wheel 包。包中所有的 `.py` Python 文件将会编译替换为目标平台的 `.so` 文件，从而达到混淆/保护代码的目的。

由于 pywhlobf 是将 .py 文件编译为目标平台的 .so 文件，所以需要目标平台的运行环境才能运行，作者目前提供了多个已经构建好的 Linux 镜像，方便大家直接使用。而对于 MacOS 和 Windows 来说，可以通过 pip 的方式进行安装使用。

![image-20210323230545443](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210323230545443.png)

以下是具体执行混淆命令的执行情况，使用上非常的简单，速度也非常的快。

![image-20210323230628270](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210323230628270.png)

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20210323230641724.png)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/huntzhan/pywhlobf
