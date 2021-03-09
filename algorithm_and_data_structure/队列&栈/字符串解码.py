class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], '', 0
        for c in s:
            # 当c为'['时，将当前multi和res入栈，并分别置空置0
            if c == '[':
                stack.append([multi, res])
                multi, res = 0, ''
            # 当c为']'时，stack出栈，拼接字符串res = last_res + cur_multi * res
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            # 当c为数字时，将数字字符转化为数字multi，用于后续倍数计算
            elif '0'<= c <= '9':
                multi = multi * 10 + int(c)
            # 当c为字母时，在res尾部添加c
            else:
                res += c
        return res
