# https://leetcode-cn.com/leetbook/read/linked-list/f58sg/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        cur = head
        pre = None
        while cur:
            tmp = cur.next  # 暂存cur后节点
            cur.next = pre  # 修改next指向
            pre = cur       # 访问下一节点
            cur = tmp       # 访问下一节点
        return pre

        # 递归
