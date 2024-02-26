# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220410_urllib_3.py
# Time       ：2022/4/10 9:40
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""
"""post 请求"""

# Request URL: http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# Request Method: POST
# cname: 成都
# pid:
# pageIndex: 1
# pageSize: 10

import urllib.request,urllib.parse

def create_request(page,cname='成都'):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname' : cname,
        'pid' :'',
        'pageOndex': page,
        'pageSize': '10'
    }
    #post请求需要
    data = urllib.parse.urlencode(data).encode('utf-8')


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }

    request = urllib.request.Request(url=base_url,headers=headers,data=data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open('KFC_chengdu' + str(page) + '.josn','w',encoding='utf-8')as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入终止页'))

    for page in range(start_page,end_page+1):
#       请求对象组包
        request = create_request(page)
#       获取网络数据
        content = get_content(request)
#       写入文件
        down_load(page,content)
