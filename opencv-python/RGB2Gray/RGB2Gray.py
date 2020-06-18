import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread('Image1.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('test-QRcode.jpg', img)
plt.imshow(img)
plt.show()
