class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        total = sum(arr)
        
        if total%3!=0: return False
        
        part = total//3
        
        counter = 0
        curr_count = 0

        for i in range(len(arr)):
            
            if counter==2: return True
            
            curr_count += arr[i]
            
            if curr_count == part:
                counter+=1
                curr_count=0
                
            
            
        return False
            
        