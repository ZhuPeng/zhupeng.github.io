还记得之前推荐过的 [一些有趣和诡异的 JavaScript 代码](<https://mp.weixin.qq.com/s?__biz=MzA3MzE4ODY0Mg==&mid=2455984012&idx=1&sn=0857c2c4a4385929cd4d982dfc8da107&chksm=888523c1bff2aad7d7d1733ec6b09e25a3689b80adaba7b1ffc467b832b73fbb49b864ed96d0&token=186311316&lang=zh_CN#rd>) 嘛？

今天要推荐一些有趣且鲜为人知的 Python 特性，随着数据分析、人工智能的使用，Python 的用户和社区也越来越活跃，有的时候，Python 的一些输出结果对于初学者来说似乎并不是那么一目了然。

![](<https://static.geekbang.org/infoq/5c74e151e59dc.png>)

先分享几个给大家压压惊

* Return return everywhere!/到处返回！

```python
def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
```

**Output:**

```python
>>> some_func()
'from_finally'
```



* Half triple-quoted strings/三个引号

```python
>>> print('wtfpython''')
wtfpython
>>> print("wtfpython""")
wtfpython
>>> # 下面的语句会抛出 `SyntaxError` 异常
>>> # print('''wtfpython')
>>> # print("""wtfpython")
```

更多示例请查看如下中、英文仓库。

> 中文版：<https://github.com/leisurelicht/wtfpython-cn>
>
> 英文版：<https://github.com/satwikkansal/wtfpython>