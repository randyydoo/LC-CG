class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''  
        detect cycle
        '''

        indeg = [0] * numCourses
        d = {i:[] for i in range(numCourses)}
        q = collections.deque()

        for course, req in prerequisites:
            indeg[course] += 1
            d[req].append(course)

        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        visited = 0
        while q:
            vertex = q.popleft()
            visited += 1
            for neigh in d[vertex]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)

        return visited == numCourses
