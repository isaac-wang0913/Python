class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 纵向扫描时，从前往后遍历所有字符串的每一列
        # 比较相同列上的字符是否相同，如果相同则继续对下一列进行比较，如果不相同则当前列不再属于公共前缀
        if not strs:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
