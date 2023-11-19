class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        word = 1
        i = 0
        length = min(len(s) for s in strs)

        def helper(s1, s2, i):
            if s1[i] == s2[i]:
                return True
            return False
            
        while i <= length - 1:
            if not helper(strs[0], strs[word], i):
                break
            elif word != len(strs) - 1:
                word += 1
                continue
            else:
                word = 1
                i += 1
        return strs[0][:i]

