# get_yaml.py
# -*-coding:utf-8 -*-

import yaml

def get_yaml_data(yaml_file):
    '''配置文件获取方法'''
    print("*****获取yaml数据*****")
    with open(yaml_file, encoding='utf-8')as file:
        content = file.read()
        # print(content)
        # print(type(content))
        #print("*****转换yaml数据为字典或列表*****")
        # 设置Loader=yaml.FullLoader忽略YAMLLoadWarning警告
        data = yaml.load(content, Loader=yaml.FullLoader)
        # print(data)
        # print(type(data))
        # print(data.get('Question'))
        # print(data['Question']["Q_1"])
        # 类型为字典 <class 'dict'>
        # print(data[0]["model"]) # 若类型为列表 <class 'list'>
        return data

if __name__ == "__main__":
    get_yaml_data("sanmuxiaomei\question\config.yal")

