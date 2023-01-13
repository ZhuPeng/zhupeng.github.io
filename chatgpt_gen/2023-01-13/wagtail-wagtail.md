
大家好，又见面了，我是 GitHub 精选君！

今天要给大家推荐一个 GitHub 开源项目 wagtail/wagtail，该项目在 GitHub 有超过 13.9k Star，用一句话介绍该项目就是：“A Django content management system focused on flexibility and user experience”。

![image-20230113223137211](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20230113223137211.png)

Wagtail 是一个由 Torchbox 开发的 Python 内容管理系统 (CMS)。它基于 Django 框架，具有强大的可扩展性和易于使用的编辑界面。Wagtail 还提供了富媒体支持、可视化页面编辑和先进的内容管理功能，适用于各种网站和应用程序。

以下是 Wagtail 的页面展示效果。

![Wagtail screenshot](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_wagtail-screenshot-with-browser.png)

功能比较的多和强大，Wagtail 非常关注用户体验，同时又提供了简洁的控制能力给到设计和开发人员。

![image-20230113222132135](https://raw.githubusercontent.com/ZhuPeng/pic/master/mac/compress_image-20230113222132135.png)


### 如何安装使用

安装和使用方式参考如下动图或代码：

![Installing Wagtail](https://raw.githubusercontent.com/wagtail/wagtail/master/.github/install-animation.gif)

```bash
pip install wagtail
wagtail start mysite
cd mysite
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 使用示例 DEMO

下面是一个使用 Wagtail 创建简单页面的示例。

首先，在 myapp 目录下创建一个文件 `models.py`，并添加以下代码：

```python
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

然后，在 myapp 目录下创建一个文件 `views.py`，并添加以下代码：

```python
from django.shortcuts import render
from wagtail.core.models import Page

def home(request):
    page = Page.objects.get(slug='home')
    return render(request, 'home.html', {
        'page': page,
    })

```

最后，在 myapp 目录下创建一个文件 `templates/home.html`，并添加以下代码：

```html
{% extends 'base.html' %}

{% block content %}
    <h1>{{ page.title }}</h1>
    {{ page.body|richtext }}
{% endblock %}
```

以上就能实现展示页面 Title 和 Body 的能力，是不是挺简单的？

更多项目详情请查看如下链接。

开源项目地址：https://github.com/wagtail/wagtail

开源项目作者：wagtail

