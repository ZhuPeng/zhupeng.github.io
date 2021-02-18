---
layout: post
title: 2021 年了，Swift 的 JSON-Model 转换还能有什么新花样
tags: 投稿
---

大家过年好，今天的文章来自于读者的投稿。以下是作者的简介：

> 我叫明林清，是的姓明，不姓林。早期做过前端，后来多数时间做 iOS，现在有 10 年多了 😱😱，这几年在做技术管理，代码写得少了点。现就职于提供音视频直播、点播服务的百家云。

投稿的内容是作者在春节期间、带娃之余、用了几个晚上完成的一个 Swift 版的 JSON-Model 转换工具 [ExCodable](https://github.com/iwill/ExCodable)。以下是该项目相关的内容。

别走！看到前面的介绍大家心里可能想“嗷，又一个轮子”，但是 ExCodable 真的有点不一样：
- 它在 Swift `Codable` 基础上做的扩展；
- 基于 `KeyPath` 实现了 Key-Mapping；
- 差不多实现了 YYModel 所有特性；
- 1 个文件、500 行代码。

我们团队准备开始使用 Swift，第一选择当然是站在上巨人的肩膀。节前开始寻找一些开源框架，比如网络请求用 [Alamofire](https://github.com/Alamofire/Alamofire)、自动布局用 [SnapKit](https://github.com/SnapKit/SnapKit)，毫无悬念。但是 JSON-Model 转换并没有找到一个合适的。

GitHub 上 Star 比较多的有几种类型：
- 刀耕火种型：这种框架用于读写 JSON，至于 Model 是不管的，比如 [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) —— 适用于少量使用、Model 很简单甚至没有的情况。
- 优雅绅士型：Swift 内置的 Codable 是可以满足刚需的，但也有官方框架的通病 —— 繁琐，[Codextended](https://github.com/JohnSundell/Codextended) 对其做了大量的简化，但还是要逐个属性 Encode/Decode —— 适用于 Model 相对简单的场景。
- 八仙过海型：[ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)、[HandyJSON](https://github.com/alibaba/HandyJSON)、[KakaJSON](https://github.com/kakaopensource/KakaJSON) 等各有所长，他们都各自构建了整套的序列化、反序列化机制，略复杂，甚至还有直接读写内存的（“依赖于从 Swift Runtime 源码中推断的内存规则，任何变动我们将随时跟进”），这就有点危险了，至少不够优雅。

调研一番之后倾向于 Codextended，因为能享受到官方的 Codable。起初有考虑直接基于它做扩展来支持 Key-Mapping，但是后来发现受到限制较多，于是重新写了关键部分的实现，有些调整、也有些舍弃。

Codextended 最欠缺的是 Key-Mapping，经过各种摸索、尝试，发现 KeyPath 方式可行。解决掉关键问题后面就简单了，很快实现了 [YYModel](https://github.com/ibireme/YYModel) 支持的所有特性。

主要特性：
- 通过 `KeyPath` 和 `CodingKey` 配置 Key-Mapping；
- 支持多个候选 Key；
- 支持 Key 嵌套；
- 支持自定义 Encode/Decode Handler；
- 支持使用 Subscript 进行 Encode/Decode；
- 支持类型自动转换以及自定义转换；
- 支持多种 Encoder/Decoder，默认使用 JSON；
- 使用类型推断；
- 使用 `Optional` 类型取代抛错误；
- 支持 struct、class、subclass。

示例：

定义 struct；

```swift
struct TestStruct: Equatable {
    private(set) var int: Int = 0
    private(set) var string: String = ""
}
```

实现 `ExCodable`；

```swift
extension TestStruct: ExCodable {
    
    static var keyMapping: [KeyMap<Self>] = [
        KeyMap(\.int, to: "int", "i"),
        KeyMap(\.string, to: "nested.string")
    ]
    
    init(from decoder: Decoder) throws {
        Self.keyMapping.decode(&self, using: decoder)
    }
    func encode(to encoder: Encoder) throws {
        Self.keyMapping.encode(self, using: encoder)
    }
    
}
```

Encode、Decode；

```swift
let test = TestStruct(int: 100, string: "Continue")
let data = test.encoded() as Data? // Model to JSON Data
let copy = data?.decoded() as TestStruct? // JSON Data to Model
XCTAssertEqual(copy, test)
```

更多示例代码参考 GitHub 上的 [Usage](https://github.com/iwill/ExCodable#usage) 以及单元测试代码。

在此，需要感谢 John Sundell 的 [Codextended](https://github.com/JohnSundell/Codextended) 提供的创意；以及 ibireme 的 [YYModel](https://github.com/ibireme/YYModel) 提供的丰富特性，用 Objective-C 时受用了很多年。

开源项目地址：[https://github.com/iwill/ExCodable](https://github.com/iwill/ExCodable)
