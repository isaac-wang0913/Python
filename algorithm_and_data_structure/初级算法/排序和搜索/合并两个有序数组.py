class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 方法1：python的切片
        # 时间复杂度: O((n + m)log(n + m))
        # 空间复杂度: O(1)
        # python中切片是原地修改
        # nums1[:] = sorted(nums1[:m] + nums2)
        # return nums1

        # 方法2：双指针，从前往后，需要使用额外空间
        # 时间复杂度: O(n + m)
        # 空间复杂度: O(m)
        # new_num1 = nums1[:m]
        # nums1[:] = []
        # p, q = 0, 0
        # while p < m and q < n:
        #     if new_num1[p] < nums2[q]:
        #         nums1.append(new_num1[p])
        #         p += 1
        #     else:
        #         nums1.append(nums2[q])
        #         q += 1
        # if p < m:
        #     nums1.extend(new_num1[p:])
        # if q < n:
        #     nums1.extend(nums2[q:])

        # 方法3：双指针，从后往前，不需要额外空间
        # 时间复杂度: O(n + m)
        # 空间复杂度: O(1)
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
