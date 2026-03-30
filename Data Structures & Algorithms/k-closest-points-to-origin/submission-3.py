import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        h = []
        heapq.heapify(h)

        for coord in points:
            dist = (coord[0] - 0)**2 + (coord[1] - 0)**2
            heapq.heappush(h, (dist, coord))


        while k > 0:
            res.append(heapq.heappop(h)[1])
            k-=1
            
        return res