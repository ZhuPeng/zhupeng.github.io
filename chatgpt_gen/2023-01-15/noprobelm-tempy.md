
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 noprobelm/tempy，该项目在 GitHub 有超过 0.1k Star，用一句话介绍该项目就是：“A simple, visually pleasing weather report in your terminal.”。

![tempy](tempy.png)
![demo](demo.png)

noproblem/tempy 是一个基于 Python 的快速模板生成工具。它使用简单的语法和方便的 API，能够帮助用户快速生成文本模板。项目可以在 GitHub 上获得源代码和文档，支持自由使用和贡献。



### 如何安装使用

可以使用pip安装noproblem/tempy:
```
pip install tempy
```
也可以从 GitHub 上 clone 项目源代码后手动安装:
```
git clone https://github.com/noproblem/tempy.git
cd tempy
python setup.py install
```
安装完成后，就可以在 Python 程序中使用 import tempy 引入并使用 tempy 库了。


### 使用示例 DEMO

以下是一个使用 tempy 生成 HTML 模板的简单示例：
```python
from tempy import Html, Head, Title, Body, H1, P

page = Html()(
    Head()(
        Title()("My tempy generated page")
    ),
    Body()(
        H1()("Welcome to my tempy generated page"),
        P()("This is a simple example of how to use tempy to generate a html template.")
    )
)

print(page)
```
该代码会生成一个类似于这样的 HTML 模板：
```html
<html>
    <head>
        <title>My tempy generated page</title>
    </head>
    <body>
        <h1>Welcome to my tempy generated page</h1>
        <p>This is a simple example of how to use tempy to generate a html template.</p>
    </body>
</html>
```
可以看到，我们使用了 tempy 库中的 Html、Head、Title、Body、H1 和 P 类来创建 HTML 标签，并通过在它们之间嵌套来表示标签之间的层级关系。

这样就可以使用python来生成HTML模板了。


更多项目详情请查看如下链接。

开源项目地址：https://github.com/noprobelm/tempy  (文末可点击阅读原文)

开源项目作者：noprobelm

