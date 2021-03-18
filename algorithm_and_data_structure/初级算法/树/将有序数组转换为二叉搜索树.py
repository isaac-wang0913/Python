# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 递归
        if not nums:
            return
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid+1:]
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node
