
# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20220407_urllib_1.py
# Time       ：2022/4/4 16:40
# Author     ：sanmuxiaomei 
# version    ：python 3.7
# email      ：349258449@qq.com 
"""


# from pywebio import start_server
# from pywebio.input import input, FLOAT
# from pywebio.output import put_text

# def bmi():  # bmi() 函数内容不变
#     height = input("请输入你的身高(cm)：", type=FLOAT)
#     weight = input("请输入你的体重(kg)：", type=FLOAT)

#     BMI = weight / (height / 100) ** 2

#     top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
#                   (22.9, '正常'), (27.5, '过重'),
#                   (40.0, '肥胖'), (float('inf'), '非常肥胖')]

#     for top, status in top_status:
#         if BMI <= top:
#             put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
#             break
# if __name__ == '__main__':
#     start_server(bmi, port=80)

Question_list1= "[122,12,33,'ssa','sdasda']"

Question_list2= "[2321,2323,444,'ssa','sdasda']"

Question_list1= eval(Question_list1)
print(Question_list1,type(Question_list1))
    