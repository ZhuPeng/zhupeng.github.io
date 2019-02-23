# Python 之禅和设计模式

Python 以其语法简单和易用而备受青睐，近年来随着 Python 在数据分析、机器学习等领域的使用而引起大家的广泛关注。

今天首先要跟大家分享一下 Python 之禅，介绍了 Python 的设计哲学和编程原则。

在 Python 的交互式解释器里面输入命令 `import this` 就会显示 Python 之禅。

> \> \> \> import this
> The Zen of Python, by Tim Peters
>
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!

上述观点对于我们的日常编程很有指导意义，比如简单胜过复杂、代码可读性很重要、错误不应该被直接忽略等。就不一一翻译了，毕竟禅是需要不断去实践、修行才能悟出其中的道理。

为了让大家更好的去体会 Python 的魅力，今天要跟大家的推荐的是「Python Patterns」，该项目收集了 Python 中常用的设计模式和 Pythonic 风格的代码样例，包括单例模式、工厂模式、装饰器等，不管你是在学习或者使用 Python，这个项目都是很值得学习的。

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub精选/ZenOfPython/patterns.1.png)

![](https://7465-test-3c9b5e-1258459492.tcb.qcloud.la/GitHub精选/ZenOfPython/patterns.2.png)

项目地址：https://github.com/faif/python-patterns

接下来简单介绍一下小编在使用 Python 装饰器的一些经验。在 Python 里面一切都是对象，其中函数可以被当成参数传递给另外一个函数，通常可以用来在函数执行的前后做一些事情，例如统计函数执行耗时、增加日志、缓存函数结果等

```python
def foo():
    print 'foo'
    
def deco(f):
    # do something
    foo()
    # do something
    
deco(foo)
```

上述是比较直接的实现方式，没有体现 Python 语法的优雅，如下是更 Pythonic 的写法。

```python
def deco(f):
    def wrapper(*args, **kws):
        print 'before run function:', f.__name__
        f(*args, **kws)
        print 'post run function:', f.__name__
    return wrapper

@deco
def foo():
    print 'foo'
    
foo()
# Output:
# before run function: foo
# foo
# post run function: foo
```

其中 `@deco` 等同于 `foo = deco(foo)`。