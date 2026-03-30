from heapq import heappop, heappush, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        heapify(heap)
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        for key in seen.keys():
            heappush(heap, (-seen[key], key))

        for i in range(0, k):
            result.append(heappop(heap)[1])
        return result

            
