# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归
        # def helper(node, lower = float("-inf"), upper = float("inf")):
        #     if not node:
        #         return True
        #     value = node.val
        #     if value <= lower or value >= upper:
        #         return False
        #     if not helper(node.right, value, upper):
        #         return False
        #     if not helper(node.left, lower, value):
        #         return False
        #     return True
        # return helper(root)

        # 递归 中序遍历
        stack, pre = [], float("-inf")
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val <= pre:
                return False
            pre = cur.val
            cur = cur.right
        return True
