class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        # print(sorted_nums, "\tLength of the array: ", len(sorted_nums))
        
        max_count = 0
        count = 0
        
        if len(sorted_nums)<=1:
                return len(sorted_nums)
        
        for i in range(len(sorted_nums)-1):
            #print(i)
            if (sorted_nums[i+1]-sorted_nums[i])==0:
                count = count
                # print("present count for value {}:".format(sorted_nums[i]), count)
            
            elif (sorted_nums[i+1]-sorted_nums[i])==1:
                count += 1
                # print("present count for value {}:".format(sorted_nums[i]), count)
                
            else:
                max_count = max(max_count, count+1)
                # print(max_count)
                count=0
                
            if i+1==len(sorted_nums)-1:
                max_count = max(max_count, count+1)
                # print("traversing the array has been completed:==>", max_count)
                break
                
        # print(max_count)
        
        return max_count