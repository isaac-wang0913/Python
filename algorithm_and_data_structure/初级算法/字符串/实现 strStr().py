class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 滑动窗口，最直接的方法，沿着字符逐步移动滑动窗口
        n1 = len(haystack)
        n2 = len(needle)
        for i in range(n1-n2+1):
            if haystack[i:i+n2] == needle:
                return i
        else:
            return -1
