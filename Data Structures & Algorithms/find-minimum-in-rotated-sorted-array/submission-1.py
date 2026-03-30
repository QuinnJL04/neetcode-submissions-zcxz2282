class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        mid = (l + r) // 2
        min_val = nums[0]
        for i in range(r):
            min_val = min(min_val, nums[i])

        return min_val