class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = i

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
                    
        return result