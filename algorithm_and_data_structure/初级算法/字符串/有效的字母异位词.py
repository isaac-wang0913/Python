class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 哈希表
        return collections.Counter(s) == collections.Counter(t)
