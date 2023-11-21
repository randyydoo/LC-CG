class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = collections.defaultdict(list)   
        top_ord = set()

        for c, r in prerequisites:
            graph[c].append(r)
            top_ord.add(c)
            top_ord.add(r)

        def dfs(c, visited):
            nonlocal res
            if c in visited:
                return False
            if c not in top_ord:
                return True

            visited.add(c) 
            for r in graph[c]:
                if r in top_ord and not dfs(r, visited):
                    return False
            res.append(c)
            top_ord.remove(c)

            return True

        for c, r in prerequisites:
            if not dfs(c, set()):
                return []
                
        temp = []
        if len(res) < numCourses:
            for i in range(numCourses):
                if i not in res:
                    temp.append(i)

        return temp + res if prerequisites else [i for i in range(numCourses)]
