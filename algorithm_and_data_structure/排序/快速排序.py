# 快速排序：取一个元素，使元素p归位，列表被p分成两部分，左边都比p小，右边都比p大，递归完成排序
# 时间复杂度 nlogn 每一层复杂度是n
# 缺点：1.递归最大深度 2.最坏情况 倒序排列，每次都是少一个数字 时间复杂度高 (加入随机化)
import random
# 框架
# def quick_sort(data, left, right):
#     if left < right:
#         mid = partition(data, left, right)
#         quick_sort(data, mid+1, right)
#         quick_sort(data, left, mid-1)

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: #从右边找比tmp小的数
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp: #从左边找比tmp大的数
            left += 1
        li[right] = li[left]  #tmp归位
    li[left] = tmp
    return left

def quick_sort(li, left, right):
    if left < right:    #至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, mid+1, right)
        quick_sort(li, left, mid-1)

li = [random.randint(0,100) for i in range(10)]
print(li)
quick_sort(li, 0, len(li)-1)
print(li)
