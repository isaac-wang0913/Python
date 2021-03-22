class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # dp 存放中间子问题的结果
        # dp = {}
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # 动态规划
        # 只保存两项
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        i, j = 1, 1
        for _ in range(2, n+1):
            i, j = j, i + j
        return j
