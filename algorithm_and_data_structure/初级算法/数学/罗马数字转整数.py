class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        j = 0
        for i in range(len(s)-1):
            # 把一个小值放在大值的左边，就是做减法，否则为加法
            if dic[s[i]] >= dic[s[i + 1]]:
                j += dic[s[i]]
            else:
                j -= dic[s[i]]
        return j + dic[s[-1]]
