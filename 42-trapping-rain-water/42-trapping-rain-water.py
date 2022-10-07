class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right= len(height)-1
        left_high = right_high = 0
        ans = 0 
        
        while left<=right:
            if left_high<=right_high:
                
                if left_high > height[left]:
                    ans += left_high - height[left]
                    
                else:
                    left_high = height[left]
                
                left+=1
                
            else:
                if right_high>height[right]:
                    ans+=right_high - height[right]
                    
                else:
                    right_high = height[right]            
                right -= 1
                
        return ans
                    