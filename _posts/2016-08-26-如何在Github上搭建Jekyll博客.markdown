---
layout: default
title:  "如何在Github上搭建Jekyll博客"
date:   2016-08-26 14:24
categories: jekyll update
---
>Jekyll 是一个简单的博客形态的静态站点生产机器。它有一个模版目录，其中包含原始文本格式的文档，通过 Markdown （或者 Textile） 以及 Liquid 转化成一个完整的可发布的静态网站，你可以发布在任何你喜爱的服务器上。Jekyll 也可以运行在 GitHub Page 上，也就是说，你可以使用 GitHub 的服务来搭建你的项目页面、博客或者网站，而且是完全免费的。

[Jekyll 官网](http://jekyllrb.com/)  
[Jekyll 国内镜像](http://jekyll.bootcss.com/)

Jekyll的安装过程还是比较坎坷的
- 首先安装RubyGems
```
sudo dnf install rubygems
```
- 安装完成后你得安装一些devel包，包括ruby-devel, libffi-devel, libxml2-devel, libyaml-devel等
- 完成后执行以下命令
```
sudo gem install jekyll
```
- 如果全程无报错，那么恭喜你，你已经成功一大半了，试试这个
```
jekyll -v
```
- 如果正常返回版本号的话，输入以下命令
```
bundle
```
- 系统会提示你安装bundle，安装完成后，整个安装过程就OK了！

OK,接下来，我们就要搭建第一个自己的第一个BLOG了
- 首先在Github上创建一个仓库，名字为{username}.github.io
- 完了之后执行下面命令(你已经安装完并配置了GIT)
```
sudo git clone {你的仓库git地址}
```
- 接下来，我们就要来生成BLOG了，使用下面的命令
```
jekyll new blog
cd blog
jekyll serve
```
- 现在，你的BLOG已经在http://localhost:4000/上了！
- 只要将你的_site文件夹里的内容复制进GIT仓库，并执行以下命令(在GIT仓库的目录下）就可以在{username}.github.io访问了
```
sudo git add --all
sudo git commit -m "提交信息"
sudo git push
```
- 完成！
>建议使用```jekyll serve --watch```模式，这样系统一检测到改动就会自动生成，无需build  
请将文章写在_posts文件夹下

By LEXUGE

