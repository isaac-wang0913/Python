class Solution:
    def countAndSay(self, n: int) -> str:
        # 递归
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + '*' #防止s[i+1]溢出
        count = 1
        result = ''
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                result += str(count) + s[i]
                count = 1
        return result
