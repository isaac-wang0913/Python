# https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xeywh5/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return []
        result = [root.val]
        return result + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # 迭代
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 递归的时候隐式地维护了一个栈，而我们在迭代的时候需要显式地将这个栈模拟出来
        result = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                result.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return result
