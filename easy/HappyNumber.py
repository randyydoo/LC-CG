class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited and n > 1:
            visited.add(n)
            temp = 0
            s = str(n)
            for c in s:
                temp += int(int(c)**2)
            n = temp

        return True if n == 1 else False    
