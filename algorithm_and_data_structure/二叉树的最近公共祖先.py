# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:        # 递归的终止条件
            return
        if root == q or root == p:
            return root     # 递归的终止条件
        # 返回值
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not (left or right):
            return
        elif not left:
            return right
        elif not right:
            return left
        else:
            return root
