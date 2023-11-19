class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or len(s) <= numRows:
            return s

        ans = [''] * numRows
        i, rev = 0, False

        for c in s:
            ans[i] += c
            if i == numRows - 1:
                rev = True
                i -= 1
            elif not rev:
                i += 1
            elif rev:
                i -= 1
            if i == 0 and rev:
                rev = False
                
        return "".join(ans)
