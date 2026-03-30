class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in seen:
                seen[diff] = i
            else:
                return [min(i, seen[nums[i]]), max(i, seen[nums[i]])]
        