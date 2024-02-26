# import easyocr

# #设置识别中英文两种语言
# reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory
# result = reader.readtext(r"C:\Users\Administrator\Pictures\123.png", detail = 0)
# print(result)

import PaddleOCR
# PaddleOCR  百度开源


ocr = PaddleOCR (use_angle_cls=True, lang="ch")
# 输入待识别图片路径
img_path = r"C:\Users\Administrator\Pictures\123.png"
# 输出结果保存路径
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)

from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.show()

# ALTAKOr7fjafGSt7pSNnjlIsam	
# 5a55ab1ff9c14436b2a95bea24444ae7