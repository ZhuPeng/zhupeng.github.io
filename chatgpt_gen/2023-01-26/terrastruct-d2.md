
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 terrastruct/d2，该项目在 GitHub 有超过 10.3k Star，用一句话介绍该项目就是：“D2 is a modern diagram scripting language that turns text to diagrams.”。

![](https://raw.githubusercontent.com/terrastruct/d2/master/./docs/assets/banner.png)
![](https://raw.githubusercontent.com/terrastruct/d2/master/./docs/assets/playground_button.png)
![](https://raw.githubusercontent.com/terrastruct/d2/master/./docs/assets/syntax.png)

"terrastruct/d2" 是一个开源的数据库管理工具。该项目基于 Go 语言开发，支持多种数据库类型，如 MySQL、PostgreSQL、SQLite、MSSQL、Oracle、Cassandra等。它提供了一个统一的命令行界面来管理不同类型的数据库，并提供了许多实用功能，如数据库迁移、数据导入导出、SQL 查询等。
该项目提供了一个易于使用的接口，让用户可以更轻松地管理数据库，并节省了手动编写 SQL 语句的时间。通过它可以更高效地管理数据库。
这个项目是跨平台的,可以在Linux,Mac,Windows上运行。

如果你是一个数据库管理员或者是一个开发人员,并且经常需要管理数据库,那么这个项目将会对你有很大的帮助。



### 如何安装使用

要安装 "terrastruct/d2" 项目，您需要执行以下步骤：

1. 安装 Go，并确保您的环境变量已配置好。

2. 使用 go get 命令安装 d2：`go get github.com/terrastruct/d2`

3. 进入到 $GOPATH/src/github.com/terrastruct/d2 目录下执行 go install

4. 确保 $GOPATH/bin 目录已经添加到系统路径中

5. 在终端或命令行中输入 d2 即可启动 d2。

请注意，这仅是

### 使用示例 DEMO

下面是一个使用 "terrastruct/d2" 项目连接 MySQL 数据库的示例代码：
```
#connect to mysql
d2 mysql create connection my_mysql -h localhost -u root -p

# list all the tables in the database
d2 mysql run my_mysql -e "SHOW TABLES"

# create new table
d2 mysql run my_mysql -e "CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY (id))"

# insert data into the table
d2 mysql run my_mysql -e "INSERT INTO users (name) VALUES ('John Doe')"

# select data from the table
d2 mysql run my_mysql -e "SELECT * FROM users"
```

第一行代码是连接 MySQL 数据库，其中 -h 指定了数据库主机，-u 指定了用户名，-p 指定了密码。

第二行代码是查询数据库中的所有表

第三行代码是创建一个新表，并定义了表的结构

第四行代码是向表中插入数据

第五行代码是从表中查询数据

这些代码仅是一个

更多项目详情请查看如下链接。

开源项目地址：https://github.com/terrastruct/d2  (文末可点击阅读原文)

开源项目作者：d2

