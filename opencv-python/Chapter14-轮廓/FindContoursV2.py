# 在ROI中查找轮廓并进行筛选
# 参考资料
# [1] [Python-Opencv 轮廓常用操作](https://www.cnblogs.com/zhangxiaoman/p/12390742.html)
# [2] [Python+OpenCV图像处理之轮廓发现](https://www.cnblogs.com/qianxia/p/11102800.html)
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
img = cv2.drawContours(ROI, contours, I, (0, 255, 0), 1)

blue = (255, 0, 0)
ROI = cv2.circle(ROI, pt, 1, blue, -1)

plt.imshow(ROI)
plt.show()
