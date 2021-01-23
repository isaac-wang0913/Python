# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum):
        # 递归 DFS
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # if not root:
        #     return False
        # if not (root.left or root.right):   # 左右子树同时为空才是叶子节点
        #     return sum == root.val
        # return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.right)

        # 迭代 BFS
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return False
        queue = [root, root.val]
        while queue:
            node = queue.pop(0)
            path = queue.pop(0)
            if not (node.left or node.right) and path == sum:
                return True
            if node.left:
                queue.append(node.left)
                queue.append(node.left.val + path)
            if node.right:
                queue.append(node.right)
                queue.append(node.right.val + path)
        return False
