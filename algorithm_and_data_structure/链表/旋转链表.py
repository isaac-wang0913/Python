# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        if not head.next:
            return head
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next    # 找到链表尾
            length += 1                 # 得到链表的长度
        old_tail.next = head            # 将链表闭合成环
        # 查找新的tail
        new_tail = head
        for i in range(length - k%length -1):
            new_tail = new_tail.next
        new_head = new_tail.next        # 新的head
        new_tail.next = None            # 打破之前形成的环
        return new_head
