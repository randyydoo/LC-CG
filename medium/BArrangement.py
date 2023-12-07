# sol 1
class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        valid = [True] * (n+1)
        def perm(pos):
            nonlocal res
            if pos > n:
                res += 1
                return

            for i in range(1, n+1):
                if valid[i] and (pos % i == 0 or i % pos == 0):
                    valid[i] = False
                    perm(pos+1)
                    valid[i] = True

        perm(1)
        return res

# sol 2
class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        def perm(stack):
            nonlocal res
            if len(stack) == n:
                res += 1
                return

            index = len(stack)+1
            for i in range(1, n+1):
                if i not in stack and (index % i == 0 or i % index == 0):
                    stack.add(i)
                    perm(stack)
                    stack.remove(i)

        perm(set())
        return res
