import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# 读图
src0 = cv2.imread("QR147*147*8bits.bmp")
src1 = cv2.imread("QRunit25*25*8bits.bmp")
src2 = cv2.imread("HanXin59*52*8bits.bmp")

# 画图
src0 = cv2.circle(src0, (30, 30), 2, red, -1)
src0 = cv2.circle(src0, (117, 30), 2, red, -1)
src0 = cv2.circle(src0, (102, 102), 2, red, -1)
src0 = cv2.circle(src0, (30, 117), 2, red, -1)

src1 = cv2.circle(src1, (3, 3), 1, red, -1)
src1 = cv2.circle(src1, (21, 3), 1, red, -1)
src1 = cv2.circle(src1, (18, 18), 1, red, -1)
src1 = cv2.circle(src1, (3, 21), 1, red, -1)

src2 = cv2.circle(src2, (11, 11), 1, red, -1)
src2 = cv2.circle(src2, (36, 11), 1, red, -1)
src2 = cv2.circle(src2, (11, 36), 1, red, -1)
src2 = cv2.circle(src2, (36, 36), 1, red, -1)

# 显示图
plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(src0)
plt.subplot(2, 2, 2)
plt.imshow(src1)
plt.subplot(2, 2, 3)
plt.imshow(src2)
plt.show()

# src = cv2.imread('2.bmp')

# src = cv2.circle(src, (21, 22), 1, red, -1)
# src = cv2.circle(src, (46, 22), 1, red, -1)
# src = cv2.circle(src, (45, 41), 1, red, -1)
# src = cv2.circle(src, (15, 54), 1, red, -1)
# src = cv2.circle(src, (46, 47), 1, red, -1)

# src = cv2.circle(src, (10, 12), 1, red, -1)
# src = cv2.circle(src, (68, 63), 1, red, -1)

# # 获取某个点的像素值
# print(src[20, 21])

# cv2.imwrite('2_point.bmp', src)

# plt.imshow(src)
# plt.show()

# src = cv2.imread('test-QRcode.jpg')

# src = cv2.circle(src, (214, 78), 2, red, -1)
# src = cv2.circle(src, (490, 78), 2, red, -1)
# src = cv2.circle(src, (214, 354), 2, red, -1)
# src = cv2.circle(src, (458, 322), 2, blue, -1)

# cv2.imwrite('test-QRcode_FinderPatternPoint.jpg', src)

# plt.imshow(src)
# plt.show()

# # src = cv2.imread('HanXinBin.bmp')

# # src = cv2.circle(src, (11, 11), 1, red, -1)
# # src = cv2.circle(src, (36, 11), 1, red, -1)
# # src = cv2.circle(src, (11, 36), 1, red, -1)
# # src = cv2.circle(src, (36, 36), 1, red, -1)


# # cv2.imwrite('test-HanXinBin.bmp', src)

# # src = cv2.imread('qrBin.bmp')

# # src = cv2.circle(src, (30, 30), 2, red, 5)
# # src = cv2.circle(src, (116.5, 30), 2, red, 5)
# # src = cv2.circle(src, (102, 102), 2, red, 5)
# # src = cv2.circle(src, (30, 116.5), 2, blue, 5)

# # plt.imshow(src)
# # plt.show()
