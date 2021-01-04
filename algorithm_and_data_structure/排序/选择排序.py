# 选择排序:一趟排序记录最小值，放到第一个位置
# 关键点：无序区，无序区最小数的位置
# 一共n-1次 ，最后一次一定是最大的数
# 时间复杂度O(n^2)
import random

def select_sort(li):
    for i in range(len(li)-1):    #第i躺，一共n-1次 因为最后一次不用执行
        min_index = i   # 记录无序区最小值的索引，假设开始索引指向第一个数
        for j in range(i, len(li)):  #无序区的位置
            if li[j] < li[min_index]:
                min_index = j   #不断更新无序区最小数的位置
        li[j], li[min_index] = li[min_index], li[j]
        print(li)

li = [random.randint(0, 100) for i in range(10)]
print(li)
select_sort(li)
print(li)

