class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        max_sum = nums[0]
        pre = 0
        for num in nums:
            pre = max(num, pre + num)
            max_sum = max(max_sum, pre)
        return max_sum
