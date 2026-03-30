import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        dist = {}
        #init a adjacency list
        adj_list = defaultdict(list)
        #init a min heap
        heap = [(0, k)]
        heapq.heapify(heap)

        for start, end, time in times:
            adj_list[start].append((end, time))

        while heap:
            time, node = heapq.heappop(heap)
            #if node has been visited we skip (min heap enforces that we have the abs min path)
            if node in visited:
                continue
            visited.add(node)
            dist[node] = time

            for nei, cur_time in adj_list[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + cur_time, nei))

        if len(dist) < n:
            return -1
        return max(dist.values())

        
