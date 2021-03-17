# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # # 两次遍历
        # # 第一次遍历得到length
        # def getlength(head):
        #     length = 0
        #     while head:
        #         length += 1
        #         head = head.next
        #     return length
        # dummy = ListNode(0, head)
        # l = getlength(head)
        # cur = dummy
        # # 第二次遍历删除节点
        # for i in range(1, l-n+1):
        #     cur = cur.next
        # cur.next = cur.next.next
        # return dummy.next

        # 一次遍历，双指针
        dummy = ListNode(0,head)
        fast = head
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
