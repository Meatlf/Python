##plt 显示图片
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
 
src0 = cv.imread("1.png")
plt.imshow(src0)
plt.show()

src1 = cv.imread("2.jpg")
src1RGB = cv.cvtColor(src1,cv.COLOR_BGR2RGB)
plt.imshow(src1RGB)
plt.show()