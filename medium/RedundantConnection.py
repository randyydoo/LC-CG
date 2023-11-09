class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        def dfs(u,v):
            if u == v:
                return True
            visited.add(u)

            for neigh in graph[u]:
                if neigh not in visited and dfs(neigh, v):
                    return True
            return False

        res = [] 
        for u,v in edges:
            visited = set()
            if dfs(u,v):
                res.append([u,v])
            else:
                graph[u].append(v)
                graph[v].append(u)
        return res[-1]
