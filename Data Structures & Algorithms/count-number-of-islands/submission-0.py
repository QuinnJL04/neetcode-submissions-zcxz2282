class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        #for each new island explore all adjacent 1's and add to visited
        def dfs(row, col):
            #out of bounds
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                return
            #water or in visited
            if grid[row][col] == "0" or (row, col) in visited:
                return

            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        #scan over the grid and call dfs on new islands
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
            
        return count 

