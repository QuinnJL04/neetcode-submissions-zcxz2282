class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = nums[0]
        while l <= r:
            mid = (l+r) // 2
            if nums[l] < nums[r]:
                result = min(nums[l], result)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            result = min(result, nums[mid])
        return result