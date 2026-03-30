import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

        order = []
        heapq.heapify(order)

        for key in seen.keys():
            heapq.heappush(order, (-seen[key], key))


        res = []

        for i in range(k):
            res.append(heapq.heappop(order)[1])

        return res