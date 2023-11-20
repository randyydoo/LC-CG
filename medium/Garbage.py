class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time_cost = {0:0}
        trash = collections.defaultdict(int)
        latest = collections.defaultdict(int)
        # map trash type to its count
        # calculate total time (latest house time_cost) + counts
        prev = 0
        for i, c in enumerate(travel):
            time_cost[i+1] = c + prev
            prev += c

        for i in range(len(garbage)):
            garb = garbage[i]
            m_count, p_count, g_count = garb.count('M'), garb.count('P'), garb.count('G')
            trash['M'] += m_count
            trash['P'] += p_count
            trash['G'] += g_count
            if m_count:
                latest['M'] = max(latest['M'], i)
            if p_count:
                latest['P'] = max(latest['P'], i)
            if g_count:
                latest['G'] = max(latest['G'], i)
                
        res = 0
        for gar, ct in trash.items():
            res += (ct) + (time_cost[latest[gar]])

        return res
