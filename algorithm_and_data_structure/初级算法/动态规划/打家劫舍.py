class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = {}
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]
