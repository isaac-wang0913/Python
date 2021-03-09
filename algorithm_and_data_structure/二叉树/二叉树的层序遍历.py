# https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefh1i/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        # 广度优先需要用队列作为辅助结构
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            tmp = []
            length = len(queue)   # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
            # 如果节点的左/右子树不为空，也放入队列中
            for i in range(length):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if  cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(tmp)
        return result
