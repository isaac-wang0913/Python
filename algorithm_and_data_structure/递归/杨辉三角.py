class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 递归
        # 递归的终止条件
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        # 递归的表达式
        result = self.generate(numRows-1)
        result.append([1] + [result[-1][i-1] + result[-1][i] for i in range(1, numRows-1)]+[1])
        return result
