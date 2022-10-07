class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        res = max(piles)
        
        while l<=r:
            
            hour = 0
            
            m = (l+r)//2
            
            
            for pile in piles:
                hour+=ceil(pile/m)
                
            
            if hour<=h:
                res = min(res, m)
                r = m - 1
                
            elif hour>h:
                l =m + 1
        
        return res
                