import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)
        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            diff = a - b
            heapq.heappush(h, - diff)
            
        return -h[0]