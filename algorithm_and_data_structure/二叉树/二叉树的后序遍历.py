# https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xebrb2/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return []
        result = [root.val]
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + result
        # 迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        result = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                result.append(cur.val)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return result[::-1]
