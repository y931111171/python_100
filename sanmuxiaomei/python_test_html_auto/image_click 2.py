#图片识别点击功能

# _*_ coding:UTF-8 _*_


import aircv as ac
def matchImg(imgsrc,imgobj,confidence=0.7):
    '''#imgsrc=原始图像，imgobj=待查找的图片,confidencevalue相识度'''
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
 
    match_result = ac.find_template(imsrc,imobj,confidence)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape']=(imsrc.shape[1],imsrc.shape[0])#0为高，1为宽

    return match_result


imgsrc = 'sanmuxiaomei\python_test_auto\Snipaste_2022-07-22_00-20-32.png'
imgobj = 'sanmuxiaomei\python_test_auto\number_0.png'

f1 = matchImg()
f1(imgsrc,imgobj)