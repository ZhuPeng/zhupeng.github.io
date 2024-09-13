---
layout: post
title: GitHub 开源项目 golang-migrate/migrate 介绍，Database migrations. CLI and Golang library.
tags: Go
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

今天要给大家推荐一个 GitHub 开源项目 golang-migrate/migrate，该项目在 GitHub 有超过 14.9k Star。

![](https://stats.deeptrain.net/repo/golang-migrate/migrate/?theme=light)

一句话介绍该项目：Database migrations. CLI and Golang library.





###### 项目介绍

背景介绍：在现代软件开发中，数据库的变更与版本管理是一个不可忽视的问题。随着业务的发展，数据库架构需要不断地演化来满足新的业务需求。这个过程中，如何保证数据库变更的一致性、安全性以及可追溯性，成为了项目团队面临的重大挑战。传统的手动执行 SQL 脚本的方式不仅耗时耗力，还极易出错，尤其是在多环境、大团队的情况下。因此，一个自动化、可靠的数据库迁移工具就显得尤为重要。



![](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_tmp-36e1a5f5fd311e07e00bd59f719eab8d.png)

项目介绍：`migrate` 是一个用 Go 编写的数据库迁移工具，可作为命令行工具或者 Go 语言库使用。它支持从多种来源读取迁移脚本，包括本地文件系统、GitHub、AWS S3 等，并能将这些迁移应用到各种类型的数据库上，如 PostgreSQL、MySQL、SQLite、MongoDB 等。`migrate` 项目的设计理念注重简洁性和健壮性，它不会尝试去纠正用户输入的错误，遇到疑问时选择失败退出，保持了数据库驱动的轻量级，并通过粘合所有部分确保逻辑的严密性。这种设计使得 `migrate` 不仅功能强大，而且非常灵活，适用于各种复杂的数据库迁移需求。

如何使用：
1. 通过 Docker 使用（需安装 Docker）:
```bash
docker run -v {{ migration dir }}:/migrations --network host migrate/migrate -path=/migrations/ -database postgres://localhost:5432/database up 2
```
2. 在 Go 项目中使用:
```go
import (
    "github.com/golang-migrate/migrate/v4"
    _ "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/github"
)

func main() {
    m, err := migrate.New(
        "github://mattes:personal-access-token@mattes/migrate_test",
        "postgres://localhost:5432/database?sslmode=enable")
    if err != nil {
        // 处理异常
    }
    m.Steps(2)
}
```

项目推介：`migrate` 已经被众多知名公司和开源项目所采用，凭借其强大的功能和灵活的设计赢得了不少用户的青睐。它的 GitHub 仓库目前拥有超过 7k 的星标，从社区的反馈和贡献者数量来看，`migrate` 项目维护活跃，社区活力充沛。此外，`migrate` 支持丰富的数据库和迁移源，无论是传统企业还是新兴的互联网公司，都能在项目开发中从 `migrate` 中受益。最重要的是，`migrate` 项目的文档齐全，使用方式简单明了，即使是初学者也能快速上手。因此，无论你是开发人员、DBA 还是项目经理，`migrate` 都是解决数据库迁移问题的优秀选择。

以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=golang-migrate/migrate&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/golang-migrate/migrate 

开源项目作者：golang-migrate

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=golang-migrate/migrate)

关注我们，一起探索有意思的开源项目。

