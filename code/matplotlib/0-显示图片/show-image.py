##plt 显示图片
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
 
src = cv.imread("1.png")

plt.imshow(src)
plt.show()
