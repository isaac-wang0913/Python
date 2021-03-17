class Solution:
    def reverse(self, x: int) -> int:
        # 字符串的简单运用和int之间的转换
        s = str(x)
        if s[0] != '-':
            result = s[::-1]
        else:
            result = int('-' + s[:0:-1])
        if ((-2) ** 31) <= result <= (2 ** 31 - 1):
            return result
        else:
            return 0
