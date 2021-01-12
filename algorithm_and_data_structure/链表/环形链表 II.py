# https://leetcode-cn.com/leetbook/read/linked-list/jjhf6/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCircle(self, head):
        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:    # 第一次相遇
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast     #第二次相遇
        return
