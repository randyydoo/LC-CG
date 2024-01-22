class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        mp = {-1:0, 0: 1}

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                mp[i] = mp[i-1]+1
            else:
                mp[i] = 1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                mp[i] = max(mp[i], mp[i+1]+1)

        return sum(mp.values()
