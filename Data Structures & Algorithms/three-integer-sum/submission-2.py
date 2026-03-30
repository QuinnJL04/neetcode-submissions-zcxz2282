class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() #sort so ik its from least to greatest
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #this is the duplicated check
                continue
            j, k = i+1, len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    while j<k and nums[j] == nums[j+1]: #ensuring j and k are new numbers that havent been used
                        j+=1
                    while j<k and nums[k] == nums[k-1]: #ensuring j and k are new numbers that havent been used
                        k-=1
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < target: #since its sorted ik that the left pointer should be moved forward if the sum is less than the target
                    j+=1
                else: #else if its greater than the right pointer should be moved down
                    k-=1

        return result       