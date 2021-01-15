# https://leetcode-cn.com/leetbook/read/linked-list/f9izv/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # 哨兵节点广泛应用于树和链表中，如伪头、伪尾、标记等，它们是纯功能的，通常不保存任何数据，
        # 其主要目的是使链表标准化，如使链表永不为空、永不无头、简化插入和删除
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur   # 避免出现连续的val值
            cur = cur.next  # 无论是cur.val == val 还是 cur.val != val ，cur都要更新迭代
        return dummy.next
