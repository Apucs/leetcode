class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # print(temperatures)
        
        res = [0]*len(temperatures)
        stack = []
        
        
        for i, val in enumerate(temperatures):
            
            while stack and val>stack[-1][0]:
                stackTop, stackId = stack.pop()
                res[stackId] = i-stackId
            
            stack.append((val, i))
            
        return res

                
            