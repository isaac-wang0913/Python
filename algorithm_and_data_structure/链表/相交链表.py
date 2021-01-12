# https://leetcode-cn.com/leetbook/read/linked-list/jjbj2/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        # 双指针 + 链表拼接
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1
