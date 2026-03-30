class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        res = float('inf')

        while l <= r:
            # if nums[l] < nums[m] l and m are in the first arr search the second one

            #else if nums[l] > nums[m] then m and r are in the sec arr search that arr

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[l] <= nums[m]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m - 1
        return res



            