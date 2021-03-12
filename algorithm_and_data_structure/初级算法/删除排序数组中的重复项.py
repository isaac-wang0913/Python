class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # while 循环
        i, j = 0, 1
        n = len(nums)
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        return i+1

        # for 循环
        i = 0
        n = len(nums)
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
