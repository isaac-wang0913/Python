# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)

        # 递归的终止条件：1.只有一个节点 2.没有节点None
        if not head or not head.next:
            return head
        # 递归表达式
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head
