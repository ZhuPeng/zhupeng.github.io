通过 defer 在测试代码执行完后获取全局的堆栈（runtime.Stack），分析未正常结束的 goroutine，从而达到检测 goroutine 泄露的目标。



Go 里面的 Stack 是什么样的？





如何获取 Go 里面的 Stack？

如何通过 Stack 检测是否存在 Goroutine 泄露？

还有其他方式可以检测 Goroutine 检测嘛？

