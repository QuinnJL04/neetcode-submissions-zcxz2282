class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def dfs(i):
            if i >= len(nums):
                return 0 
            if i in mem:
                return mem[i]
            
            mem[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return mem[i]
        
        return dfs(0)
            
            
            
