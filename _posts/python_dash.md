# Python 数据可视化 - Dash

Python 以其语法简单和易用而备受青睐，近年来随着 Python 在数据分析、机器学习等领域的使用而引起大家的广泛关注。使用 Python 我们可以很容易的编写一个爬虫从互联网上获取很多数据，但是如果需要将数据进行可视化就要复杂一些了。

Dash 是建立数据分析性应用的 Python 框架，使用它不要你直接使用 JavaScript。基于 Plotly.js、React 和 Flask，Dash 可以直接结合你的数据分析代码，构建酷炫的 UI Web 应用。



![](https://user-images.githubusercontent.com/1280389/30086128-9bb4a28e-9267-11e7-8fe4-bbac7d53f2b0.gif)



如上是只有 43 Python 代码构建的应用，通过 Pandas 加载 Google Finance 的数据，并使用 Dash 进行可视化。

```python
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value,
        'google',
        dt(2017, 1, 1),
        dt.now()
    )
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()
```



![](https://user-images.githubusercontent.com/1280389/30086123-97c58bde-9267-11e7-98a0-7f626de5199a.gif)



Dash 应用的代码是基于前端交互的响应式的风格，这使得我们可以很容易构建交互式的复杂应用。上图中的应用只有 160 行 Python 代码，是不是很简单？

> 项目地址：https://github.com/plotly/dash

***

