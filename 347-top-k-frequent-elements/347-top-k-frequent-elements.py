class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}
        
        for num in nums:
            res[num] = 1 + res.get(num, 0)
        
            
        res_sorted = dict(sorted(res.items(), key = lambda x : x[1], reverse=True))
                
        return list(res_sorted.keys())[:k]
            
        