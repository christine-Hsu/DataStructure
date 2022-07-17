"""
升序
思想：从左到右将相邻的元素进行比较，如果左边元素比右边元素大，那么两者互换，否则保持不变
"""

import matplotlib.pyplot as plt
from random import shuffle


def bubblesort_anim(a):
    x = range(len(a))  # 坐标轴显示的时候添加一个横坐标
    swapped = True  # 标记排序是否结束
    while swapped:
        plt.clf()  # 清空显示窗口以实现动画效果
        swapped = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
                swapped = True
        plt.plot(x, a, "k.", markersize=6)
        plt.pause(0.01)


a = list(range(300))
shuffle(a)

bubblesort_anim(a)
