class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r,c))

        directions = [(0, -1), (0, 1), (1,0), (-1,0)]
        count = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == -1:
                        continue
                    if (nr, nc) in visit:
                        continue
                    grid[nr][nc] = count
                    visit.add((nr, nc))
                    q.append((nr, nc))
            if q:
                count += 1


                    


                



