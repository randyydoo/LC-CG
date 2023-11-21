class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        for i in range(len(s)):
            temp = set()
            temp.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in temp:
                    break
                else:
                    temp.add(s[j])
            if len(temp) > curr:
                curr = len(temp)
        return curr
