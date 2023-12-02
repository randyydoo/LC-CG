class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cts = collections.defaultdict(int)
        res = 0

        for c in chars:
            cts[c] += 1
        
        for s in words:
            temp = cts.copy()
            tmp = 0
            for c in s:
                if not cts[c]:
                    break
                tmp += 1
                cts[c] -= 1
            if tmp == len(s):
                res += len(s)
            cts = temp
        return res
