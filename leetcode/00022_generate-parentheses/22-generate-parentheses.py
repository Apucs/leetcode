class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openB = closeB = 0
        result = []
        stack = []

        def backtrack(openB, closeB):
            if openB == closeB == n:
                result.append("".join(stack))
                # print("\n")
                return

            if openB < n:
                stack.append("(")
                # print("From openB==>open and closed bracket:", openB+1, closeB, stack)
                backtrack(openB+1, closeB)
                stack.pop()
                # print("After poping", openB, closeB, stack, result)

            if closeB < openB:
                stack.append(")")
                # print("From closeB==>open and closed bracket:", openB, closeB+1, stack)
                backtrack(openB, closeB+1)
                stack.pop()
                # print("After poping from closed one", openB, closeB, stack, result)

        backtrack(openB, closeB)

        return result
