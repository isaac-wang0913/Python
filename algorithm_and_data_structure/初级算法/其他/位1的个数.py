class Solution:
    def hammingWeight(self, n: int) -> int:
        # 位移动
        # & 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
        count = 0
        while n > 0:
            count += n & 1
            n = n >> 1
        return count
