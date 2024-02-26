

'''
from cnstd import CnStd
from cnocr import CnOcr

std = CnStd()
cn_ocr = CnOcr()

box_infos = std.detect('002\multi-line_cn1.png')

for box_info in box_infos['detected_texts']:
    cropped_img = box_info['cropped_img']
    ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
    print('ocr result: %s' % str(ocr_res))
'''

import Date_needed

#获取某个文件夹中的文件生成一个列表
filePath = "./003"
filePath_list = Date_needed.data_needed(filePath)
print(f'_______________________{filePath_list}')