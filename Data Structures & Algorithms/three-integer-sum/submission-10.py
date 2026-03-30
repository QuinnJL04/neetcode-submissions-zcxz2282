class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            else:
                i = k + 1
                j = len(nums) - 1
                while i < j:
                    summ = nums[k] + nums[i] + nums[j]
                    if summ == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        i += 1
                        while nums[i] == nums[i - 1] and i < j:
                            i+=1
                    elif summ < 0:
                        i += 1
                    else:
                        j -= 1
                        while nums[j] == nums[j + 1] and i < j:
                            j -= 1
        return res
