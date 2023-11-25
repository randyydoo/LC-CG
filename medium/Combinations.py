class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def comb(i, stack):
            if len(stack) == k:
                res.append(stack.copy())
                return
            if i > n:
                return 

            stack.append(i)
            comb(i+1, stack)
            stack.pop()
            comb(i+1,stack)
            return

        comb(1, [])
        return res
