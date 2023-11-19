class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        prev_max = 0
        
        for l in left:
            prev_max = max(prev_max,l)
        
        for r in right:
            prev_max = max(prev_max, n-r)
            
        return prev_max
