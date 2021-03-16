class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 双指针，快速排序的思想 for实现
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] == 0:
        #         continue
        #     else:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        # return nums

        # while 实现
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return nums
