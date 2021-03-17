# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # # 双指针
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(1)
        # cur = head
        # pre = None
        # while cur:
        #     tmp = cur.next  # 暂存cur后节点
        #     cur.next = pre  # 修改next指向
        #     pre = cur       # 访问下一节点
        #     cur = tmp       # 访问下一节点
        # return pre

        # 递归
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        def recur(cur, pre):
            if not cur: return pre      # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre              # 修改节点引用指向
            return res                  # 返回反转链表的头节点

        return recur(head, None)        # 调用递归并返回
