## 在一个窗口中显示多张图片
import cv2 as cv
import matplotlib.pyplot as plt
 
src0 = cv.imread("1.png")
src1 = cv.imread("2.jpg")

plt.figure()
plt.subplot(1,2,1)
plt.imshow(src0)
plt.subplot(1,2,2)
src1RGB = cv.cvtColor(src1,cv.COLOR_BGR2RGB)
plt.imshow(src1RGB)
plt.show()