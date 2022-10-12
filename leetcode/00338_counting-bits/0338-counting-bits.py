class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0]*(n+1)
        offset = 1

        for i in range(1, n+1):
            if i == 2*offset:
                offset = i

            ans[i] = (1 + ans[i-offset])
            # print(ans)

        return ans
