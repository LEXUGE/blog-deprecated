---
layout: default
title:  "ArchLinux下安装QQ"
date:   2016-11-06 15:45
categories: jekyll update
---
QQ一直是Linux用户的一个难题  
今天我们就叫大家使用Longene WINE QQ来实现QQ的使用  
[wine QQ deb包下载](http://www.longene.org/download/WineQQ7.8-20151109-Longene.deb)  
下载了deb包后，打开，将data.tar.gz压缩包解压出来，再将data.tar.gz压缩包解压  
完成后得到/opt和/usr目录  
- 把/opt/下的logene 文件夹 移动到系统/opt/下  
- 在把 usr/bin/下的 qq 移动到你的系统 /usr/bin下  

完毕后进行测试：
```
sh /opt/longene/qq/qq.sh
```
帐号密码都能输入，不存在常规wine下安装qq 无法输入的问题，能正常聊天和文件传输，比较稳定！  
  

