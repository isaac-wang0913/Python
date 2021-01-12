# https://leetcode-cn.com/leetbook/read/linked-list/jf1cc/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        两次遍历
        时间复杂度：O(n)
        空间复杂度：O(1)
        def getlength(head):    # 第一次遍历获取长度
            length = 0
            cur = head
            while cur:
                cur = cur.next
                length += 1
            return length
        length = getlength(head)
        dummy = ListNode(0)     # 哨兵节点
        dummy.next = head
        cur = dummy
        for i in range(length-n):   #第二次遍历删除节点
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

        # 一次遍历，双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
