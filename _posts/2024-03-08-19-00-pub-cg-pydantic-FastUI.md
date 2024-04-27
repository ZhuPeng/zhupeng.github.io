---
layout: post
title: 快速开发 UI 页面的工具包
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

在前端编程中，我们如何更快地构建更好的用户界面一直是一个重要而复杂的问题。使用 JavaScript（如 React）开发前端应用是常见的选择，然而这需要我们深入学习和理解新的编程语言和工具。此外，前后端开发通常需要复制和粘贴组件到每个视图中，这与开发效率和代码可维护性相悖。

今天要给大家推荐一个 GitHub 开源项目 pydantic/FastUI，该项目在 GitHub 有超过 6.3k Star，一句话介绍该项目：Build better UIs faster.


![](https://raw.githubusercontent.com/pydantic/FastUI/main/screenshot.png)

###### 项目介绍

FastUI 是一个以 Python 代码定义 Web 应用程序用户界面的新方法，允许 Python 开发者使用 React 构建响应式 web 应用，而无需编写一行 JavaScript，或接触 `npm`。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240410220002620.png)

FastUI 主要包括四部分：`fastui` PyPI 包、`@pydantic/fastui` npm 包、`@pydantic/fastui-bootstrap` npm 包和 `@pydantic/fastui-prebuilt` npm 包。在 FastUI 的核心是一套匹配的 Pydantic 模型和 TypeScript 接口，这些接口在构建时由 TypeScript 和 pyright/mypy，在运行时由 Pydantic 进行验证。

###### 如何使用

如何安装和使用 FastUI，可以参见 README 中的详细指南。社区提供了一个完整的 FastAPI 应用示例，该应用使用 FastUI 展示了一些用户配置文件：

```python
from datetime import date

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    dob: date = Field(title='Date of Birth')


# define some users
users = [
    User(id=1, name='John', dob=date(1990, 1, 1)),
    User(id=2, name='Jack', dob=date(1991, 1, 1)),
    User(id=3, name='Jill', dob=date(1992, 1, 1)),
    User(id=4, name='Jane', dob=date(1993, 1, 1)),
]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    """
    Show a table of four users, `/api` is the endpoint the frontend will connect to
    when a user visits `/` to fetch components to render.
    """
    return [
        c.Page(  # Page provides a basic container for components
            components=[
                c.Heading(text='Users', level=2),  # renders `<h2>Users</h2>`
                c.Table(
                    data=users,
                    # define two columns for the table
                    columns=[
                        # the first is the users, name rendered as a link to their profile
                        DisplayLookup(field='name', on_click=GoToEvent(url='/user/{id}/')),
                        # the second is the date of birth, rendered as a date
                        DisplayLookup(field='dob', mode=DisplayMode.date),
                    ],
                ),
            ]
        ),
    ]


@app.get("/api/user/{user_id}/", response_model=FastUI, response_model_exclude_none=True)
def user_profile(user_id: int) -> list[AnyComponent]:
    """
    User profile page, the frontend will fetch this when the user visits `/user/{id}/`.
    """
    try:
        user = next(u for u in users if u.id == user_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="User not found")
    return [
        c.Page(
            components=[
                c.Heading(text=user.name, level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.Details(data=user),
            ]
        ),
    ]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))
```
对应 UI 渲染如下：

![](https://raw.githubusercontent.com/pydantic/FastUI/main/screenshot.png)

###### 项目推介

虽然 FastUI 仍在积极开发中，但它已经提供了一种全新的方式来构建 Web 应用程序用户界面。其使用 Python 作为前端编程语言的独特设计，使得 Python 开发者无需过度依赖 JavaScript 就可以快速构建并展示高质量的 Web 页面。FastUI 以其简单的接口设计、使用方便性和高度可扩展性吸引了许多开发者的关注。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=pydantic/FastUI&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/pydantic/FastUI 

开源项目作者：pydantic

开源协议：

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=pydantic/FastUI)

关注我们，一起探索有意思的开源项目。

