class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        curr_prod = 1
        for i in range(1, len(nums)):
            curr_prod *= nums[i-1]
            prefix[i] = curr_prod 
        print(prefix)

        suffix = [1] * len(nums)
        curr_prod_2 = 1
        for j in range(len(nums) - 2, -1, -1):
            curr_prod_2 *= nums[j+1]
            suffix[j] = curr_prod_2
        print(suffix)

        result = [1] * len(nums)

        for k in range(len(nums)):
            result[k] = prefix[k] * suffix[k]

        return result

