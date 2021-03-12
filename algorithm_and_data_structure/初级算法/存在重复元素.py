class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 集合方法
        # return len(set(nums)) != len(nums)

        # 哈希表
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for val in dic.values():
            if val > 1:
                return True
        return False
