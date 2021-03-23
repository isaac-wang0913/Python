class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # ^按位异或运算符：当两对应的二进位相异时，结果为1
        xory = x ^ y
        count = 0
        while xory > 0:
            count += xory & 1
            xory = xory >> 1
        return count
