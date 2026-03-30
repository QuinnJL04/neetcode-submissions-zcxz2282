class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        seen = {}
        for i in range(len(nums)):
            curr_num = nums[i] 
            if curr_num not in seen:
                seen[curr_num] = 1
            else:
                seen[curr_num] += 1
        
        print(seen)
        for key in seen.keys():
            value = (-seen[key], key)
            heapq.heappush(heap, value)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result