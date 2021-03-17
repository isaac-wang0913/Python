class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pythonic 的方法
        new_s = ''.join(ss.lower() for ss in s if ss.isalnum())
        return new_s == new_s[::-1]

        # 双指针
        # new_s = "".join(ss.lower() for ss in s if ss.isalnum())
        # left = 0
        # right = len(new_s)-1
        # while left < right:
        #     if new_s[left] != new_s[right]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True
