class Solution:
    def isValid(self, s: str) -> bool:
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        dic = {'{': '}',  '[': ']', '(': ')', '?':'?'}
        stack = ['?']
        for i in s:
            if i in dic:
                stack.append(i)
            elif i != dic[stack.pop()]:
                return False
        return len(stack) == 1
