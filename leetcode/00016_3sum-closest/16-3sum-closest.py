class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest = 0
        mindiff = float("inf")
        for i in range(len(nums)-2):

            l = i+1
            r = len(nums)-1
            while l < r:
                Sum = nums[i]+nums[l]+nums[r]
                if abs(Sum-target) < mindiff:
                    closest = Sum
                    mindiff = abs(Sum-target)
                if Sum > target:
                    r -= 1
                elif Sum < target:
                    l += 1
                else:
                    return closest
        return closest
