30 秒你可以做什么？有没有一点像灵魂拷问？

可以喝杯水、看看窗外、写一个 bug ?

今天要推荐的是 30秒代码片段学习的系列，有如下好多个，按需取用在碎片时间查看~

- [30 Seconds of JavaScript](https://github.com/30-seconds/30-seconds-of-code)
- [30 Seconds of CSS](https://30-seconds.github.io/30-seconds-of-css/)
- [30 Seconds of Interviews](https://30secondsofinterviews.org/)
- [30 Seconds of React](https://github.com/30-seconds/30-seconds-of-react)
- [30 Seconds of Python](https://github.com/kriadmin/30-seconds-of-python-code) 
- [30 Seconds of PHP](https://github.com/appzcoder/30-seconds-of-php-code)
- [30 Seconds of Kotlin](https://github.com/IvanMwiruki/30-seconds-of-kotlin) 
- [30 Seconds of Knowledge](https://chrome.google.com/webstore/detail/30-seconds-of-knowledge/mmgplondnjekobonklacmemikcnhklla) 



列举几个里面涉及的知识点：

* JavaScript 计算某一日期是一年中的第几天

```javascript
const dayOfYear = date =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```



* Python 的冒泡排序

```python
def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
```



* PHP 的 endsWith

```php
function endsWith($haystack, $needle)
{
    return strrpos($haystack, $needle) === (strlen($haystack) - strlen($needle));
}
```