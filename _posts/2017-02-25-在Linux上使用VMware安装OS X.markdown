---
layout: default
title:  "在Linux上使用VMware安装OS X"
date:   2017-02-25 22:56
categories: jekyll update
---
![](/image/OS X启动.png)  
![](/image/OS X.png)  
![](/image/OS X关于.png)  
  
  
  
> OS X一直以惊艳的外表，卓越的性能打动着人们。而人们却为价格望而却步，如何无风险地来安装一个稳定且高速的OS X呢？  
  
  
[VMware Player-Hackintosh组合包](/download/WMware-Hackintosh.zip)  
[OS X系统(Google Drive)](https://drive.google.com/open?id=0B-PSijxodhB1YTRRcU1CMEI2OEE)  
  
  
如何安装OS X，今天，我将手把手指导  
1. 安装VMware Player  
- 首先以root身份安装组合包中的bundle文件  
- 为VMware打补丁，以root身份执行以下命令  
```
cd /usr/lib/vmware/modules/source
cp /home/lexuge/下载/vmmon.tar .
cp /home/lexuge/下载/vmmon.tar .
vmware-modconfig --console --install-all
```  
- 安装Mac破解补丁  
解压unlocker压缩包后以root身份执行lnx-install.sh  
至此，VMware安装完成
  
  
2. 下载上面的安装镜像，请有耐心  
  
  
3. 安装OS X  
- 新建一个虚拟机，选择稍后安装系统-OS X-存储虚拟硬盘为单文件  
- 进入虚拟机设置，设置内存尽可能的大，CPU 4核，然后删除现有的虚拟硬盘，并添加一个虚拟硬盘(配置：SATA-然后选择下载的macOS Sierra 10.12 by wikigain.vmdk)  
- 进入虚拟机，开始安装  
  
  
4. 享受一切！  
