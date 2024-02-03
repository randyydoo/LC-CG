class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr = strs[0]
        if "" in strs:
            return ""
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(curr)):
                if strs[i][j] != curr[j]:
                    break
                j += 1
            curr = curr[:j]
            if not curr:
                return ''
        return curr
        
