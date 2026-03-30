class Solution:
    def solve(self, board: List[List[str]]) -> None:
        o = set()

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1):
                    o.add((r, c))

        print(o)
        q = deque(o)
        safe = set(q)
        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                directions = [(0, -1), (0, 1), (1, 0), (-1,0)]
                for dr, dc in directions:
                    fr, fc = cr + dr, cc + dc
                    if 0 <= fr < ROWS and 0 <= fc < COLS and board[fr][fc] == "O":
                        #mark as safe and add to queue
                        if (fr, fc) not in safe:
                            safe.add((fr, fc))
                            q.append((fr, fc))
        
        print(safe)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
        


