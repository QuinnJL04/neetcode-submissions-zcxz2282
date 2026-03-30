class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        seen = set(nums)
        longest = 1
        for num in seen:
            count = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    num += 1
                    count += 1
                longest = max(longest, count)
        
        return longest
            
