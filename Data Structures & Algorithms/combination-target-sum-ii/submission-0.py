class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def dfs(i, subset, total):

            if total == target:
                res.append(subset.copy())
                return

            if total > target or i >= len(candidates):
                return

            #add current num to subset
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            #undo work and then dont add current num to subset
            subset.pop()
            #skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, subset, total)

        dfs(0, subset, 0)
        return res
