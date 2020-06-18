import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread('2.bmp')
rows, cols, ch = img.shape

pts1 = np.float32([[0, 0], [68, 0], [0, 72], [68, 72]])
pts2 = np.float32([[0, 0], [34, 0], [0, 48], [56, 48]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (68, 72))

M = cv2.getPerspectiveTransform(pts2, pts1)
dst = cv2.warpPerspective(dst, M, (68, 72))

blue = [0, 0, 255]
dst = cv2.circle(dst, (60, 20), 3, blue, -1)

plt.imshow(dst)
plt.show()

img = cv2.imread('test-HanXinBin.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('test-HanXinBin2.bmp', img)
rows, cols = img.shape

pts1 = np.float32([[11, 11], [36, 11], [11, 36], [36, 36]])
pts2 = np.float32([[5.5, 5.5], [21.5, 5.5], [5.5, 21.5], [21.5, 21.5]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (27, 27))
cv2.imwrite('test-HanXinBin3.bmp', dst)

plt.imshow(dst)
plt.show()

img = cv2.imread('qrBin.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = img.shape

pts1 = np.float32([[30, 30], [116.5, 30], [102, 102], [30, 116.5]])
pts2 = np.float32([[3.5, 3.5], [21.5, 3.5], [18.5, 18.5], [3.5, 21.5]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (25, 25))
ret, thresh = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY)
cv2.imwrite('test-QRcode.bmp', thresh)

plt.imshow(thresh)
plt.show()
