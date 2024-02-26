
#第一步：查找图片在原始图片上的坐标点

from lib2to3.pgen2 import driver
import aircv as ac
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import aircv

def matchImg(imgsrc,imgobj,confidence=0.5):#imgsrc=原始图像，imgobj=待查找的图片 最低相似度
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidence)  #返回格式 {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽
    print(match_result)
    return match_result


#调用测试
imsrc= r'C:\Users\cc\Desktop\112.png'
imobj= r'C:\Users\cc\Desktop\Snipaste_2022-07-27_22-42-12.png'
imgfile=r'C:\Users\cc\Desktop\124.png'
position = matchImg(imsrc,imobj,0.5)


 
# 说明：通过aircv的find_template()方法，来返回匹配图片的坐标结果
# 1.入参：
# find_template(原始图像imsrc，待查找的图片imobj，最低相似度confidence)

# 2.返回结果：

# {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)

# confidence：匹配相似率
# rectangle：匹配图片在原始图像上四边形的坐标
# result：匹配图片在原始图片上的中心坐标点，也就是我们要找的点击点
 
# 注意：如果结果匹配到的confidence小于入参传递的相似度confidence，则会返回None，不返回字典
# 参考文档：https://github.com/NetEaseGame/aircv
 
# 第二步：将图片匹配的坐标点，转换为手机屏幕上实际的坐标点
# 因为截图后在PC上的分辨率，和在手机上分辨率不一样，而我们通过第一步求出的坐标点是PC上截图的坐标点，一般比手机上大很多，所以需要转换一下坐标
 
# driver=webdriver.

photo_position=self.driver.get_screenshot_as_file(imgfile)   #截屏手机
 
x = self.driver.get_window_size()['width']
y = self.driver.get_window_size()['height']
size_width,size_height = x,y #获得手机d的宽高尺寸
 
confidence2= 0.8  # 定义相似度

position = matchImg(imsrc,imobj,confidence2)# 用第一步的方法，实际就是find_template()方法
 
if position != None:
    x, y = position['result']
    shape_x, shape_y = tuple(map(int,position['shape']))
    position_x,position_y=int(photo_position_x+(photo_width/shape_x*x)),int(photo_position_y+(photo_height/shape_y*y))

    self.driver.tap([(position_x, position_y)])

 
# 思路说明：
# 1.通过appium的方法driver.get_screenshot_as_file(filename)进行截图
# 2.通过appium的get_window_size获得宽高的字典，进而得到宽和高
# 3.在PC上通过截图和获取到的手机屏截图做匹配，返回匹配结果坐标以及PC上原图的尺寸
# 4.通过PC上截图和手机上屏幕的宽高比，以及在PC上的实际坐标点，获得手机上实际的坐标点
# 5.最后通过appium的方法对手机上的坐标进行点击drive.tap([x,y])
 
# 注意：为了匹配结果的精准性，截图最好在PC上原图1:1下截图，不要放大后截图，否则相似度会差很多
 
# 第三步：优化，截取手机上部分区域图片，进行相似度匹配，提高匹配精度
# 因为有些图片太小了，如果在一张大图上进行匹配，经常匹配不到。那如果知道图片出现的大概位置，可以截图那个区域再进行匹配
 
# 这里有两种区域截图方法：
# 1.根据appium定位到的元素进行截图

# driver.find_element(*element).screenshot(imgfile)

 
# 2.根据截图矩形左上角坐标（百分比x,y）和宽高（百分比）截图

# Image.open(imgfile).crop((pc_location_x,pc_location_y,pc_location_x+pc_width,pc_location_y+pc_height)).save(imgfile)

 
# 先截取整个手机屏幕，然后根据百分比以及PC上截图的宽高进行计算，通过PIL的crop()方法截图，获得截图上的坐标
# 然后根据PC和手机上图片的比例获得手机上的坐标


