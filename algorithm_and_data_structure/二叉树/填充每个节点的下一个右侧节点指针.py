# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        # 广度优先需要用队列作为辅助结构
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # if not root:
        #     return root
        # queue = [root]
        # while queue:
        #     length = len(queue)
        #     for i in range(length):
        #         node = queue.pop(0)
        #         if i < length - 1:
        #             node.next = queue[0]
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
