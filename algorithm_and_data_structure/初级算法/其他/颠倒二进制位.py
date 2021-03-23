class Solution:
    def reverseBits(self, n: int) -> int:
        # 逐位颠倒
        result = 0
        j = 31
        while n > 0:
            result += (n & 1) << j
            j -= 1
            n = n >> 1
        return result
