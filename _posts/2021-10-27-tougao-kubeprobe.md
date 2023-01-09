**可选标题：**

- 又一神器开源了｜大规模kubernetes集群诊断利器
- 一文读懂，最新开源的 KubeProber 诊断工具

- 一款刚开源的大规模kubernetes集群诊断利器，好用到爆！
- 带你沉浸式体验面对大规模Kubernetes集群我们是如何巡检的     我想用这个

- 带你深度体验kubeprober -- 开源大规模kubernetes集群诊断工具

**确认标题：**用更云原生的方式做诊断 ｜大规模kubernetes集群诊断利器深度解析

**正文如下：**

**talk is cheap, show me the demo**

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/clip_image001.gif)

**背景**

我们基于Erda (https://www.erda.cloud/)（现已[开源](https://github.com/erda-project/erda)）管理了有相当规模数量的Kubernetes集群，集群的稳定性决定了的服务质量以及对外口碑，很长一段时间我们在这件事情上都显得很被动，经常会出现 Erda 支持同学或者客户将问题反馈到说有业务出现了问题，需要我们协助查询一下是不是平台导致的，然后我们上去一顿操作最后解决问题，答复客户，看似专业且厉害，急用户之所急，实则无章无法，一地鸡毛。

通常我们依赖监控系统来提前发现问题，但是监控数据作为一个正向链路，很难覆盖到所有场景，经常会有因为集群配置的不一致性或者一些更底层资源的异常，即使监控数据完全正常，但是整个系统依然会有一些功能不可用，对此我们做了一套巡检系统，针对系统中一些薄弱点以及一致性做诊断，但是这套系统的扩展性不是很好，对集群跟巡检项的管理也相对粗暴了一点。

最后我们决定做一个更加云原生的诊断工具，使用operator来实现集群跟诊断项的管理，抽象出集群跟诊断项的资源概念，来解决大规模kubernetes集群的诊断问题，通过在中心来下发诊断项到其他集群，并统一收集其他集群的诊断结果来实现任何时刻都可以从中心获取到其他所有集群的运行状态，做到对大规模kubernetes集群的有效管理以及诊断。

**Kubeprober**

**项目介绍**

项目地址： https://github.com/erda-project/kubeprober

官网地址： [https://k.erda.cloud]( https:/k.erda.cloud)

KubeProber 是一个针对大规模 Kubernetes 集群设计的诊断工具，用于在 kubernetes 集群中执行诊断项以证明集群的各项功能是否正常，KubeProber 有如下特点：

- **支持大规模集群** 支持多集群管理，支持在管理端配置集群跟诊断项的关系以及统一查看所有集群的诊断结果；
- **云原生** 核心逻辑采用 [operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 来实现，提供完整的Kubernetes API兼容性;

- **可扩展** 支持用户自定义巡检项。

其核心架构如下：

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_clip_image002.png)

区别于监控系统，kubeProber 从巡检的角度来证明集群的各项功能是否正常，监控作为正向链路，无法覆盖系统的中的所有场景，系统中各个环境的监控数据都正常，也不能保证系统是 100% 可以用的，因此需要一个工具从反向来证明系统的可用性，根本上做到先于用户发现集群中不可用的点，比如：

- 集中的所有节点是否均可以被调度，有没有特殊的污点存在等；
- pod是否可以正常的创建，销毁，验证从 kubernetes，kubelet 到 docker 的整条链路；

- 创建一个service，并测试连通性，验证 kube-proxy 的链路是否正常；

- 访问一个 ingress 域名，验证集群中的 ingress 组件是否正常工作；

- 对 Etcd 执行 put/get/delete 等操作，用于验证 Etcd 是否正常运行；

- ... 更多

**组件介绍**

Kubeprober整体采用Operator来实现核心逻辑，集群之间的管理使用 [remotedialer](https://github.com/rancher/remotedialer) 来维持被纳管集群跟管理集群之间的心跳链接，被纳管集群通过RBAC赋予probe-agent最小所需权限并且通过心跳链接实时上报被纳管集群元信息以及访问apiserver的token，实现在管理集群可以对被管理集群的相关资源进行操作的功能。

**probe-master**

运行在管理集群上的 operator，这个 operator 维护两个 CRD，一个是 Cluster，用于管理被纳管的集群，另一个是 Probe，用于管理内置的以及用户自己便编写的诊断项，probe-master 通过 watch 这两个 CRD，将最新的诊断配置推送到被纳管的集群，同时 probe-master 提供接口用于查看被纳管集群的诊断结果。

**probe-agent**

运行在被纳管集群上的 operator，这个 operator 维护两个 CRD，一个是跟 probe-master 完全一致的 Probe，probe-agent 按照 probe 的定义去执行该集群的诊断项，另一个是 ProbeStatus，用于记录每个 Probe 的诊断结果，用户可以在被纳管的集群中通过kubectl get probestatus 来查看本集群的诊断结果。

**什么是Probe**

kubeprobe中运行的诊断计划我们称之为Probe，一个Probe为一个诊断项的集合，我们建议将统一场景下的诊断项作为一个Probe来运行，probe-agent组件会watch probe资源，执行Probe中定义的诊断项，并且将结果写在 ProbeStatus的资源中。

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_clip_image003.png)

我们期望有一个输出可以清晰的看到当前集群的运行状态，因此我们建议所有的Probe都尽可能数属于应用，中间件，Kubernets，基础设置这四大场景，这样我们可以再展示状态的时候清楚的自上而下的查看究竟是系统中的哪个层面引起的问题。

目前的Probe还比较少，我们还在继续完善，也希望跟大家一起共建。[自定义Probe](https://github.com/erda-project/kubeprober/blob/master/probers/README.md)

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_clip_image004.png)

**对比其他诊断工具**

目前社区已经有kuberhealthy以及kubeeye来做kubernetes集群诊断这件事情。

kuberheathy提供一套比较清晰的框架可以让你轻松编写自己的诊断项，将诊断项CRD化，可以轻松的使用kubernetes的方式来对单个kubernetes进行体检。

kubeeye同样是针对单个集群，主要通过调用kubernetes 的 event api 以及 Node-Problem-Detector 来检测集群控制平面以及各种节点问题，同时也支持自定义诊断项。

kubeprober 做的也是诊断 kubernetes 集群这件事情，提供框架来编写自己的诊断项，除此之外，kubeprober 主要解决了大规模kubernetes 集群的诊断问题，通过中心化的思路，将集群跟诊断项抽象成CRD，可以实现在中心 kubernetes 集群管理其他kubernetes 诊断项配置，诊断结果收集，未来也会解决大规模 kubernetes 集群的运维问题。

|                      | kuberhealthy | kubeeye                               | kubeprober                                |
| -------------------- | ------------ | ------------------------------------- | ----------------------------------------- |
| 开发团队             | kuberhealthy | kubesphere                            | erda                                      |
| 开发语言             | GoLang       | GoLang                                | GoLang                                    |
| 诊断范围             | k8s集成测试  | k8s控制面功能，节点异常检测，yaml规范 | k8s核心链路，节点异常事件，中间件状态等。 |
| 自定义诊断项         | 支持         | 支持基于npd的自定义检查规则           | 支持                                      |
| 命令行工具           | kubectl      | ke                                    | kubectl + plugin                          |
| 多集群支持           | 不支持       | 不支持                                | 支持                                      |
| 支持手动触发诊断任务 | 支持         | 不支持                                | 支持                                      |
| 告警                 | 不支持       | 不支持                                | 支持                                      |
| 可视化               | 不支持       | 不支持                                | 支持                                      |

**如何使用**

kubeprober主要解决大规模kubernetes集群的诊断问题，通常我们选择其中一个集群作为master集群，部署probe-master，其他集群作为被纳管集群，部署probe-agent。更详细的使用步骤可以查看 GitHub 开源仓库。



单集群使用kubeprober

同时kubeprober也可以用于单集群的诊断，适用于没有那么多kubernetes集群需要诊断的场景，具体的使用方法参考[这里](https://docs.erda.cloud/1.3/manual/eco-tools/kubeprober/best-practices/standalone_kubeprober.html)。

**可视化**

kubeprober在多集群中根据probe的策略执行诊断项，会产生大量的诊断事件，那对这些诊断项进行可视化的展示就显得尤为重要，可以有一个全局的dashborad对大规模集群的海量诊断项进行统一的查看分析会更有利于我们掌握这些集群的运行状态。

kubeprober支持将诊断项事件写入 infuxdb，通过grafana来配置图表来统一展示诊断结果，比如我们将 ERROR 事件统一展示出来作为最高优先级进行关注。

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_clip_image011.png)

同时我们也可以通过扩展probe-agent上报的集群信息来展示一张详尽的集群列表

![img](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_clip_image012.png)



**欢迎参与**

当前kubeprobe已经发布了第一个版本0.1.0，还有许多功能不太完善，probe-master的管理能力还可以进一步的被放大挖掘，probe的编写也需要更加的简单易用，我们希望跟社区一期共建，通过打造一个大规模Kubernetes集群的管理神器。

[Contributing to KubeProber](https://github.com/erda-project/kubeprober/blob/master/CONTRIBUTING.md)
