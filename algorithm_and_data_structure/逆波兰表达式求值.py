class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in '+-*/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(str(int(eval(num2 + s + num1))))
            else:
                stack.append(s)
        return int(stack[-1])
