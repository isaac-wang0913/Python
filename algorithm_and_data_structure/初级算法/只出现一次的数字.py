class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 位运算，使用异或运算 a ^ a = 0, a ^ a ^ b = b, a ^ 0 = a
        result = nums[0]
        for j in range(1 , len(nums)):
            result = result ^ nums[j]
        return result
