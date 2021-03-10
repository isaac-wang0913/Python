class Solution:
    def fib(self, N: int) -> int:
        # # 递归
        # if N < 2:
        #     return N
        # else:
        #     return self.fib(N-1) + self.fib(N-2)

        # 带备忘录的递归
        # visited = {}
        # def refib(N):
        #     if N in visited:
        #         return visited[N]
        #     if N < 2:
        #         result = N
        #     else:
        #         result = refib(N-1) + refib(N-2)
        #     visited[N] = result
        #     return result
        # return refib(N)

        # 动态规划
        if N < 2:
            return N
        i, j, result = 0, 0, 1
        for _ in range(2, N+1):
            i, j = j, result
            result = i + j
        return result
