class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 9999999999
        
        i, j = 0, len(height)-1
        
        max_area = 0
        
        while i<j:
            max_area = max(max_area, (j-i)*(height[i] if height[i]<height[j] else height[j]))
            
            if height[i]<height[j]: i=i+1
            else: j=j-1
                
        return max_area