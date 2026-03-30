class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, j, mem):
            if i > j:
                return 0
            if i in mem:
                return mem[i]
            
            mem[i] = max(dfs(i + 1, j, mem), nums[i] + dfs(i+2, j, mem))
            return mem[i]
        
        return max(dfs(0, len(nums) - 2, {}), dfs(1, len(nums) - 1, {}))