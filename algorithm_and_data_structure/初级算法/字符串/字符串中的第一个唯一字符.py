class Solution:
    def firstUniqChar(self, s: str) -> int:
        # # 哈希表
        # import collections
        # count = collections.Counter(s)
        # for i in range(len(s)):
        #     if count[s[i]] == 1:
        #         return i
        # else:
        #     return -1
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for j in range(len(s)):
            if dic[s[j]] == 1:
                return j
        return -1
