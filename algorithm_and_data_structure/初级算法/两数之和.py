class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 暴力解法
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # 哈希表
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],i]
            dic[num] = i
        return []
