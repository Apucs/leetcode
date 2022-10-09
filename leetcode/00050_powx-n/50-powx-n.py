class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow_cus(x, n):

            # print(x, n)

            if x == 0:
                return 0
            if n == 0:
                return 1

            res = pow_cus(x*x, n//2)

            val = x*res if n % 2 else res
#             print("result for x:", res, val, x, n)

            return x*res if n % 2 else res

        res = pow_cus(x, abs(n))

        return res if n >= 0 else 1/res
