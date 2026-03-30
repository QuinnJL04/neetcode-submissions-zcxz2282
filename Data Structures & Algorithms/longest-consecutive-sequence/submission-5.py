class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #build an array of each subsequence

        #return the len(maxsubseqeunce)

        #i can build from any num s/t num - 1 not in nums

        #for O(1) look up i can convert nums to a set()

        nums = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in nums:
                count = 0
                while (num + count) in nums:
                    count += 1
                result = max(result, count)

        return result
            






