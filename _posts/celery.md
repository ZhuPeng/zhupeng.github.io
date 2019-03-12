# Celery

Celery 是一个异步任务队列，它是用 Python 编写非常简单、灵活、可靠，我们可以使用它快速的构建用来处理大量信息的分布式系统。Celery 是语言无关的，但他提供了其他常见语言的接口支持。如果你的项目使用 Python 进行开发那么使用 Celery 就自然而然。

https://github.com/celery/celery 代码或者图片

***
OK，接下来就正式进入正题
使用 Python 开发 Web 应用，在服务 QPS 不断增长过程中，需要不断的关注性能问题并优化，似乎没有尽头。而出身名门 Go 语言，最大的卖点在于它的性能，无论在运行还是编译时它都有突出的性能优势。通过 Go 重写 Python 核心 API 的逻辑能够达到几十倍甚至几百倍的性能提升。


如果你恰巧使用 Python 在开发，同时项目里面使用了 Celery，又由于核心 API 的性能不足持续不断在优化。不妨尝试使用 Golang 重构，相信会有质的飞跃。那么 gocelery 就是你需要的，你可以在 Go 代码提交任务，在 Python 的 Celery Worker 执行，当然你也可以单独作为 Go 版的任务队列使用。

https://github.com/gocelery/gocelery