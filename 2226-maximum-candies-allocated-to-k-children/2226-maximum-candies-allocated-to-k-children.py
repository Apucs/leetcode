class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        l, r = 1, max(candies)

        res = 0


        if sum(candies) < k:
            return res

        while l<=r:

            child = 0
            noCandies = (l+r)//2

            for candy in candies:
                child += floor(candy/noCandies)

            if child >= k:
                res = max(res, noCandies)
                l = noCandies + 1

            elif child<k:
                r = noCandies - 1

        # print(res)
        return res