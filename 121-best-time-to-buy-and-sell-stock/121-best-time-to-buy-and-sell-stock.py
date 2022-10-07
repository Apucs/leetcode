class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        max_profit = 0
        
        i = 0
        j=1
        while j<len(prices):
            
            profit = prices[j] - prices[i]
            
            if profit<=0:
                i = j
                j+=1
                
            else: 
                max_profit = max(max_profit, profit)
                j+=1
            print(i, j, max_profit)
                
        
                    
                
        return max_profit
            
            
        