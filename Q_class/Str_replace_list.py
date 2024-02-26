# Str_replace_list.py
# !/usr/bin/env python
# -*-coding:utf-8 -*-
import os
import sys
BAST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAST_DIR)


from Q_class.Isit_number import isit_number

def Replace_list(list_str,replace_str=','):
    '''获取列表或字符串转为列表
    list_str:待转换文本或列表
    replace_str:转化特定标识符 如,0,%,~ ,默认,
    '''
    str_list = ''
    for i in list_str:
        if i =='[' or i == ']' or i=='\'' or i == ' ' or i == '':
            continue
        else:
            str_list +=i
    # print(str_list)
    # print(type(str_list))  
    str_list0= []
    number = 0
    count = 0
    str_text=''
    # print(len(str_list))
    # for k  in str_list:
    #     number +=1
    #     if k == ',' or number== len(str_list):
    #         str_list0.append(str_list[count:number])
    #         count = number
    #         continue
    #     elif number == len(str_list):
    #         str_list0.append(str_list[count:number])
    # return str_list0

    for k  in str_list:
        number +=1
        if k == ',':
            if str_text == '':
                continue
            elif isit_number(str_text) == True:
                str_list0.append(int(str_text))
            else:
                str_list0.append(str_text)
            str_text = ''
            # count = number
            continue
        elif number == len(str_list):
            str_text += k
            if isit_number(str_text) == True:
                str_list0.append(int(str_text))
            else:
                str_list0.append(str_text)
        else:
            str_text += k
    return str_list0



    # print(type(str_list0))    

if __name__ == '__main__':
    Question_list1= "['111','222',333,'aaa','1121']"
    L = Replace_list(Question_list1)
    print(L)








