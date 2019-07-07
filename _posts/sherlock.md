# 神探夏洛克

《神探夏洛克》相信大家都看过，我们的生活肯定不会经历离奇市民自杀案件、黑帮走私事件和倒计时炸弹杀人案。我们无非就是写的 bug 造成的损失又大有小，没必要用侦探的方式来调查我们吧。

![](<https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png>)

今天推荐的工具名是 **sherlock**，它是用来查找各个社交网站中某一个用户名是否被注册过，支持了 140 个网站的用户名查找（虽然绝大部分都是需要翻墙的😅）。

![](<https://raw.githubusercontent.com/sherlock-project/sherlock/3276e973274d913368b20550ec2c9aecc38d47f2/screenshot/preview.gif>)

社交网络是一个很有意思的地方，社交网络中的你，可能是你真实生活的延伸，也可能是与你有着天壤之别的另一个你。你有没有曾经偷偷的查看过其他人的社交账号，从中发现了很多的秘密，觉得自己像极了一个侦探🕵？反正我有过~



安装和使用方法：

```bash
# NOTE: Python 3.6 or higher is required.
$ git clone https://github.com/sherlock-project/sherlock.git

# change the working directory to sherlock
$ cd sherlock

# install python3 and python3-pip if not exist

# install the requirements
$ pip3 install -r requirements.txt

$ python3 sherlock.py user123
```



> 项目地址：<https://github.com/sherlock-project/sherlock>