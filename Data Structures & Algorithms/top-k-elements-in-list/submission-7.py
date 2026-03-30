class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for num in seen.keys():
            freq[seen[num]].append(num)
        
        res= []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)   
                if len(res) == k:
                    return res