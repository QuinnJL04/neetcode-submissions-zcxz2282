class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        subset = []
        def dfs(i):
            nonlocal res
            res = max(res, len(subset))

            if i >= len(nums):
                return
            if not subset or subset[-1] < nums[i]:
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
