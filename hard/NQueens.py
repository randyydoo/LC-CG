class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.' * n for i in range(n)]
        res = []
        cols, p_diags, n_diags = set(), set(), set()

        def fill(r):
            if r == n:
                res.append(board.copy())
                return 

            for j in range(n):
                if j not in cols and (r+j) not in p_diags and (r-j) not in n_diags:
                    cols.add(j)
                    p_diags.add(r+j)
                    n_diags.add(r-j)
                    board[r] = board[r][:j] + 'Q' + board[r][j+1:]
                    fill(r+1)
                    cols.remove(j)
                    p_diags.remove(r+j)
                    n_diags.remove(r-j)
                    board[r] = '.' * n

            return 

        fill(0)
        return res
