---
layout: post
title: GitHub 开源项目 teamhanko/hanko 介绍，A passkey-first approach to authentication that takes you on the journey beyond passwords. For better security, conversion rates, and happier users.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 teamhanko/hanko，该项目在 GitHub 有超过 1.5k Star，用一句话介绍该项目就是：“A passkey-first approach to authentication that takes you on the journey beyond passwords. For better security, conversion rates, and happier users.”。

![](https://user-images.githubusercontent.com/20115649/176922807-fb92327a-15d5-4568-a4e7-78093cea045e.svg?sanitize=true#gh-light-mode-only)


"hanko" 是一个由 Go 编写的开源项目，用于生成和验证 JSON Web Tokens (JWT)。它提供了一个简单的 API ，可以使用多种加密算法（如 HMACSHA256 和 RSA）来签署和验证 JWT。它还支持自定义的 JWT 标头和声明，以及对 JWT 的生命周期进行更细粒度的控制。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=teamhanko/hanko&type=Timeline)

安装需要先安装Go语言，然后执行 `go get github.com/teamhanko/hanko` 即可。 

使用示例如下：

```
package main

import (
    "fmt"
    "time"

    "github.com/teamhanko/hanko"
)

func main() {
    // 创建一个新的JWT
    token, err := hanko.New(hanko.HS256("secret"), map[string]interface{}{
        "sub": "1234567890",
        "name": "John Doe",
        "iat": time.Now().Unix(),
    })
    if err != nil {
        fmt.Println(err)
        return
    }

    // 编码JWT
    encoded, err := token.Encode()
    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println(encoded)

    // 解码JWT
    decoded, err := hanko.Decode(encoded, hanko.HS256("secret"), &hanko.DecodeOptions{
        ValidationOptions: hanko.ValidationOptions{
            Audience:  "example",
            Issuer:    "my-project",
            Subject:   "1234567890",
            NotBefore: time.Now().Add(-time.Minute).Unix(),
            ExpiresAt: time.Now().Add(time.Minute).Unix(),
        },
    })
    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println(decoded.Claims())
}
```

需要注意的是，在实际使用中，请不要将密钥硬编码到代码中，而应该从环境变量或配置文件中读取。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/teamhanko/hanko 

开源项目作者：teamhanko

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=teamhanko/hanko)

