import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

src = np.zeros((300, 300, 3), dtype="uint8")

# 画直线
cv2.line(src, (0, 0), (300, 300), green)

# 画正方形
cv2.rectangle(src, (50, 200), (200, 225), red, 1)

# 画圆
src = cv2.circle(src, (255, 255), 3, blue, -1)

# 画任意角度的矩形
points = np.array([[23, 56], [35, 89], [58, 90], [100, 192]])
src = cv2.circle(src, tuple(points[0]), 5, blue, -1)
src = cv2.circle(src, tuple(points[1]), 5, blue, -1)
src = cv2.circle(src, tuple(points[2]), 5, blue, -1)
src = cv2.circle(src, tuple(points[3]), 5, blue, -1)
rect = cv2.minAreaRect(points)
box = cv2.boxPoints(rect)
box = np.int0(box)
src = cv2.drawContours(src, [box], 0, red, 2)

plt.imshow(src)
plt.show()
