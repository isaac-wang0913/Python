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
        carry = 0   # 初始化进位为0
        while l1 or l2:     # l1 l2 有一个未结束，继续遍历
            val1 = l1.val if l1 else 0  # 结束的链表值为0
            val2 = l2.val if l2 else 0  # 结束的链表值为0
            total = val1 + val2 + carry
            carry = total // 10     # 进位处理
            cur.next = ListNode(total % 10)      # 返回结果链表的下一位,防止溢出
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:   # 退出循环时，对最后进位的处理
            cur.next = ListNode(carry)
        return dummy.next
