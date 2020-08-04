# 参考资料
# [1] [Python-Opencv 轮廓常用操作](https://www.cnblogs.com/zhangxiaoman/p/12390742.html)
# [2] [Python+OpenCV图像处理之轮廓发现](https://www.cnblogs.com/qianxia/p/11102800.html)
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread('FinderPattern.bmp')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

pt = (15, 25)
# 遍历所有轮廓
for i, contour in enumerate(contours):
    if (cv2.pointPolygonTest(contour, pt, False) == 1):
        print(i)
        img = cv2.drawContours(img, contours, i, (0, 255, 0), 1)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# blue = (255, 0, 0)
# img = cv2.circle(img, pt, 1, blue, -1)

# isInPolygon = cv2.pointPolygonTest(contours[0], pt, False)
# print(isInPolygon)
plt.imshow(img)
plt.show()
