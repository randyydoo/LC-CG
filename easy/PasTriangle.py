# iterative
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    prev = res[i-1][j-1] + res[i-1][j]
                    temp.append(prev)
            res.append(temp)

        return res

# recursive
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        def dfs(row,temp):
            if row >= numRows:
                return 
            
            for i in range(row+1):
                if i == 0 or i == row:
                    temp.append(1)
                else:
                    temp.append(res[row-1][i-1]+res[row-1][i])

            res.append(temp)
            dfs(row+1, [])
            return 

        dfs(0, [])
        return res
