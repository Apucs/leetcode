class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # return str(int(num1)*int(num2))

        if "0" in (num1, num2):
            return "0"

        res = [0]*(len(num1)+len(num2))

        d1 = num1[::-1]
        d2 = num2[::-1]

        for i in range(len(d1)):
            for j in range(len(d2)):
                res[i+j] += int(d1[i])*int(d2[j])
                res[i+j+1] += res[i+j]//10
                res[i+j] %= 10

        return "".join(map(str, res[::-1])).lstrip("0")
