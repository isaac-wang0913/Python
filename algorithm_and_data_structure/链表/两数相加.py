# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 创建一个伪结点dummy和cur指向头结点, dummy用来最后返回,cur用来遍历
        dummy = ListNode(0)
        cur = dummy
        carry = 0   # 初始化进位为 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            cur.next = ListNode(total%10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            cur.next = ListNode(carry)
        return dummy.next
