import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # if we cant get to all nodes from k return -1 
        # else return the min time to travel to all nodes
        visited = set()
        dist = {}
        adj_list = defaultdict(list)

        heap = [(0, k)]
        heapq.heapify(heap)

        for time in times:
            start = time[0]
            end = time[1]
            t = time[2]
            adj_list[start].append((end, t))

        while heap:
            time, node = heapq.heappop(heap)
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

        
