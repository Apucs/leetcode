class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # print(numbers, "\t", target)
        
        diff = dict()
        # print(diff)
        
        #a = {7: 0, 2: 1, -2: 2, -6: 3}
        
        for i, num in enumerate(numbers):
            d = target-num
            
            if d not in diff:
                diff.update({num:i})
                
        # print(diff)
        
        for i, num in enumerate(numbers):
            d = target-num
            if (d in diff) and (i!=diff[d]):
                # print([diff[d]+1, i+1])
                return [diff[d]+1, i+1]
        