class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k':0}
        res, over = 0, 0
        def valid(d):
            return (d['c'] >= d['r'] >= d['o'] >= d['a'] >= d['k'])

        for c in croakOfFrogs:
            d[c] += 1
            if not valid(d):
                return -1
            
            if c == 'c':
                over += 1
            elif c == 'k':
                over -= 1
                
            res = max(res, over)
        if over == 0:
                return res
        return -1
