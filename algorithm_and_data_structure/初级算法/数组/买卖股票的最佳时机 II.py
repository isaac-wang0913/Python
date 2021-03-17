class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法,等价于上涨都买，下降都不买
        profit = 0
        n = len(prices)
        for i in range(n-1):
            tmp = prices[i+1] - prices[i]
            if tmp > 0:
                profit += tmp
        return profit
