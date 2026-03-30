class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for num in nums:
            count = 0
            if num - 1 not in nums:
                #then num is a starting subseq
                while (num + count) in nums:
                    count+=1

            result = max(result, count)
        return result