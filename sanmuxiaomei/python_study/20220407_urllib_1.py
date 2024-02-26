# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220407_urllib_1.py
# Time       ：2022/4/4 16:40
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""
import urllib.request

# #网页
# url_page="http://www.baidu.com"
# url_name='baidu.html'
# #下载网站
# urllib.request.urlretrieve(url_page,url_name)
# #下载图片
# url_img='http://www.baidu.com'
# img_name='b'
# urllib.request.urlretrieve(url_img,filename=img_name)
# #下载视频
# url_video=""
# url_vname=''
# urllib.request.urlretrieve(url_video,url_vname)


def url_down(url_page,url_name):
    urllib.request.urlretrieve(url_page,url_name)

a=r'C:\Users\cc\Pictures\电源面.png'
b='电源1.jpg'
s1=url_down()
s1(a,b)

