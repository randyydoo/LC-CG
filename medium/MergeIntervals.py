class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            start, finish = intervals[i][0], intervals[i][1]
            if start <= curr[1]:
                curr[1] = max(curr[1], finish)
            else:
                res.append(curr)
                curr = intervals[i]
        res.append(curr)
        return res
