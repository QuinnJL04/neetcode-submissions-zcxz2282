class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        fruit = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fruit += 1
        
        if fruit == 0:
            return 0
        
        time = 0

        directions = [(0, -1), (0, 1), (1,0), (-1,0)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 2
                    fruit -= 1
                    q.append((nr, nc))
            if q:
                time += 1
        
        return time if fruit == 0 else -1