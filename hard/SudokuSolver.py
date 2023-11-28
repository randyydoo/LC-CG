class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)
        empty = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.add((i,j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    grids[(3*(i//3)+(j//3))].add(val)

        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i+1,0) 
            if (i,j) in empty:
                for num in range(1,10):
                    val = str(num)
                    if val not in rows[i] and val not in cols[j] and val not in grids[3*(i//3)+(j//3)]:
                        board[i][j] = val
                        rows[i].add(val)
                        cols[j].add(val)
                        grids[(3*(i//3)+(j//3))].add(val)
                        nxt = dfs(i, j+1)
                        if nxt:
                            return True
                        board[i][j] = '.'
                        rows[i].remove(val)
                        cols[j].remove(val)
                        grids[(3*(i//3)+(j//3))].remove(val)
                return False
            return dfs(i, j+1)
    
        dfs(0,0)
