class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fruit = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cell = grid[r][c]
                if cell == 2:
                    q.append((r, c))
                elif cell == 1:
                    fruit += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        if fruit == 0:
            return 0
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fruit -= 1
                        q.append((nr, nc))
            if q:
                time += 1
                            
        return time if fruit == 0 else -1
                
                

            