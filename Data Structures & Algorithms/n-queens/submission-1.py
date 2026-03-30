class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        res = []
        cols = set()
        posDiag = set()
        negDiag = set()
        board = ['.' * n for _ in range(n)]
        def dfs(row):
            if row == n:
                res.append(board.copy())
                return
            for col in range(n):
                if col in cols or (row+col) in posDiag or (row-col) in negDiag:
                    continue
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                dfs(row + 1)
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
        
        dfs(0)
        return res

