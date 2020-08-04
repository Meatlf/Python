# ROI
# 参考资料
# [OpenCV-Python 选择ROI](https://blog.csdn.net/wsp_1138886114/article/details/90731929)
import cv2

src = cv2.imread("FinderPattern.bmp")
roi = src[0:20, 0:30]

cv2.imshow('roi', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
