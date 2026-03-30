class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        res2 = []
        seen = set()
        if len(nums) == 0:
            return [[]]

        perms = self.permuteUnique(nums[1:])
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
                
        for arr in res:
            arr_tuple = tuple(arr)
            if arr_tuple not in seen:
                res2.append(arr)
                seen.add(arr_tuple)
        
        return res2