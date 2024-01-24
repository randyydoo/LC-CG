class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0

        mp = {}
        visited = set()
        for i in range(len(s)):
            if (s[i] in mp and mp[s[i]] != t[i]) or (s[i] not in mp and t[i] in visited):
                return 0
            mp[s[i]] = t[i]
            visited.add(t[i])

        return 1
       
