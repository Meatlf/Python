# 在ROI中查找轮廓并进行筛选
# 参考资料
# [1] [Python-Opencv 轮廓常用操作](https://www.cnblogs.com/zhangxiaoman/p/12390742.html)
# [2] [Python+OpenCV图像处理之轮廓发现](https://www.cnblogs.com/qianxia/p/11102800.html)
# [3] [OpenCV—轮廓操作一站式详解：查找/筛选/绘制/形状描述与重心标注(Python版)](https://blog.csdn.net/iracer/article/details/90695914#7.%E6%A0%87%E6%B3%A8%E8%BD%AE%E5%BB%93%E9%87%8D%E5%BF%83)
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread('FinderPattern.bmp')

pt = (15, 25)
ROI = img[pt[1]-13:pt[1]+13, pt[0]-13:pt[0]+13]

ROIgray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(ROIgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 遍历所有轮廓r
pt = (13, 13)
minArea = 1000
I = 0

for i, contour in enumerate(contours):
    if((cv2.pointPolygonTest(contour, pt, False) == 1) and (cv2.contourArea(contour) < minArea)):
        minArea = cv2.contourArea(contour)
        I=i
ROI = cv2.drawContours(ROI, contours, I, (0, 255, 0), 1)

red = (255, 0, 0)
blue = (0,0,255)
green = (0,255,0)

ROI = cv2.circle(ROI, pt, 1, red, -1)  # 画红点

mom = cv2.moments(contours[I])
pt = (int(mom['m10'] / mom['m00']), int(mom['m01'] / mom['m00']))  # 使用前三个矩m00, m01和m10计算重心
cv2.circle(ROI, pt, 1, blue, -1)  # 画蓝点

plt.imshow(ROI)
plt.show()
