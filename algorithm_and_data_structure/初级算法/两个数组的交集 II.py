from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # 哈希表
        # # 时间复杂度：O(m + n )
        # # 空间复杂度：O(min(m. n))
        # # 为了降低空间复杂度
        # if len(num1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        # n = Counter(nums1)
        # result = []
        # for num in nums2:
        #     if num in nums1 and n[num] > 0:
        #         result.append(num)
        #         n[num] -= 1
        # return result

        # 双指针
        # 时间复杂度：O(m + n )
        # 空间复杂度：O(min(m. n))
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        result = []
        while i < n1 and j < n2:
            if nums1[i] < nums[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result
