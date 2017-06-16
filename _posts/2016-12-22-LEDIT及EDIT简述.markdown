---
layout: default
title:  "LEDIT及EDIT简述"
date:   2016-12-22 19:40
categories: jekyll update
---
**LEDIT及EDIT简述**  
![](/image/LEDIT宣传.png)  

  
  
EDIT是LEXUGE用C语言制作的一款命令行文本编辑软件，目前功能简单  
LEDIT是LEXUGE在Linux下用纯C制作，不依赖任何非标准函数库的终端文本编辑软件，功能与EDIT一样  
上述两款软件全部遵守[GPL协议](http://www.gnu.org/licenses/gpl.txt)(以本文所述作为最后实际有效话语)  
两个版本书写的文档基本兼容  
下面是帮助：  
- 使用上，下，左，右键来移动光标  
- 使用Ctrl+w保存文件  
- 使用Ctrl+r打开文件  
- 使用ESC来退出(LEDIT需要两次ESC)  
- 在加密文件时，请记住您输入的数字，在下次打开同一个文件时，请输入这个数字以解密  
- 在打开文件时，请确保文件没有制表符(Tab)  
- 当文件小范围损坏时，请以非LEDIT文件的选项打开尝试恢复到正确格式  

  
  
Copyright ("2015-2016") LEXUGE  

Tips:在使用LEDIT编辑EDIT的文件时，请先使用```dos2unix```命令来转换格式，在使用EDIT编辑LEDIT时，请在Linux平台先用```unix2dos```来转换格式  


