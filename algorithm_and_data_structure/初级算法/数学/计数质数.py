class Solution:
    def countPrimes(self, n: int) -> int:
        # 暴力解法 超时
        # res = 0
        # for i in range(2,n):
        #     for j in range(2,i):
        #         if i % j == 0:
        #             break
        #     else:
        #         res += 1
        # return res

        # 厄拉多塞筛法
        # 定义数组标记是否是质数
        is_prime = [1] * n
        res = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                res += 1
                # 从 i*i 开始标记
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        return res
