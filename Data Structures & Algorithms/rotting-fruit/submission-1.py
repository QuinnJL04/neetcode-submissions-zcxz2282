class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque([])
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    dr, dc = r + d[0], c + d[1]
                    if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        fresh -= 1
                        q.append((dr, dc))
            if q: #count time for that wave not for each fruit rotted
                time += 1
        return time if fresh == 0 else -1