class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
            
        s_mp, t_mp = defaultdict(int), defaultdict(int)
        for c in t:
            t_mp[c] += 1

        valid = 0
        res = [float("-inf"), float("inf")]
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            if c in t_mp:
                s_mp[c] += 1
            if s_mp[c] == t_mp[c]:
                valid += 1
            while l <= r and valid == len(t_mp):
                if s_mp[s[l]]:
                    s_mp[s[l]] -= 1
                if r+1-l < res[1]-res[0]:
                    res = [l, r+1]
                if s_mp[s[l]] < t_mp[s[l]]:
                    valid -= 1
                l += 1
            r += 1

        return '' if res[0] == float('-inf') else s[res[0]:res[1]]
