import os 

#获取某个文件夹的文件生成一个列表

### 定义文件名获取函数
def data_needed(filePath):
    '''
    获取某个文件夹的文件生成一个列表 /n
    filePath=地址
    data_needed(filePath)
    
    '''
    import os        #引入os
    file_name = list()        #新建列表
    for i in os.listdir(filePath):        #获取filePath路径下所有文件名
        data_collect = ''.join(i)        #文件名字符串格式
        file_name.append(data_collect)        #将文件名作为列表元素填入
    print("----------获取filePath中文件名列表成功----------\n")        #打印获取成功提示
    return(file_name)        #返回列表


### 主函数
if __name__ == '__main__':
    filePath = os.path.abspath(os.curdir)        #想要获取文件名的路径
    print(data_needed(filePath))        #调用文件名获取函数，并打印结果




'''
import os

# __file__ 为当前执行的文件

#当前文件路径
print(os.path.realpath(__file__))
#当前文件所在的目录，即父路径
print(os.path.split(os.path.realpath(__file__))[0])
#找到父路径下的其他文件，即同级的其他文件
print(os.path.join(proDir,"config.ini"))

'''