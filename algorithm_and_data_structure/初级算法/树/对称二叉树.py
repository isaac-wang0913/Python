# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归
        # if not root:
        #     return True
        # def dfs(left, right):
        #     if not (left or right):
        #         return True
        #     if not (left and right):
        #         return False
        #     if left.val != right.val:
        #         return False
        #     return dfs(left.left, right.right) and dfs(left.right, right.left)
        # return dfs(root.left, root.right)
    
        # 迭代
        if not root or not (root.left or root.right):
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
