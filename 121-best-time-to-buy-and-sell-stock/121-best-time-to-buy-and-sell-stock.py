class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        max_profit = 0
        
        l = 0
        r = 1
        for r in range(1,len(prices)):
            
            profit = prices[r] - prices[l]
            
            if profit<=0:
                l = r
                
            else: 
                max_profit = max(max_profit, profit)
                
            # print(l, r, max_profit)
                
        
                    
                
        return max_profit
            
            
        