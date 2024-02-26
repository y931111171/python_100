# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220409_urllib_2.py
# Time       ：2022/4/9 11:12
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""

'''get 请求'''

import urllib.request
import urllib.parse

def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&'
    date = {
        'start':(page - 1) * 20,
        'limit':20
    }
    date = urllib.parse.urlencode(date)
    url = base_url + date

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('douban_' + str(page) + '.josn','w',encoding='utf-8')as fp:
        fp.write(content)
#(1)请求对象定制

#(2)获取响应数据



if __name__ == '__main__':
    start_page = int(input('请输入起始信息'))
    end_page = int(input('请输入终止信息'))

    for page in range(start_page,end_page+1):
#       请求定制
        request = create_request(page)
#       获取响应数据
        content = get_content(request)
#       下载
        down_load(page,content)