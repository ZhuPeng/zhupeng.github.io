说起 git，广大 IT 人士应该都不陌生，无论是公司里用于管理代码的 Gitlab，或者是同性交友平台（划掉）github，我们平时多多少少都会有接触。Git 是一款出色的项目管理软件，来自于天才少年 Linus Torvalds，他在创造出 Linux kernel 之后，开发了 git，用于管理 Linux kernel 的源码。从此以后，越来越多的项目开始使用git作为自己的版本管理工具。

​	github作为全世界最大的交友平台，不止托管了许多优秀的项目源码，还有相当一部分开源的资料可以供我们免费下载，比如：中国科学技术大学计算机学院的课程资源（https://github.com/ustcwpz/USTC-CS-Courses-Resource）

![USTC_git](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)

或者是一些奇奇怪怪的知识（杭州买房攻略：https://github.com/houshanren/hangzhou_house_knowledge）

![hangzhou](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)

你以为github是这样的

![github](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image005.jpg)

但实际上他是这样的

![youtube](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image007.jpg)

或者是这样的

![logo](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image009.jpg)

我们日常工作生活中，涉及到写代码或者是写文之类的工作时，使用 git 可以很方便的管理我们的创作内容，下面给大家简单介绍一下如何在自己家中搭建一个 Gitlab 服务器。

首先，我们要保证 git 服务器的稳定，7*24在线，性能要足够支撑稳定运行，现规划两种方案：路由器和树莓派。因为我家中的路由器性能略差，因此我选择了这款树莓派4b（2G rom版）。作为最新一代树莓派，它继承了树莓派家族便携、开源、接口丰富的特点，并且性能相对于树莓派3b+有较大升级，也是家用服务器的不二之选。

![rapi4_front](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)

（这个角度看树莓派居然有种别样的美感）

接下来介绍树莓派安装gitlab的相关内容：

1、访问gitlab官网（https://packages.gitlab.com/gitlab），获取gitlab-ce包的相关信息。因为gitlab做了树莓派的相关支持，可以直接通过官网wget下载对应版本。这里我使用最新版本12.8.6作为gitlab服务器。

![gitlab_dld](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image012.jpg)

根据右侧的提示，我们可以添加相关远程仓库，并使用 apt-get 包管理工具进行在线下载安装。

在我本地添加完相关仓库地址后，apt-get 还是安装失败，所以我选择直接下载对应 deb 包，由于该包较大，使用 wget 尝试多次后依然失败，建议直接使用某雷下载 download.deb 包进行安装。

installing...

![install](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image014.jpg)

2、安装成功后工作：

安装 deb 包耗时5分钟左右，安装完成后，因为 gitlab 使用的80端口被树莓派自带的 apache 服务占用，所以需要先停止 apache 服务，再进行 gitlab 的部署。

![apache](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image016.jpg)

3、这时，我们就可以运行gitlab-ctl reconfigure命令，来初始化gitlab服务器了。

（约十分钟左右）

提示完成以后，可以通过在局域网内使用树莓派ip+80端口访问 Gitlab 界面，至此，gitlab的安装工作基本完成。 

![gitlab](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image018.jpg)

进入Gitlab管理界面，来创建一个十分 niubility 的项目（捂脸逃 

![niubility](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image020.jpg)

4、现在我们在本地局域网内就能方便的使用git服务了，如果我们想更加愉快地在异地管理自己的项目，接下来给大家介绍一款实用工具：花生壳。

在花生壳开放平台 https://open.oray.com/ 看到了花生壳开放了面向开发者的 phtunnel 嵌入式解决方案。相对于传统的 pc 客户端映射内网服务，对于git服务是个更加合适的选择，于是我将 phtunnel 嵌入了自己的树莓派。 

![sdk](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image022.jpg)

首先登陆开发者平台 https://open.oray.com/ 申请开发者权限，这里不再赘述，申请成功后拿到了属于自己的 APPID 和 APPKEY。

然后就可以去下载树莓派额 sdk 来进行嵌入了，打开压缩包以后看到下列四个包： 

![pkg](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image024.jpg)

