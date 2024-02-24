class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        visited = {}
        for frm, to, cost in flights:
            adj[frm].append([cost, to])
            visited[frm] = float('inf')
            visited[to] = float('inf')
        
        res = float("inf")
        h = [[0, 0, src]] #[cost, stops, curr]

        while h:
            for _ in range(len(h)):
                stops, cost, curr = heappop(h)
                if curr == dst:
                    res = min(res, cost)
                    continue
                visited[curr] = cost
                for nxt_cost, nxt_stop in adj[curr]:
                    if stops <= k and cost+nxt_cost<=visited[nxt_stop]:
                        heappush(h,[stops+1,cost+nxt_cost, nxt_stop])

        return res if res != float("inf") else -1
