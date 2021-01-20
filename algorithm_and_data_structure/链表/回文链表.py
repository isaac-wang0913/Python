# https://leetcode-cn.com/leetbook/read/linked-list/fov6t/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        # pythonic 的方法
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # li  = []
        # cur = head
        # while cur:
        #     li.append(cur.val)
        #     cur = cur.next
        # return li == li[::-1]

        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        if not head:
            return True
        # 找到前半部分链表的尾节点并反转后半部分链表
        first_end = self.end_of_first(head)
        second_start = self.reverse_list(first_end.next)
        first = head
        second = second_start
        result = True
        while second:
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next
        # 还原链表
        first_end.next = self.reverse_list(second_start)
        return result

    def end_of_first(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