虽然我本地的设备是aarch64，但是树莓派官网下载的 Raspbian Buster 安装完成后是32位的，这里我选择了armv8版的包。

按照帮助文档尝试运行，目前比较正常，扫码后使用调试账号登录，提示登录成功，域名状态变为online。 

![qr_code](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image026.jpg)

通过本地管理接口也可以获取到账号信息。 

![rpc](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image028.jpg)

 现在phtunnel的依然是前台运行状态，绑定完账号信息之后，重新启动，加上 -d 参数，使程序后台运行，这次启动后程序会使用之前的配置文件，无需再次绑定，本地管理接口调用也验证了这个猜想。 添加一个到本地80端口的映射，就可以从外网访问到 niubility 项目了。 

![dim_niubility](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image030.jpg)

5、克隆到本地

点击clone后获取地址：http://raspi.git.com/root/niubility_project.git，我们需要把前面的域名改为花生壳的映射域名：http://thedim.qicp.vip/root/niubility_project.git，就可以 git clone 了。 

![ ](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image032.jpg)

 使用git clone命令克隆项目以后，在项目目录下使用 git remote -v 来查看当前克隆的项目路径。此时 git remote -v重的信息已经变成了花生壳映射的地址。后续再继续进行git操作的时候，就不需要单独配置host或者是其他操作了。

修改本地文件并 push：

![commit](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image034.jpg)

6、制作开机启动 这里我们使用 systemd 来守护进程。systemd 即system daemon，是一个系统级的系统与服务管理器。在新版的 Linux 发行版中，代替了systemV，成为更主流的守护方式。

这里我们编写一个简单的phtunnel.service文件，使phtunnel可以进行开机启动，文件内容如下：

```ini
  [Unit] Description=Start phtunnel program
  
  [Service] Type=simple ExecStart=/usr/bin/phtunnel -l /var/log/phtunnel.log -c /etc/phtunnel.json -r -i <填入APPID> -k <填入APPKEY> RemainAfterExit=no Restart=always

  [Install] WantedBy=network-online.target
```

将该service文件放置于 /lib/systemd/system/ 目录下，创建一个service文件，

使用systemctl命令即可管理systemd启动文件。常用的管理命令如下

```bash
  systemctl enable phtunnel #创建一个软连接，将phtunnel.service加入相应的target中，设置开机启动。
 
  systemctl start phtunnel  #启动phtunnel服务。
 
  systemctl status phtunnel  #查看phtunnel服务当前运行状态。
 
  systemctl restart phtunnel #重启phtunnel服务。 
```

至此，我们的“微型·假装有公网ip版·Git服务器”就搭建完成了，又能开心地跟小伙伴们玩（zhuang）耍（bi）了。

花生壳PHTunnel采用C语言实现，最小约80KB，能轻松实现高性能反向代理应用，支持TCP、UDP、HTTP、HTTPS协议，端到端的TLS加密通信，黑白名单防黑验证等；覆盖Windows、Linux、树莓派、Mac、安卓等主流操作系统。

![984x492](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image035.jpg)

作为花生壳内网穿透的核心组件，花生壳PHTunnel可以集成嵌入到各种网络和智能IoT设备中，无需公网IP，只要有网就能轻松穿透各种复杂的路由和防火墙，实现外网访问内网的各种应用。

![场景](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image037.jpg)

后续：我们可以使用 Gitlab + phtunnel 的 docker 镜像来更方便的创建一个 Gitlab 服务（相关镜像：gitlab/gitlab-ce:latest，bestoray/phtunnel:latest），两个镜像均已支持 arm 平台。或者可以将 Gitlab 和 phtunnel 服务打包进一个自己的镜像。现在搭建的git只支持http访问，后续添加https映射的方法需要继续研究。手上的另一台树莓派设备，是树莓派 zero W，相对于树莓派4b要更加小巧，后面会尝试将这部分剩余计算力充分利用起来，搭建一些有趣的个人网站。这部分相关内容，我们下期再详细介绍。

想要了解更多花生壳相关的内容，可以扫码进群，欢迎大家一起来交流。

