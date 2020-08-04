# FindContours

## 参考资料

[1] [OpenCV—轮廓操作一站式详解：查找/筛选/绘制/形状描述与重心标注(Python版)](https://blog.csdn.net/iracer/article/details/90695914)

## QA

**Q**:如何理解以下语句中的`contours`和`hierarchy`?

```python
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # for opencv4.1
print("find", len(contours), "contours")
```

**A**:

1)轮廓变量contours中有n个向量，即找到n个轮廓。调试展开contours变量，可以看到每个元素都是一个由一系列轮廓上的点组成的;

2)调试展开hierarchy变量，可以看到其类型为ndarray的n维数组，维度为(1, 21, 4)，第二维度对应轮廓的索引号（共21个轮廓），第三维度为1×4的轮廓级别信息（每个轮廓包含4个级别描述量[Next，Previous，First_Child，Parent]）。