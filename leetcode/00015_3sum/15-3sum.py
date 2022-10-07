class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        target = 0

        nums.sort()
        res = set()

        for i in range(len(nums)):
            j = i+1

            k = len(nums) - 1

            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:

                    res.add(tuple([nums[i], nums[j], nums[k]]))

                if curr_sum < target:
                    j = j+1
                else:
                    k = k-1

        return res
