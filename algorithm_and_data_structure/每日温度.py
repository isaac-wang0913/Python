class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 单调栈：维护一个存储下标的单调栈
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        stack = []
        result = [0 for i in range(len(T))]
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result
