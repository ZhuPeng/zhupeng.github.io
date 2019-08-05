## runtime

包含 go 里面原生支持的类型，如 chan

* chan

详细介绍：<https://draveness.me/golang/concurrency/golang-channel.html>

```go
// 跳过 buf 直接发送给 receiver
if sg := c.recvq.dequeue(); sg != nil {
		// Found a waiting receiver. We pass the value we want to send
		// directly to the receiver, bypassing the channel buffer (if any).
		send(c, sg, ep, func() { unlock(&c.lock) }, 3)
		return true
}
```

buf => 循环数组


* defer 

* mutex 饥饿模式

竞争模式转化为队列排队模式，防止部分 goroutine 一直争抢不到锁(或者时间较长)

自旋（Spinnig）其实是在多线程同步的过程中使用的一种机制，自旋的优点是避免了 Goroutine 的切换。

* golang gc
* WaitGroup：Add 和 Wait 互相等待和唤醒，Add 之后为 0 唤醒 Wait G；count 不为 0 休眠 Wait G

等待 main 程序退出除了用 WaitGroup 还可以使用 Channel 监听命令行退出信号

```go
type WaitGroup struct {
    noCopy noCopy  // noCopy 的主要作用就是保证 WaitGroup 不会被开发者通过再赋值的方式进行拷贝
                   // checker copyChecker 运行期间的 copy 检查，Cond 有该属性，发生了则 panic
    state1 [3]uint32
}


wg := &sync.WaitGroup{}   
count := 10
wg.Add(count)
for i:=0; i<10; i++ {
  go func() {
    defer wg.Done()   // exec 10 times
  }
}
wg.Wait()  // Wait 10 times Done


ch := make(chan os.Signal, 1)
signal.Notify(ch, os.Interrupt)
<-ch
```

* Cond: Broadcast 广播唤醒所有 G / Signal 唤醒队列最前的 G  (goready/gopark 唤醒/阻塞)

* ErrGroup：收集多个 G 执行的错误

* Semaphore：信号量，用来控制资源的使用

* SingleFlight: 控制相同时间对下游的重复请求(redis 热点缓存失效)

  