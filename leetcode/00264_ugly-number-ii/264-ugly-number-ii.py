class Solution:
    def nthUglyNumber(self, n: int) -> int:

        if n == 1:
            return 1
        p2, p3, p5 = 0, 0, 0
        res = [0]*n
        res[0] = 1
        for i in range(1, n):
            val = min(2*res[p2], 3*res[p3], 5*res[p5])

            if val == 2*res[p2]:
                p2 += 1
            if val == 3*res[p3]:
                p3 += 1
            if val == 5*res[p5]:
                p5 += 1

            res[i] = val

        return res[-1]
