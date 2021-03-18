# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        # 递归 深度优先搜索DFS
        # 自底向上” 是另一种递归方法。
        # 在每个递归层次上，我们首先对所有子节点递归地调用函数，然后根据返回值和根节点本身的值得到答案
        # 这个过程可以看作是后序遍历的一种
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # 自底向上
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # 自顶向下意味着在每个递归层级，我们将首先访问节点来计算一些值，
        # 并在递归调用函数时将这些值传递到子节点。 所以 “自顶向下” 的解决方案可以被认为是一种前序遍历
        # def top_down(node, h):
        #     if not node:
        #         return h
        #     return max(top_down(node.left, h+1), top_down(node.right, h+1))
        # return top_down(root,0)

        # 广度优先搜索 BFS
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return 0
        height = 0
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            height += 1
        return height
