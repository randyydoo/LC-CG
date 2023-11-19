class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        min_costs = collections.defaultdict(int)

        for u,v,w in times:
            # [weight, v]
            adj[u].append([w, v])

        heap = [(0, k)] 

        while heap:
            curr_cost, curr_v = heapq.heappop(heap)

            if curr_v not in min_costs:
                min_costs[curr_v] = curr_cost
            else:
                min_costs[curr_v] = min(curr_cost, min_costs[curr_v])

            for nxt_cost, nxt_node in adj[curr_v]:
                if nxt_node not in min_costs:
                    heapq.heappush(heap, (nxt_cost+curr_cost, nxt_node))

        return max(min_costs.values()) if len(min_costs) == n else -1
