class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            # 末尾不为9，不需要进位
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                # 末位为9，只进一位 或者 末位为9，一直进位到第一位
                digits[i] = 0
                if digits[0] == 0:
                    digits.insert(0,1)
                    return digits
