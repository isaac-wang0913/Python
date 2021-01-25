# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        # 递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not inorder:
            return
        root = TreeNode(postorder[-1])
        ind = inorder.index(root.val)
        root.left = self.buildTree(inorder[0:ind], postorder[0:ind])
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
        return root
