# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node就是要删除的节点，我们任务是要把他删掉
        # 不能delete这个node A，但可以用后面的node B把这个node覆盖掉，
        # 然后用它的下下个地址node C来作为node A的下一个地址
        node.val = node.next.val
        node.next = node.next.next
