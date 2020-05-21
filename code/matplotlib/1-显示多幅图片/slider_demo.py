##plt 同时显示多幅图像
import cv2 as cv
import matplotlib.pyplot as plt
 
src0 = cv.imread("1.png",0)
src1 = cv.imread("2.jpg",0)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(src0)
plt.subplot(1,2,2)
plt.imshow(src1)
plt.show()