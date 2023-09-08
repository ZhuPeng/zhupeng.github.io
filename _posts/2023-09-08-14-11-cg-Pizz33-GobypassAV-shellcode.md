---
layout: post
title: GitHub 开源项目 Pizz33/GobypassAV-shellcode 介绍，shellcode免杀加载器，使用go实现，免杀bypass火绒、360、核晶、def等主流杀软
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 Pizz33/GobypassAV-shellcode，该项目在 GitHub 有超过 534 Star，用一句话介绍该项目就是：“shellcode免杀加载器，使用go实现，免杀bypass火绒、360、核晶、def等主流杀软”。


![image](https://user-images.githubusercontent.com/88339946/232708666-a8e28b1b-2502-4bbc-91a9-d88e5ff44e9d.png)
![image](https://user-images.githubusercontent.com/88339946/232708833-9709b6c6-59b3-455a-aaa5-e4a92e549c3b.png)
![image](https://user-images.githubusercontent.com/88339946/234937098-ba1f7e9b-0c8e-4455-a84b-46a6ae53159f.png)
![image](https://user-images.githubusercontent.com/88339946/234936629-b80e9b97-8a85-485e-9097-bbf4091a4d39.png)
![image](https://user-images.githubusercontent.com/88339946/234928250-bcf2952f-c345-4241-b33c-73e053b54dd5.png)
![image](https://user-images.githubusercontent.com/88339946/233016193-23d034da-951a-400a-9720-fffa2b21ba81.png)
![image](https://user-images.githubusercontent.com/88339946/234165227-7a26383c-6f8f-484a-8bfb-6d35d2880e59.png)
![image](https://user-images.githubusercontent.com/88339946/234788023-2a9fd53a-2c02-4467-9ef1-6c654106680d.png)









背景介绍：
在网络安全领域，我们经常会遇到各种杀毒软件对于恶意代码的防护问题。这些杀毒软件，如火绒、360、核晶、def等，通过提取特征，对恶意代码进行识别和查杀。然而，这种方法存在一定的局限性，例如，shellcode写在文件里容易被提取特征，而远程加载的方式虽然免杀性和持久性更好，但请求的地址容易被封禁和溯源。这就需要我们寻找一种新的方法，来绕过这些杀毒软件的防护。

项目介绍：
"GobypassAV-shellcode" 是一个 shellcode 免杀加载器，使用 go 语言实现，能够免杀绕过火绒、360、核晶、def等主流杀软。项目的主要设计要点是使用编译参数限制和加密技术，对 shellcode 进行处理，使其能够绕过杀毒软件的特征提取和查杀。此外，项目还提供了远程加载的方法，通过将加密后的字符串放到云端，可以有效地隐匿 C2 地址，提高了免杀性和持久性。

如何使用：
首先，生成 c 的 payload，然后运行 "go run encode.go" 或 "python xor64.py" 对 shellcode 进行加密。加密后的结果填到代码里编译运行 "go build decode.go"。如果需要进行远程加载，可以把加密后的字符串放到云端，把云端地址填到对应位置生成。如果出现缺少依赖的报错，运行 "go mod init & go mod tidy" 拉取即可。

项目推介：
"GobypassAV-shellcode" 是一个活跃的开源项目，对于网络安全领域的研究者和工程师来说，是一个非常有价值的工具。项目的作者是一位经验丰富的开发者，他的项目已经得到了许多知名用户和公司的使用和推荐。此外，项目的 README 中还提供了详细的使用教程和相关资源链接，对于初学者来说，是一个非常好的学习资源。所以，我强烈推荐大家关注和使用这个项目。







以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=Pizz33/GobypassAV-shellcode&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/Pizz33/GobypassAV-shellcode 

开源项目作者：Pizz33

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=Pizz33/GobypassAV-shellcode)

关注我们，一起探索有意思的开源项目。

