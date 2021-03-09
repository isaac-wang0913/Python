# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 递归的终止条件是两个节点都为空
        # 或者两个节点中有一个为空
        # 或者两个节点的值不相等
        # if not root:
        #     return True
        # def dfs(left, right):
        #     if not (left or right):
        #         return True
        #     if not (left and right):
        #         return False
        #     if left.val != right.val:
        #         return False
        #     return dfs(left.right, right.left) and dfs(left.left, right.right)
        # return dfs(root.left, root.right)

        # 迭代
        # 维护一个队列
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
