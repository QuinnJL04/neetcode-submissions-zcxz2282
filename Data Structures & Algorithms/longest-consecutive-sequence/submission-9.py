class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        longest = 0
        for num in nums:
            count = 1
            left = num - 1
            if left not in seen:
                count = 1
                while num + 1 in seen:
                    count += 1
                    num += 1
            longest = max(longest, count)

        return longest
            
