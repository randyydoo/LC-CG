# DFS O(n^2)
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in adjacentPairs:
            graph[v].append(u)
            graph[u].append(v)
        
        def dfs(u, visited, res):
            visited.add(u)
            res.append(u)
            if len(res) == len(graph):
                return True
            
            for neigh in graph[u]:
                if neigh not in visited and dfs(neigh, visited, res):
                    return res

            return False

        for num in graph.keys():
            if len(graph[num]) == 1:
                return dfs(num, set(), [])
# Iterative O(n)
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in adjacentPairs:
            graph[v].append(u)
            graph[u].append(v)


        for num in graph.keys():
            if len(graph[num]) == 1:
                prev = num

        res = [prev]
        visited = set()

        while graph[prev]:
            visited.add(prev)
            nxt = graph[prev].pop()
            if nxt not in visited:
                res.append(nxt)
                prev = nxt
        return res
