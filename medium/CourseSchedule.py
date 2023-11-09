class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for course, req in prerequisites:
            graph[course].append(req)

        def dfs(u, v, visited):
            if u == v or v in visited:
                return False
            if v not in graph:
                return True

            visited.add(v)
            for neigh in graph[v]:
                if not dfs(u, neigh, visited):
                    return  False
            visited.remove(v)
            graph[v] = []
            return True

        for course, req in prerequisites:
            if not dfs(course, req, set()):
                return False

        return True