![image-20200325220542784](说起 git，广大 IT 人士应该都不陌生，无论是公司里用于管理代码的 Gitlab，或者是同性交友平台（划掉）github，我们平时多多少少都会有接触。Git 是一款出色的项目管理软件，来自于天才少年 Linus Torvalds，他在创造出 Linux kernel 之后，开发了 git，用于管理 Linux kernel 的源码。从此以后，越来越多的项目开始使用git作为自己的版本管理工具。

github作为全世界最大的交友平台，不止托管了许多优秀的项目源码，还有相当一部分开源的资料可以供我们免费下载，比如：中国科学技术大学计算机学院的课程资源（https://github.com/ustcwpz/USTC-CS-Courses-Resource）

![USTC_git](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg)

或者是一些奇奇怪怪的知识（杭州买房攻略：https://github.com/houshanren/hangzhou_house_knowledge）

![hangzhou](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.jpg)

你以为github是这样的

![github](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image005.jpg)

但实际上他是这样的

![youtube](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image007.jpg)

或者是这样的

![logo](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image009.jpg)

我们日常工作生活中，涉及到写代码或者是写文之类的工作时，使用 git 可以很方便的管理我们的创作内容，下面给大家简单介绍一下如何在自己家中搭建一个 Gitlab 服务器。

首先，我们要保证 git 服务器的稳定，7*24在线，性能要足够支撑稳定运行，现规划两种方案：路由器和树莓派。因为我家中的路由器性能略差，因此我选择了这款树莓派4b（2G rom版）。作为最新一代树莓派，它继承了树莓派家族便携、开源、接口丰富的特点，并且性能相对于树莓派3b+有较大升级，也是家用服务器的不二之选。

![rapi4_front](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image010.jpg)

（这个角度看树莓派居然有种别样的美感）

接下来介绍树莓派安装gitlab的相关内容：

1、访问gitlab官网（https://packages.gitlab.com/gitlab），获取gitlab-ce包的相关信息。因为gitlab做了树莓派的相关支持，可以直接通过官网wget下载对应版本。这里我使用最新版本12.8.6作为gitlab服务器。

![gitlab_dld](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image012.jpg)

根据右侧的提示，我们可以添加相关远程仓库，并使用 apt-get 包管理工具进行在线下载安装。

在我本地添加完相关仓库地址后，apt-get 还是安装失败，所以我选择直接下载对应 deb 包，由于该包较大，使用 wget 尝试多次后依然失败，建议直接使用某雷下载 download.deb 包进行安装。

installing...

![install](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image014.jpg)

2、安装成功后工作：

安装 deb 包耗时5分钟左右，安装完成后，因为 gitlab 使用的80端口被树莓派自带的 apache 服务占用，所以需要先停止 apache 服务，再进行 gitlab 的部署。

![apache](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image016.jpg)

3、这时，我们就可以运行gitlab-ctl reconfigure命令，来初始化gitlab服务器了。

（约十分钟左右）

提示完成以后，可以通过在局域网内使用树莓派ip+80端口访问 Gitlab 界面，至此，gitlab的安装工作基本完成。 

![gitlab](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image018.jpg)

进入Gitlab管理界面，来创建一个十分 niubility 的项目（捂脸逃 

![niubility](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image020.jpg)

4、现在我们在本地局域网内就能方便的使用git服务了，如果我们想更加愉快地在异地管理自己的项目，接下来给大家介绍一款实用工具：花生壳。

在花生壳开放平台 https://open.oray.com/ 看到了花生壳开放了面向开发者的 phtunnel 嵌入式解决方案。相对于传统的 pc 客户端映射内网服务，对于git服务是个更加合适的选择，于是我将 phtunnel 嵌入了自己的树莓派。 

![sdk](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image022.jpg)

首先登陆开发者平台 https://open.oray.com/ 申请开发者权限，这里不再赘述，申请成功后拿到了属于自己的 APPID 和 APPKEY。

然后就可以去下载树莓派额 sdk 来进行嵌入了，打开压缩包以后看到下列四个包： 

![pkg](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image024.jpg)

虽然我本地的设备是aarch64，但是树莓派官网下载的 Raspbian Buster 安装完成后是32位的，这里我选择了armv8版的包。

按照帮助文档尝试运行，目前比较正常，扫码后使用调试账号登录，提示登录成功，域名状态变为online。 

![qr_code](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image026.jpg)

通过本地管理接口也可以获取到账号信息。 

![rpc](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image028.jpg)

 现在phtunnel的依然是前台运行状态，绑定完账号信息之后，重新启动，加上 -d 参数，使程序后台运行，这次启动后程序会使用之前的配置文件，无需再次绑定，本地管理接口调用也验证了这个猜想。 添加一个到本地80端口的映射，就可以从外网访问到 niubility 项目了。 

![dim_niubility](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image030.jpg)

5、克隆到本地

点击clone后获取地址：http://raspi.git.com/root/niubility_project.git，我们需要把前面的域名改为花生壳的映射域名：http://thedim.qicp.vip/root/niubility_project.git，就可以 git clone 了。 

![clone](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image032.jpg)

 使用git clone命令克隆项目以后，在项目目录下使用 git remote -v 来查看当前克隆的项目路径。此时 git remote -v重的信息已经变成了花生壳映射的地址。后续再继续进行git操作的时候，就不需要单独配置host或者是其他操作了。

修改本地文件并 push：

![commit](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image034.jpg)

6、制作开机启动 这里我们使用 systemd 来守护进程。systemd 即system daemon，是一个系统级的系统与服务管理器。在新版的 Linux 发行版中，代替了systemV，成为更主流的守护方式。

这里我们编写一个简单的phtunnel.service文件，使phtunnel可以进行开机启动，文件内容如下：

```ini
  [Unit] Description=Start phtunnel program
  
  [Service] Type=simple ExecStart=/usr/bin/phtunnel -l /var/log/phtunnel.log -c /etc/phtunnel.json -r -i <填入APPID> -k <填入APPKEY> RemainAfterExit=no Restart=always

  [Install] WantedBy=network-online.target
```

将该service文件放置于 /lib/systemd/system/ 目录下，创建一个service文件，

使用systemctl命令即可管理systemd启动文件。常用的管理命令如下

```bash
  systemctl enable phtunnel #创建一个软连接，将phtunnel.service加入相应的target中，设置开机启动。
 
  systemctl start phtunnel  #启动phtunnel服务。
 
  systemctl status phtunnel  #查看phtunnel服务当前运行状态。
 
  systemctl restart phtunnel #重启phtunnel服务。 
```

至此，我们的“微型·假装有公网ip版·Git服务器”就搭建完成了，又能开心地跟小伙伴们玩（zhuang）耍（bi）了。

花生壳PHTunnel采用C语言实现，最小约80KB，能轻松实现高性能反向代理应用，支持TCP、UDP、HTTP、HTTPS协议，端到端的TLS加密通信，黑白名单防黑验证等；覆盖Windows、Linux、树莓派、Mac、安卓等主流操作系统。

![984x492](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image035.jpg)

作为花生壳内网穿透的核心组件，花生壳PHTunnel可以集成嵌入到各种网络和智能IoT设备中，无需公网IP，只要有网就能轻松穿透各种复杂的路由和防火墙，实现外网访问内网的各种应用。

![场景](file:////Users/zhupeng/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image037.jpg)

后续：我们可以使用 Gitlab + phtunnel 的 docker 镜像来更方便的创建一个 Gitlab 服务（相关镜像：gitlab/gitlab-ce:latest，bestoray/phtunnel:latest），两个镜像均已支持 arm 平台。或者可以将 Gitlab 和 phtunnel 服务打包进一个自己的镜像。现在搭建的git只支持http访问，后续添加https映射的方法需要继续研究。手上的另一台树莓派设备，是树莓派 zero W，相对于树莓派4b要更加小巧，后面会尝试将这部分剩余计算力充分利用起来，搭建一些有趣的个人网站。这部分相关内容，我们下期再详细介绍。

想要了解更多花生壳相关的内容，可以扫码进群，欢迎大家一起来交流。

![image-20200325220542784](/Users/zhupeng/Work/git/zhupeng.github.io/images/image-20200325220542784.png))