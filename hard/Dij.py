class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = collections.defaultdict(list)
        for curr, to, cost in edges:
            self.graph[curr].append([cost, to])

    def addEdge(self, edge: List[int]) -> None:
        curr, to, cost = edge[0], edge[1], edge[2]
        self.graph[curr].append([cost, to])

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [[0, node1]]
        visited = set()
        while heap:
            cost, node = heapq.heappop(heap)
            visited.add(node) 

            if node == node2:
                return cost
            for nxt_cost, nxt_node in self.graph[node]:
                if nxt_node not in visited:
                    heapq.heappush(heap, [cost+nxt_cost, nxt_node])

        return -1

