# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 方法1：哈希表
        # 遍历所有节点，每次遍历到一个节点时，判断该节点此前是否被访问过
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # lookup = set()
        # cur = head
        # while cur:
        #     if cur in lookup:
        #         return True
        #     else:
        #         lookup.add(cur)
        #         cur = cur.next
        # return False

        # 方法2：快慢指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        slow = head
        fast = head
        while fast and fast.next:    # 如果不加fast.next 就会溢出
            # do-while, 防止slow, fast都在head，循环就不会执行
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
