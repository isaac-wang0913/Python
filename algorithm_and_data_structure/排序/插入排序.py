# 插入排序：有序区只有一个，每次从无序区找一个数插入有序区的正确位置
# 时间复杂度O(n^2)

import random

def insert_sort(li):
    for i in range(1, len(li)):     #一共摸n-1张排，i表示无序曲的下标
        tmp = li[i]     #临时变量存储摸到的牌
        j = i - 1   # j指的手里牌的下标
        while j >= 0 and li[j] > tmp:   #插入到有序区
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

li = [random.randint(0, 100) for i in range(10)]
print(li)
insert_sort(li)
print(li)


