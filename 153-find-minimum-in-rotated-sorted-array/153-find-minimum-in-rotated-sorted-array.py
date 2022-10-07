class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return nums[0]
        
        min_val = nums[0]
        l, r = 0, len(nums)-1
        
        while l<=r:
            m = (l+r)//2  
            min_val = min(min_val, nums[m])
            
            if nums[l]<nums[r]:
                min_val = min(min_val, nums[l])
                break
            
            if nums[m]> nums[m+1]:
                min_val = nums[m+1]
                break
            
            if nums[m]>=nums[l]:
                l = m+1
            else:
                r = m-1          
            
            
        return min_val