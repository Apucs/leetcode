class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        missing = False

        if nums[0] != 0:
            return 0

        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]+1:
                return nums[i-1]+1
            else:
                continue

        return len(nums)
