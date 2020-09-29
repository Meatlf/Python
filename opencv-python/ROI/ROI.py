# 图像叠加运算
# 功能：制作理想的，可用的测试数据
# 参考资料
# []()
import cv2
import numpy as np
import random
import os

listDir = os.listdir('./src/')
print(listDir)

for n in range(len(listDir)):
    print(n)
    (filename, extension) = os.path.splitext(listDir[n])
    print(filename)

    src = np.full((480, 640), 255, dtype='uint8')

    roi = cv2.imread("./src/"+listDir[n], cv2.IMREAD_COLOR)
    roi_resize = cv2.resize(roi, (210, 210), interpolation=cv2.INTER_CUBIC)
    roi_gray = cv2.cvtColor(roi_resize, cv2.COLOR_BGR2GRAY)

    # 生成随机数
    random_i = random.randint(0, 200)
    random_j = random.randint(0, 200)

    for j in range(roi_gray.shape[0]):
        for i in range(roi_gray.shape[1]):
            src[i+random_i, j+random_j] = roi_gray[i, j]

    cv2.imshow('src', src)
    cv2.imshow('roi', roi_gray)
    cv2.imwrite("./dst/"+filename+".bmp", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
