class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num]=1
            else:
                seen[num] += 1
        
        for num in seen.keys():
            if seen[num] == 1:
                return num