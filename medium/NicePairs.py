class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res = 0
        rev = collections.defaultdict(int)
        for num in nums:
            rev_num = int(str(num)[::-1])
            res += rev[num-rev_num]
            rev[num-rev_num] += 1

        return res % (10**9 + 7)
