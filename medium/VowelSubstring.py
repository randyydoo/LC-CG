class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr_ct, res = 0, 0
        for i in range(k):
            if s[i] in vowels:
                curr_ct += 1

        i = 0
        res = max(res,curr_ct)
        for j in range(k, len(s)):
            if s[i] in vowels:
                curr_ct -=1
            if s[j] in vowels:
                curr_ct += 1
            i += 1
            res = max(res, curr_ct)

        return res
