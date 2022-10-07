class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        l = r = 0
        
        deq = collections.deque()
        
        for r in range(len(nums)):
            
            while deq and nums[deq[-1]]<nums[r]:
                deq.pop()
                
            deq.append(r)

            
            if l>deq[0]:
                deq.popleft()
                
            if r+1>=k:
                output.append(nums[deq[0]])
                l+=1
  
        return output
        