class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max = 1
        i = 0
        while i <= len(s) - 1:
            temp = set()
            temp.add(s[i])
            j = i + 1
            while True: 
                if j > len(s) - 1 or s[j] in temp:
                    break
                else:
                    temp.add(s[j])
                    j += 1
            if len(temp) > max:
                max = len(temp)
            i += 1
        return max
