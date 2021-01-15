# https://leetcode-cn.com/leetbook/read/linked-list/fe0kj/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if not head:
            return
        evenhead = head.next    # 偶数头
        odd = head              # 奇数开头
        even = head.next
        while even and even.next:   # while odd 会溢出
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
