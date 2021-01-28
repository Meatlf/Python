# -*- coding: utf-8 -*-
"""
功能：将.tif图片转换为.bmp格式
参考资料：
[1] [python 实现图片格式的批量转化，jpg转化为png或者png转化为jpg](https://blog.csdn.net/weixin_42535742/article/details/96477313)
"""

import cv2
import os

print('----------------------------------------------------')
print('程序的功能为：将该目录下输入的文件内的图片转为指定格式')  # 目前我测试了jpg转化为png和png转化为jpg。
print('转化结果保存在当前目录下的new_picture内')
print('----------------------------------------------------')

# son = raw_input('请输入需要转化的文件夹名：')
son = "./git/Python/python/data/"
# picture_type = raw_input('请输入想要将图片转化的类型：')
picture_type = "bmp"
daddir = '/home/user1/'
path = daddir + son

newpath = daddir + "./git/Python/python/outputData/"
if not os.path.exists(newpath):
    os.mkdir(newpath)

path_list = os.listdir(path)
number = 0  # 统计图片数量
for filename in path_list:
    number += 1
    portion = os.path.splitext(filename)
    print('convert  ' + filename + '  to '+portion[0]+'.'+picture_type)
    img = cv2.imread(path+"/"+filename)
    cv2.imwrite(newpath+"/"+portion[0]+'.'+picture_type, img)
print("共转化了%d张图片" % number)
print('转换完毕，文件存入 '+newpath+' 中')
cv2.waitKey(0)
cv2.destroyAllWindows()
