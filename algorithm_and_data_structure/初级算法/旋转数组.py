class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方法1 暴力法
        # # 时间复杂度：O(n)
        # # 空间复杂度：O(n)
        # n = len(nums)
        # li = [0 for _ in range(n)]
        # for i in range(n):
        #     li[(i+k) % n] = nums[i]
        # for i in range(n):
        #     nums[i] = li[i]
        # return nums

        # 方法2 数组的切片,但会使用额外的空间，空间复杂度不是O(1)
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]
        # return nums

        # 方法3 pythonic的方法
        # n = len(nums)
        # k = k % n
        # for i in range(k):
        #     tmp = nums.pop()
        #     nums.insert(0, tmp)
        # return nums

        # 方法4 三次旋转
        n = len(nums)
        k = k % n
        nums[:] = nums[::-1]
        nums[k:] = nums[k:][::-1]
        nums[:k] = nums[:k][::-1]
        return nums
