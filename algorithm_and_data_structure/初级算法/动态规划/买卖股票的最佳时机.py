class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 暴力解法
        # 超时
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(1)
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])
        # return profit

        # 一次遍历，每次取到最小值和最大利润
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # maxprofit = 0
        # minprice = float("inf")
        # for price in prices:
        #     minprice = min(minprice, price)
        #     maxprofit = max(maxprofit, (price-minprice))
        # return maxprofit

        # 动态规划
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        n = len(prices)
        if n == 0:
            return 0
        dp = [0] * n
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)
        return dp[-1]
