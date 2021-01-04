# 冒泡排序:相邻的两个数，如果前面比后面大，则交换两个数
# 一趟排序完成后结，无序区减少一个数，有序区增加一个数
# 一共n-1次 因为最后一次不用执行，
# 无序区一共 n-i-1 (i为第几次)
# 时间复杂度O(n^2)
import random

def bubble_sort(li):
    for i in range(len(li)-1):   #第i躺，一共n-1次 因为最后一次不用执行
        exchange = False    #设置一个检查是否发生交换的变量
        for j in range(len(li)-i-1):    # 无序区一共 n-i-1 (i为第几次) 箭头不会指到最后一个数，因为后面没有数字了
            if li[j] > li[j+1]:         
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:    #不发生交换，直接退出
            return
        print(li)   #打印每一趟

li = [random.randint(0, 100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)
