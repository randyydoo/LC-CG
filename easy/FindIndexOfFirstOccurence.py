class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 1:
               return haystack.find(needle)
        for i in range(0, len(haystack) - 1):
            #return i sub (len(haystack) - 1)
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
