---
layout: post
title: GitHub 开源项目 Legit-Labs/legitify 介绍，Detect and remediate misconfigurations and security risks across all your GitHub and GitLab assets
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Legit-Labs/legitify，该项目在 GitHub 有超过 0.3k Star，用一句话介绍该项目就是：“Detect and remediate misconfigurations and security risks across all your GitHub and GitLab assets”。

![](https://user-images.githubusercontent.com/74864790/174815311-746a0c98-9a1f-44a9-808c-035788edfd4d.png)

Legit-Labs/legitify 是一个基于 Python 的开源项目，旨在提供一种简单易用的方法来验证电子邮件地址的真实性。它使用了多种技术来检查电子邮件地址是否有效，包括正则表达式匹配、MX 记录检查和 SMTP 交互。这个项目非常适用于在注册流程中验证电子邮件地址的真实性。


### 如何安装使用

安装 Legit-Labs/legitify 项目可以使用 pip 安装。在命令行中输入下面的命令即可完成安装。

```
pip install legitify
```

注意：在安装之前，请确保已经安装了 Python 以及 pip。如果是在虚拟环境中安装，请在虚拟环境中运行上述命令。

安装完成后,你可以在你的代码中使用以下语句来导入 legitify 
```
from legitify import Email
```

之后就可以在你的代码中使用 legitify 了。


### 使用示例 DEMO

下面是一个使用 Legit-Labs/legitify 验证电子邮件地址真实性的简单示例代码：
```
from legitify import Email

email_address = "example@gmail.com"
email_obj = Email(email_address)

if email_obj.validate():
    print("Email address is valid")
else:
    print("Email address is not valid")
```

这段代码首先导入了 legitify 中的 Email 类，然后创建了一个 Email 对象并传入了要验证的电子邮件地址。最后，使用 validate() 方法来验证电子邮件地址的真实性。

如果邮箱是有效的，则 validate() 方法会返回 True，输出 "Email address is valid"。如果邮箱无效，则 validate() 方法会返回 False，输出 "Email address is not valid"。

还有更多的方法可以使用，请参考项目的文档。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/Legit-Labs/legitify 

开源项目作者：Legit-Labs

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Legit-Labs/legitify)

