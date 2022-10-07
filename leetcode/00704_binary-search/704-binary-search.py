class Solution:
    def search(self, nums: List[int], target: int) -> int:

        min_id = 0
        max_id = len(nums)-1

        while min_id <= max_id:
            mid = (min_id+max_id)//2
            # print(min_id, max_id, mid)

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                min_id = mid+1

            elif target < nums[mid]:
                max_id = mid-1

        return -1
