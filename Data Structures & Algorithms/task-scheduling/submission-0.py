import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        seen = {}

        for task in tasks:
            if task not in seen:
                seen[task] = 1
            else:
                seen[task] += 1

        time = 0

        h = []
        heapq.heapify(h)

        for key in seen.keys():
            heapq.heappush(h, (-seen[key], key))

        print(h)        
        
        cooldown = deque()

        while h or cooldown:
            time += 1

            if h:
                freq, task = heapq.heappop(h)

                if freq + 1 < 0:
                    cooldown.append((freq+1, task, time + n))
            if cooldown and cooldown[0][2] == time:
                    task = cooldown.popleft()[:2]
                    heapq.heappush(h, task)    
        return time                

        

        
            