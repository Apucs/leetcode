class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for v in tokens:
            if v in "+-*/":
                a, b = stack.pop(), stack.pop()
                if v == "/":
                    stack.append(str(int(eval(b+v+a))))
                else:
                    stack.append(str(eval(b + v + a)))
            else:
                stack.append(v)

        return stack.pop()
