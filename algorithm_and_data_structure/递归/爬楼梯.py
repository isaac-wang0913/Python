class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        i, j, result = 0, 0, 1
        for _ in range(1, n+1):
            i, j = j, result
            result = i + j
        return result
